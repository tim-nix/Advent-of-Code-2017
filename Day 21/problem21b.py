# The input to this problem is a set of rules for
# enhancing the detail of an image.  The image
# consists of a two-dimensional square grid of
# pixels that are either on (#) or off (.). The
# program always begins with this pattern:
#
#     .#.
#     ..#
#     ###
#
# Because the pattern is both 3 pixels wide and 3
# pixels tall, it is said to have a size of 3.
# Then, the program repeats the following process:
# - If the size is evenly divisible by 2, break
#   the pixels up into 2x2 squares, and convert
#   each 2x2 square into a 3x3 square by following
#   the corresponding enhancement rule.
# - Otherwise, the size is evenly divisible by 3;
#   break the pixels up into 3x3 squares, and
#   convert each 3x3 square into a 4x4 square by
#   following the corresponding enhancement rule.
# Because each square of pixels is replaced by a
# larger one, the image gains pixels and so its
# size increases. Sometimes, one must rotate or
# flip the input pattern to find a match. (Never
# rotate or flip the output pattern, though.) Each
# pattern is written concisely: rows are listed as
# single units, ordered top-down, and separated by
# slashes.
#
# How many pixels stay on after 18 iterations?

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
   

# Convert the file input into a dictionary of
# rules such in which the input grid is mapped to
# an larger (by one) ouput grid. Also, convert
# each grid from the '/' separated representation
# in the file input into a 2d list.
def parseInput(values):
   mappings = dict()
   # Iterate through the file rule representation.
   for line in values:
      line = line.replace(' ', '')
      
      # Separate the input from the output.
      parts = line.split('=>')

      # Convert the input to a grid.
      key = tuple([ tuple(k) for k in parts[0].split('/') ])

      # Convert the output to a grid.
      value = tuple([ tuple(k) for k in parts[1].split('/') ])

      # Add the rule to the dictionary.
      mappings[key] = value

   # Return the rules.
   return mappings
      

if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to dictionary
   # of rules.
   fileInput = readFile("input21b.txt")
   mappings = parseInput(fileInput)

   # For each rule, add additional rules for
   # rotations and flips.
   full_mappings = dict()
   for key in mappings:
      full_mappings[key] = mappings[key]
      # Rotate and flip 4 times.
      old_key = key
      for _ in range(3):
         # Rotate 90 degrees
         rot_key = list()
         for x in range(len(old_key)):
            row = list()
            for y in range(len(old_key)-1, -1, -1):
               row.append(old_key[y][x])
            rot_key.append(tuple(row))
         rot_key = tuple(rot_key)
         full_mappings[rot_key] = mappings[key]
         old_key = rot_key

         # If 3x3 grid then flip.
         if len(rot_key) == 3:
            # Flip horizontally.
            hzl_key = tuple([ rot_key[2], rot_key[1], rot_key[0] ])
            full_mappings[hzl_key] = mappings[key]
            # No need to flip vertically.
   
   # Define starting grid.
   grid = tuple([ tuple(list('.#.')), tuple(list('..#')), tuple(list('###')) ])
   
   # Evolve grids
   num_iterations = 18
   for _ in range(num_iterations):
      # If the grid is divisible by 2, then split
      # into 4x4 bites.
      if (len(grid) % 2 == 0):
         step = 2
      # Otherwise, split into 3x3 bites.
      elif (len(grid) % 3 == 0):
         step = 3

      # Iterate through the grid and process each
      # bite to generate the new grid.
      next_grid = list()
      next_row = 0
      for col in range(0, len(grid), step):
         next_grid += [ list() for _ in range(step + 1) ]
         for row in range(0, len(grid[0]), step):
            # Extract the bite.
            bite = tuple([ tuple(r[row:row+step]) for r in grid[col:col+step] ])
            # Map the bite to the result.
            result = full_mappings[bite]

            # Add the result to the new grid.
            for offset in range(len(result)):
               next_grid[next_row + offset] += result[offset]

         # Increment the start of the next rows in
         # the next grid.
         next_row += len(result)

      # The next grid becomes the current grid for
      # the next iteration.
      grid = next_grid

   # Count 'on' pixels by iterating through the
   # grid and counting the number of '#'.
   count = 0
   for row in grid:
      for col in row:
         if col == '#':
            count += 1

   # Display the number of 'on' pixels.
   print("Number of 'on' pixels = " + str(count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
