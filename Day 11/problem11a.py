# The problem input is a sequence of directions
# with each being the direction of a step.
# Unfortunately, the directions correspond to a
# hex grid. The hexagons ("hexes") in this grid
# are aligned such that adjacent hexes can be
# found to the north, northeast, southeast, south,
# southwest, and northwest:
#       \ n  /
#     nw +--+ ne
#       /    \
#     -+      +-
#       \    /
#     sw +--+ se
#       / s  \
# From the starting point, we need to determine
# the fewest number of steps required to reach the
# final location. (A "step" means to move from the
# hex you are in to any adjacent hex.)
#
# After following the directional steps, what is
# the shortest distance from the start point to
# the end point.

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


# Return a list of directional steps based on the
# input string being split at the commas.
def parseInput(values):
   return values.split(',')

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and the first (and only)
   # string in the list is the input.   
   fileInput = readFile("input11b.txt")
   steps = parseInput(fileInput[0])

   # To solve this problem, we use the cube
   # coordinates, as described at:
   # https://www.redblobgames.com/grids/hexagons/

   # Initialize the starting location (0, 0, 0).
   x = y = z = 0

   # Iterate through each of the steps and update
   # the location.
   for direction in steps:
      # North
      if direction == 'n':
         y += 1
         z -= 1
      # North-East
      elif direction == 'ne':
         x += 1
         z -= 1
      # South-East
      elif direction == 'se':
         x += 1
         y -= 1
      # South
      elif direction == 's':
         y -= 1
         z += 1
      # South-West
      elif direction == 'sw':
         x -= 1
         z += 1
      # North-West
      elif direction == 'nw':
         x -= 1
         y += 1

   # Calculate the distance from the start point.
   distance = (abs(x) + abs(y) + abs(z)) // 2

   # Display the distance from the start point. 
   print("Distance = " + str(distance))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
