# The problem input is a map of a portion of a
# grid computing cluster that is partially
# infected. Clean nodes are shown as .; infected
# nodes are shown as #. This map only shows the
# center of the grid; there are many more nodes
# beyond those shown, but none of them are
# currently infected. Exactly one virus carrier
# moves through the network, infecting or cleaning
# nodes as it moves. The virus carrier is always
# located on a single node in the network (the
# current node) and keeps track of the direction
# it is facing. To avoid detection, the virus
# carrier works in bursts; in each burst, it wakes
# up, does some work, and goes back to sleep. The
# following steps are all executed in order one
# time each burst:
# - If the current node is infected, it turns to
#   its right. Otherwise, it turns to its left.
#   (Turning is done in-place; the current node
#   does not change.)
# - If the current node is clean, it becomes
#   infected. Otherwise, it becomes cleaned. (This
#   is done after the node is considered for the
#   purposes of changing direction.)
# - The virus carrier moves forward one node in
#   the direction it is facing.
# The virus carrier begins in the middle of the
# map facing up.
#
# Given your actual map, after 10000 bursts of
# activity, how many bursts cause a node to become
# infected?

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
   

# Convert the grid of file input denoting the
# positions of clean and infected nodes (# are
# infected and . are clean). The result is a set
# of (x, y) coordinates in a set in which each
# coordinate is an infected node.
def parseInput(values):
   infected = set()

   # Iterate through each location in the grid.
   for y in range(len(values)):
      for x in range(len(values[y])):
         # If the location is infected, add it to
         # the set.
         if values[y][x] == '#':
            infected.add((x, y))

   start_x = len(values[0]) // 2
   start_y = len(values) // 2

   # Return the set of infected coordinates and
   # the starting position of the virus carrier.
   return (infected, start_x, start_y)


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to integer.
   fileInput = readFile("input22b.txt")
   infected, x, y = parseInput(fileInput)

   directions = [ 'up', 'right', 'down', 'left' ]

   # Initial facing is specified to 'up'.
   facing = 0

   # Number of bursts of activity to simulate.
   bursts = 10000
   caused = 0

   # Simulate the bursts.
   for _ in range(bursts):
      # If the current node is infected, it turns
      # to its right and removes the infection.
      if (x, y) in infected:
         facing = (facing + 1) % len(directions)
         infected.remove((x, y))

      # If the current node is not infected, it
      # turns to its left and adds the infection.
      else:
         facing = (facing - 1) % len(directions)
         infected.add((x, y))
         caused += 1

      # Carrier moves forward by one step.
      if directions[facing] == 'up':
         y -= 1
      elif directions[facing] == 'right':
         x += 1
      elif directions[facing] == 'down':
         y += 1
      elif directions[facing] == 'left':
         x -= 1
   
   # Display the number of infections caused.
   print("Number of infections caused = " + str(caused))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
