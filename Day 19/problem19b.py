# The problem input is a routing diagram. The
# program needs to follow the routing diagram with
# the starting point just off the top of the
# diagram. Lines (drawn with |, -, and +) show the
# path to take, starting by going down onto the
# only line connected to the top of the diagram.
# Follow this path until it reaches the end
# (located somewhere within the diagram) and stop
# there. Sometimes, the lines cross over each
# other; in these cases, it needs to continue
# going the same direction, and only turn left or
# right when there's no other option. In addition,
# someone has left letters on the line; these also
# don't change its direction, but it can use them
# to keep track of where it's been.
#
# How many steps does the program need to take to
# reach the end of the path?

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
   

# Convert the file input to a list of lists
# representing the network diagram.
def parseInput(values):
   diagram = list()
   for line in values:
      diagram.append(list(line))

   return diagram


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to integer.
   fileInput = readFile("input19b.txt")
   diagram = parseInput(fileInput)

   # Find starting value for x.
   start_x = 0
   start_y = 0
   for x in range(len(diagram[0])):
      if diagram[0][x] == '|':
         start_x = x
         break

   # Set the initial conditions.
   done = False
   string = ''
   current = '|'
   x = start_x
   y = start_y
   direction = 'down'
   steps = -1 # Eliminate off-by-one

   # Follow path until end, finding characters
   # along the way.
   while not done:
      steps += 1
      # If the current position is whitespace,
      # then done.
      if diagram[y][x] == ' ':
         done = True

      # Handle downward traversal.
      elif (current == '|') and (direction == 'down'):
         # Reached a corner; determine the next
         # direction. Looking for non-whitespace.
         if diagram[y][x] == '+':
            if diagram[y][x-1] != ' ':
               x = x - 1
               current = '-'
               direction = 'left'
            elif diagram[y][x+1] != ' ':
               x = x + 1
               current = '-'
               direction = 'right'
            elif diagram[y+1][x] != ' ':
               y = y + 1

         # If character is encountered, add it to
         # the string.
         elif diagram[y][x].isalpha():
            string += diagram[y][x]
            y += 1

         # Handle crossing path.
         else:
            y += 1

      # Handle upward traversal.
      elif (current == '|') and (direction == 'up'):
         # Reached a corner; determine the next
         # direction. Looking for non-whitespace.
         if diagram[y][x] == '+':
            if diagram[y][x-1] != ' ':
               x = x - 1
               current = '-'
               direction = 'left'
            elif diagram[y][x+1] != ' ':
               x = x + 1
               current = '-'
               direction = 'right'
            elif diagram[y-1][x] != ' ':
               y = y - 1

         # If character is encountered, add it to
         # the string.
         elif diagram[y][x].isalpha():
            string += diagram[y][x]
            y -= 1

         # Handle crossing path.
         else:
            y -= 1

      # Handle traversal to left.
      elif (current == '-') and (direction == 'left'):
         # Reached a corner; determine the next
         # direction. Looking for non-whitespace.
         if diagram[y][x] == '+':
            if diagram[y-1][x] != ' ':
               y = y - 1
               current = '|'
               direction = 'up'
            elif diagram[y+1][x] != ' ':
               y = y + 1
               current = '|'
               direction = 'down'
            elif diagram[y][x-1] != ' ':
               x = x - 1

         # If character is encountered, add it to
         # the string.
         elif diagram[y][x].isalpha():
            string += diagram[y][x]
            x -= 1

         # Handle crossing path.
         else:
            x -= 1

      # Handle traversal to right.
      elif (current == '-') and (direction == 'right'):
         # Reached a corner; determine the next
         # direction. Looking for non-whitespace.
         if diagram[y][x] == '+':
            if diagram[y-1][x] != ' ':
               y = y - 1
               current = '|'
               direction = 'up'
            elif diagram[y+1][x] != ' ':
               y = y + 1
               current = '|'
               direction = 'down'
            elif diagram[y][x+1] != ' ':
               x = x + 1

         # If character is encountered, add it to
         # the string.
         elif diagram[y][x].isalpha():
            string += diagram[y][x]
            x += 1

         # Handle crossing path.
         else:
            x += 1

   

   # Display the number of steps taken to reach
   # the end of the path.
   print("Number of steps = " + str(steps))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
