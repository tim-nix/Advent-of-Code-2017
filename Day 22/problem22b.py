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
# up, does some work, and goes back to sleep. Now,
# before it infects a clean node, it will weaken
# it to disable your defenses. If it encounters an
# infected node, it will instead flag the node to
# be cleaned in the future. So:
# - Clean nodes become weakened.
# - Weakened nodes become infected.
# - Infected nodes become flagged.
# - Flagged nodes become clean.
# Every node is always in exactly one of the above
# states. The virus carrier still functions in a
# similar way, but now uses the following logic
# during its bursts of action:
# - Decide which way to turn based on the current
#   node:
#   -- If it is clean, it turns left.
#   -- If it is weakened, it does not turn, and
#      will continue moving in the same direction.
#   -- If it is infected, it turns right.
#   -- If it is flagged, it reverses direction,
#      and will go back the way it came.
# Modify the state of the current node, as
# described above. The virus carrier moves forward
# one node in the direction it is facing. The
# virus carrier begins in the middle of the map
# facing up.
#
# Given your actual map, after 10000000 bursts of
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
# infected and . are clean). The result is a
# dictionary in which the key is a tuple of the
# (x, y)-coordinates and the value states that
# the key is 'infected'.
def parseInput(values):
   infected = dict()

   # Iterate through each location in the grid.
   for y in range(len(values)):
      for x in range(len(values[y])):
         # If the location is infected, add it to
         # the set.
         if values[y][x] == '#':
            infected[(x, y)] = 'infected'

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
   affected, x, y = parseInput(fileInput)

   directions = [ 'up', 'right', 'down', 'left' ]

   # Initial facing is specified to 'up'.
   facing = 0

   # Number of bursts of activity to simulate.
   bursts = 10000000
   caused = 0

   # Simulate the bursts.
   for _ in range(bursts):
      # If the current node is clean, it becomes
      # weakened and turns to the left.
      if (x, y) not in affected:
         affected[(x, y)] = 'weakened'
         facing = (facing - 1) % len(directions)

      # If the current node is weakened, it
      # becomes infected and does not turn.
      # Increment the number of noded infected.
      elif affected[(x, y)] == 'weakened':
         affected[(x, y)] = 'infected'
         caused += 1

      # If the current node is infected, it
      # becomes flagged and turns to the right.
      elif affected[(x, y)] == 'infected':
         affected[(x, y)] = 'flagged'
         facing = (facing + 1) % len(directions)

      # If the current node is flagged, it
      # becomes clean and reverses direction.
      elif affected[(x, y)] == 'flagged':
         del affected[(x, y)]
         facing = (facing + 2) % len(directions)

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
        
    
        
