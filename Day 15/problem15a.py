# The problem input are starting values (seeds)
# for two generators (A and B). The generators
# both work on the same principle. To create its
# next value, a generator will take the previous
# value it produced, multiply it by a factor
# (generator A uses 16807; generator B uses
# 48271), and then keep the remainder of dividing
# that resulting product by 2147483647. That final
# remainder is the value it produces next. To get
# a significant sample, the judge would like to
# consider 40 million pairs.
#
# After 40 million pairs, what is the judge's
# final count?

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
   divisor = 2147483647
   total_pairs = 40000000

   # Generate the specified number of pairs and
   # count the number of times that the lower 16
   # bits match.
   count = 0
   for _ in range(total_pairs):
      # Generate the next pair.
      next_A = (next_A * factor_A) % divisor
      next_B = (next_B * factor_B) % divisor

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
        
    
        
