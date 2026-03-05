# The problem input is a position location within
# a grid. Each square on the grid is allocated in
# a spiral pattern starting at a location marked 1
# and then spiraling outward. Store the value 1 in
# square 1. Then, store the sum of the values in
# all adjacent squares, including diagonals. Once
# a square is written, its value does not change.
# Therefore, the first few squares would receive
# the following values:
#    147  142  133  122   59
#    304    5    4    2   57
#    330   10    1    1   54
#    351   11   23   25   26
#    362  747  806--->   ...
# 
# Find the first value written that is larger than
# the puzzle input.

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


# Calculate the sum of all the neighbors (among
# neighbors with existing values).
def calcValue(x, y, positions):
   deltas = [ (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1) ]
   sum = 0
   # Iterate through each neighbor.
   for dx, dy in deltas:
      # If a value is stored for the neighbor, add
      # it to the sum.
      if (x+dx, y+dy) in positions:
         sum += positions[(x+dx, y+dy)]
   
   # Return the sum.
   return sum
   
      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to integer.   
   fileInput = readFile("input3b.txt")
   number = int(fileInput[0])

   # Starting at position 1 (x = 0, y = 0), move
   # to each location within the spiral and
   # calculate the sum of the neighbors of that
   # location.
   width = 0
   height = 0
   x = 0
   y = 0
   positions = dict()
   positions[(x, y)] = 1
   found = False
   while True:
      # Go right
      width += 1
      # Iterate through each location.
      for i in range(x+1, x + width + 1):
         # Sum the neighbors.
         positions[(i, y)] = calcValue(i, y, positions)
         # If resulting sum is large enough, exit
         # the loops.
         if positions[(i, y)] > number:
            x = i
            found = True
            break
      else:
         x += width

      # If the location was found, exit out of the
      # outer loop, as well.
      if found:
         break
      
      # Go up
      height += 1
      # Iterate through each location.
      for j in range(y+1, y + height + 1):
         # Sum the neighbors.
         positions[(x, j)] = calcValue(x, j, positions)
         # If resulting sum is large enough, exit
         # the loops.
         if positions[(x, j)] > number:
            y = j
            found = True
            break
      else:
         y += height

      # If the location was found, exit out of the
      # outer loop, as well.
      if found:
         break
      
      # Go left
      width += 1
      # Iterate through each location.
      for i in range(x-1, x-width-1, -1):
         # Sum the neighbors.
         positions[(i, y)] = calcValue(i, y, positions)
         # If resulting sum is large enough, exit
         # the loops.
         if positions[(i, y)] > number:
            x = i
            found = True
            break
      else:
         x -= width

      # If the location was found, exit out of the
      # outer loop, as well.
      if found:
         break
      
      # Go down
      height += 1
      # Iterate through each location.
      for j in range(y-1, y-height-1, -1):
         # Sum the neighbors.
         positions[(x, j)] = calcValue(x, j, positions)
         # If resulting sum is large enough, exit
         # the loops.
         if positions[(x, j)] > number:
            y = j
            found = True
            break
      else:
         y -= height

      # If the location was found, exit out of the
      # outer loop, as well.
      if found:
         break
      
   # Display the first value written that is
   # larger than the puzzle input. 
   print("Final value = " + str(positions[(x, y)]))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
