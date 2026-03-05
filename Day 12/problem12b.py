# The problem input consists of a list of programs
# that are connected to each other. Messages are
# passed between programs, but most programs are
# not connected to each other directly. Instead,
# programs pass messages between each other until
# the message reaches the intended recipient. For
# some reason, though, some of these messages are
# not ever reaching their intended recipient. Each
# program has one or more programs with which it
# can communicate, and these pipes are
# bidirectional; if 8 says it can communicate with
# 11, then 11 will say it can communicate with 8.
#
# Determine how many groups there are in total.

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


# Convert the program input into an adjacency list
# by splitting the left value from the right
# value(s). Then add a dictionary entry with the
# left value as the key and the values as a list
# of the right values.
def parseInput(values):
   adjacent = dict()
   for line in values:
      # Remove all commas
      line = line.replace(',', '')

      # Split on white space.
      line = line.split()

      # Add the new dictionary entry.
      if line[0] not in adjacent:
         adjacent[line[0]] = list()

      # Add each value to the dictionary entry.
      for node in line[2:]:
         adjacent[line[0]].append(node)

   # Return the adjacency list.
   return adjacent

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it into an
   # adjacency list.
   fileInput = readFile("input12b.txt")
   adjacent = parseInput(fileInput)

   # Create a set of all programs.
   programs = set()
   for key in adjacent:
      programs.add(key)

   # Iterate while there are still programs that
   # have not been visited.
   groups = 0
   while len(programs) > 0:
      # Perform BFS to count the number of reachable
      # programs from the program ID 0.
      visited = set()
      prog_list = list(programs)
      visited.add(prog_list[0])
      toVisit = [ prog_list[0] ]
      # Iterate while there are still nodes to visit.
      while len(toVisit) > 0:
         # Visit the next program.
         current = toVisit.pop(0)

         # Iterate through each neighbor to the
         # current program and add it to the toVisit
         # list if it has not already been seen.
         for neighbor in adjacent[current]:
            if neighbor not in visited:
               toVisit.append(neighbor)
               visited.add(neighbor)

      # Increment the number of groups and remove
      # all visited programs from the set of
      # remaining, unvisited programs.
      groups += 1
      programs = programs - visited

   # Display the number of programs groups.
   print("Number of program groups: " + str(groups))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
