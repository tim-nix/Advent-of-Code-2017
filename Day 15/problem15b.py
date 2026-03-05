# The problem input are starting values (seeds)
# for two generators (A and B). The generators
# both work on the same principle. To create its
# next value, a generator will take the previous
# value it produced, multiply it by a factor
# (generator A uses 16807; generator B uses
# 48271), and then keep the remainder of dividing
# that resulting product by 2147483647. That final
# remainder is the value it produces next. Now,
# each generator only hands a value to the judge
# when it meets their criteria:
# - Generator A looks for values that are
#   multiples of 4.
# - Generator B looks for values that are
#   multiples of 8.
# Each generator functions independently: going
# through values entirely on their own, and
# handing the next found acceptable value to the
# judge, or otherwise working through the same
# sequence of values as before until they find
# one. The judge still waits for each generator to
# provide it with a value before comparing them
# (using the same comparison method as before).
# It keeps track of the order it receives values;
# the first values from each generator are
# compared, then the second values from each
# generator, then the third values, and so on.
# This change makes the generators much slower,
# and the judge is now only willing to consider 5
# million pairs.
#
# After 5 million pairs, but using this new
# generator logic, what is the judge's final
# count?

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


# From the file input, extract the starting values
# for Generator A and Generator B.
def parseInput(values):
   start_A = int(values[0].split()[-1])
   start_B = int(values[1].split()[-1])

   return (start_A, start_B)
      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it into the
   # starting values for the two generators.
   fileInput = readFile("input15b.txt")
   next_A, next_B = parseInput(fileInput)

   # Define the provided constants
   factor_A = 16807
   factor_B = 48271
   multiple_A = 4
   multiple_B = 8
   divisor = 2147483647
   total_pairs = 5000000

   # Generate sufficient number of pairs that are
   # appropriately divisible and count the number
   # of times that the lower 16 bits match.
   count = 0
   sufficient = 0
   found_A = False
   found_B = False
   while sufficient < total_pairs:
      # Generate the next pair independently.
      
      # If the next value for A is not found, then
      # generate a new one.
      if not found_A:
         next_A = (next_A * factor_A) % divisor

      # If the next value for B is not found, then
      # generate a new one.
      if not found_B:
         next_B = (next_B * factor_B) % divisor

      # Test if the next value of A is good.
      if ((next_A % multiple_A) == 0):
         found_A = True

      # Test if the next value of B is good.
      if ((next_B % multiple_B) == 0):
         found_B = True

      # Once two good values are found, compare
      # the lowest 16 bits for a match.
      if found_A and found_B:
         found_A = found_B = False
         sufficient += 1
            
         # Extract the lower 16 bits.
         binary_A = format(next_A & 0xFFFF, '016b')
         binary_B = format(next_B & 0xFFFF, '016b')

         # If they match, increment the count.
         if binary_A == binary_B:
            count += 1
   
   # Display the final count of matching pairs.
   print("Judge's final count = " + str(count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
   
