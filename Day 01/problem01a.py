# The problem input is a capcha in the form of a
# sequence of digits. The captcha requires you to
# review this sequence of digits and find the sum
# of all digits that match the next digit in the
# list. The list is circular, so the digit after
# the last digit is the first digit in the list.
#
# What is the solution to your captcha?

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


# Convert the file input (a string of digits) to a
# list of digits (as integers).
def parseInput(values):
   digits = list(values)
   numbers = [ int(i) for i in digits ]

   return numbers

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to a list of
   # digits.   
   fileInput = readFile("input1b.txt")
   numbers = parseInput(fileInput[0])

   # Calculate the sum of digits when the current
   # digit matches the next digit in the list.
   sum_digits = 0
   for i in range(len(numbers)):
      if numbers[i] == numbers[(i + 1) % len(numbers)]:
         sum_digits += numbers[i]
      
   # Display the resulting sum. 
   print("Sum of digits that count = " + str(sum_digits))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
