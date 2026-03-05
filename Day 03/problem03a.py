# The problem input is a position location within
# a grid. Each square on the grid is allocated in
# a spiral pattern starting at a location marked 1
# and then counting up while spiraling outward.
# For example, the first few squares are allocated
# like this:
#    17  16  15  14  13
#    18   5   4   3  12
#    19   6   1   2  11
#    20   7   8   9  10
#    21  22  23---> ...
#
# Find the Manhattan Distance between the input
# position and square 1.

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

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to integer.   
   fileInput = readFile("input3b.txt")
   number = int(fileInput[0])

   # Starting at position 1 (x = 0, y = 0), move
   # to each corner of the spiral, keeping track
   # of the x,y coordinates of the corners and
   # position.
   width = 0
   height = 0
   x = 0
   y = 0
   position = 1
   while position < number:
      # Go right
      width += 1
      x += width
      position += width

      # Check to see if corner position exceeds
      # input position, and if so, backtrack and
      # break out of loop.
      if position > number:
         difference = position - number
         x -= difference
         break
      
      # Go up
      height += 1
      y += height
      position += height

      # Check to see if corner position exceeds
      # input position, and if so, backtrack and
      # break out of loop.
      if position > number:
         difference = position - number
         y -= difference
         break
      
      # Go left
      width += 1
      x -= width
      position += width

      # Check to see if corner position exceeds
      # input position, and if so, backtrack and
      # break out of loop.
      if position > number:
         difference = position - number
         x += difference
         break
      
      # Go down
      height += 1
      y -= height
      position += height

      # Check to see if corner position exceeds
      # input position, and if so, backtrack and
      # break out of loop.
      if position > number:
         difference = position - number
         y += difference
         break
      
   # Display the Manhatten distance. 
   print("Distance = " + str(abs(x) + abs(y)))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
