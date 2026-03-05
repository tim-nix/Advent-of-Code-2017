# The problem input is a sequence of integers
# corresponding to lengths along a rope. The rope
# is a circle of string with 256 marks on it.
# Based on the input, the function repeatedly
# selects a span of string, brings the ends
# together, and gives the span a half-twist to
# reverse the order of the marks within it. After
# doing this many times, the order of the marks is
# used to generate the answer. Begin with a list
# of numbers from 0 to 255, a current position
# which begins at 0 (the first element in the
# list), a skip size (which starts at 0), and a
# sequence of lengths (your puzzle input). Then,
# for each length:
# - Reverse the order of that length of elements
#   in the list, starting with the element at the
#   current position.
# - Move the current position forward by that
#   length plus the skip size.
# - Increase the skip size by one.
# The list is circular; if the current position
# and the length try to reverse elements beyond
# the end of the list, the operation reverses
# using as many extra elements as it needs from
# the front of the list. If the current position
# moves past the end of the list, it wraps around
# to the front. Lengths larger than the size of
# the list are invalid.
#
# After all operations are applied, what is the
# result of multiplying the first two numbers in
# the list?

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


# Convert the line of comma-separated numbers into
# a list of integers.
def parseInput(values):
   values = values.replace(',', ' ')
   return [ int(v) for v in values.split() ]

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and the first (and only)
   # string in the list is the input.   
   fileInput = readFile("input10b.txt")
   lengths = parseInput(fileInput[0])

   # Initialize the rope, the current location,
   # and the skip size.
   string_length = 256
   skip_size = 0
   current = 0
   rope = [ i for i in range(string_length) ]

   # Iterate through each length within the input.
   for length in lengths:
      # Make sure the length is legal.
      if length <= len(rope):
         # Calculate the section of rope on which
         # to operate.
         start = current
         end = current + length - 1
         # Reverse that section of rope.
         while start < end:
            rope[start % len(rope)], rope[end % len(rope)] = rope[end % len(rope)], rope[start % len(rope)]
            start += 1
            end -= 1

         # Update the current location and skip
         # size.
         current = (current + length + skip_size) % len(rope)
         skip_size += 1

   # Display the product of the first two numbers
   # of the list. 
   print("Product = " + str(rope[0] * rope[1]))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
