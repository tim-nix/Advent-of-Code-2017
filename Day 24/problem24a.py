# The problem input is an inventory of components
# by their port types; that is, each component has
# two ports, one on each end. The ports come in
# all different types, and only matching types can
# be connected. Each port is identified by the
# number of pins it uses; more pins mean a
# stronger connection for your bridge. The first
# port you use must be of type 0. It doesn't
# matter what type of port you end with; your goal
# is just to make the bridge as strong as
# possible. The strength of a bridge is the sum of
# the port types in each component.
#
# What is the strength of the strongest bridge you
# can make with the components you have available?

import time     # For timing the execution

# Read in the data file and convert it to a list
# of strings.
def readFile(filename):
   lines = []
   try:
      with open(filename, "r") as file:
         line = file.readline()
         while line:
            lines.append(line.replace('\n', ''))
            line = file.readline()

         file.close()
            
   except FileNotFoundError:
      print("Error: File not found!")
   except:
      print("Error: Can't read from file!")
   
   return lines
   

# Convert each line of file input into a tuple of
# two integers, each representing a component.
def parseInput(values):
   components = list()

   # Iterate through each component. Split on the
   # '/', convert numbers to integers, and store.
   for line in values:
      parts = line.split('/')
      components.append((int(parts[0]), int(parts[1])))

   # Return list of components.
   return components


# Recursively build the bridge of components and
# return the strength of the bridge.
def buildBridge(current, visited, path, components):
   max_strength = 0

   # Iterate through the components.
   for c in components:
      # Make sure that the component has not been
      # used and fits the currently exposed port.
      if (c not in visited):
         # Add the component and recursively call
         # to add the next component.
         if c[0] == current:
            strength = sum(c) + buildBridge(c[1], visited.union({ c }), path + [ c ], components)

            # If this completed bridge is the
            # strongest seen, then track it.
            if strength > max_strength:
               max_strength = strength

         # The component fits in backwards.
         elif c[1] == current:
            strength = sum(c) + buildBridge(c[0], visited.union({ c }), path + [ (c[1], c[0]) ], components)

            # If this completed bridge is the
            # strongest seen, then track it.
            if strength > max_strength:
               max_strength = strength

   # Return the strength of the best bridge seen.
   return max_strength


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to integer.
   fileInput = readFile("input24b.txt")
   components = parseInput(fileInput)

   # Perform BFS to generate bridges and find the
   # strength of the strongest bridge. The first
   # port is zero (0).
   max_strength = buildBridge(0, set(), list(), components)
   
   # Display the strength of the strongest bridge.
   print("Strongest bridge = " + str(max_strength))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
