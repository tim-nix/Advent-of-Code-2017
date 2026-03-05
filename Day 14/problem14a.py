# The problem input is a (partial) seed for a
# sequence of knot hashes. A total of 128 knot
# hashes are calculated, each corresponding to a
# single row in the grid; each hash contains 128
# bits which correspond to individual grid
# squares. Each bit of a hash indicates whether
# that square is free (0) or used (1). The hash
# inputs are a key string (your puzzle input), a
# dash, and a number from 0 to 127 corresponding
# to the row. The output of a knot hash is
# traditionally represented by 32 hexadecimal
# digits; each of these digits correspond to 4
# bits, for a total of 4 * 32 = 128 bits. To
# convert to bits, turn each hexadecimal digit to
# its equivalent binary value, high-bit first: 0
# becomes 0000, 1 becomes 0001, e becomes 1110, f
# becomes 1111, and so on.
#
# Given your actual key string, how many squares
# are used; that is, how many '1's are generated
# from the sequence of hashes?

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


# Convert a hexadecimal value (as an ASCII
# character) into a 4-bit string.
def hex_to_4bit(hex_char):
   return str(bin(int(hex_char, 16))[2:].zfill(4))


# Calculate the knot hash of the input string.
def calc_knothash(input_string):
   # Convert the input_string into a list of ASCII
   # values.
   lengths = parseInput(input_string)

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

   return dense_hash


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and the first (and only)
   # string in the list is the input.   
   file_input = readFile("input14b.txt")[0]
   file_input += '-'
   

   # Used to count the ones in each hash string.
   used_squares = 0

   # For each row, take the starting hash input,
   # convert it for the corresponding row, perform
   # knot hash on the resulting string, and count
   # the number of 1's
   total_rows = 128
   # Iterate for each row.
   for row in range(total_rows):
      # Calculate the knot hash.
      dense_hash = calc_knothash(file_input + str(row))

      # Convert to a binary representation.
      bin_string = ''
      for c in dense_hash:
         bin_string += hex_to_4bit(c)

      # Count the 1s in the result.
      for c in bin_string:
         if c == '1':
            used_squares += 1

   
   # Display the number of used squares on the disk. 
   print("Used squares = " + str(used_squares))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
