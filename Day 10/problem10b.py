# The problem input is a sequence of characters
# whose ASCII values correspond to lengths along a
# rope. The rope is a circle of string with 256
# marks on it. Based on the input, the function
# repeatedly selects a span of string, brings the
# ends together, and gives the span a half-twist
# to reverse the order of the marks within it.
# After doing this many times, the order of the
# marks is used to generate the answer. Begin with
# a list of numbers from 0 to 255, a current
# position which begins at 0 (the first element in
# the list), a skip size (which starts at 0), and
# a sequence of lengths (your puzzle input). Then,
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
# the list are invalid. Once you have determined
# the sequence of lengths to use, add the
# following lengths to the end of the sequence:
# 17, 31, 73, 47, 23. Second, instead of merely
# running one round like you did above, run a
# total of 64 rounds, using the same length
# sequence in each round. The current position and
# skip size should be preserved between rounds.
# Once the rounds are complete, you will be left
# with the numbers from 0 to 255 in some order,
# called the sparse hash. Your next task is to
# reduce these to a list of only 16 numbers called
# the dense hash. To do this, use numeric bitwise
# XOR to combine each consecutive block of 16
# numbers in the sparse hash (there are 16 such
# blocks in a list of 256 numbers). So, the first
# element in the dense hash is the first sixteen
# elements of the sparse hash XOR'd together, the
# second element in the dense hash is the second
# sixteen elements of the sparse hash XOR'd
# together, etc. Finally, the standard way to
# represent the hash is as a single hexadecimal
# string; the final output is the dense hash in
# hexadecimal notation. Because each number in
# your dense hash will be between 0 and 255
# (inclusive), always represent each number as
# two hexadecimal digits (including a leading
# zero as necessary).
#
# Treating your puzzle input as a string of ASCII
# characters, what is the Knot Hash of your puzzle
# input?

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


# Convert the string input into a list of the
# ASCII values for each character. 
def parseInput(values):
   return [ ord(c) for c in values ]

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and the first (and only)
   # string in the list is the input.   
   fileInput = readFile("input10b.txt")
   lengths = parseInput(fileInput[0])

   # Add the given lengths to list.
   lengths += [ 17, 31, 73, 47, 23 ]

   # Initialize the rope, the current location,
   # and the skip size.
   string_length = 256
   skip_size = 0
   current = 0
   rope = [ i for i in range(string_length) ]

   total_rounds = 64
   # Iterate through the lengths 64 total times.
   for _ in range(total_rounds):
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

   # Convert sparse hash to dense hash.
   dense_hash = ''
   index = 0

   # Iterate through 16 blocks of values.
   for i in range(16):
      hash_char = rope[index]

      # Iterate through 16 values per block.
      for j in range(1, 16):
         index += 1
         hash_char = hash_char ^ rope[index]

      # Add a leading zero, if necessary.
      char_val = hex(hash_char)[2:]
      if len(char_val) == 1:
         char_val = '0' + char_val

      # Add the characters from the round to the
      # dense hash string.
      dense_hash += char_val
      index += 1
         
   # Display the dense hash value. 
   print("Dense hash = " + str(dense_hash))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
