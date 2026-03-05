# The problem input consists of a 2d array of
# numbers from a spreadsheet. Calculate the
# spreadsheet's checksum. For each row, determine
# the difference between the largest value and the
# smallest value; the checksum is the sum of all
# of these differences.
#
# What is the checksum for the spreadsheet in your
# puzzle input?

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


# Convert the file input (a list of strings with
# each string as a row of numbers) to a list of
# lists of integers.
def parseInput(values):
   numbers = list()
   for v in values:
      # Split the row into separate numbers.
      v = v.split()
      
      # Convert to a list of integers and add to
      # the list.
      numbers.append([ int(a) for a in v ])

   # Return the numbers.
   return numbers

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to a list of
   # digits.   
   fileInput = readFile("input2b.txt")
   numbers = parseInput(fileInput)

   # Iterate through each row of numbers.
   checksum = 0
   for row in numbers:
      # Find the minimum and maximum for each row.
      min_val = min(row)
      max_val = max(row)

      # Add the difference to the checksum.
      checksum += (max_val - min_val)
      
   # Display the resulting checksum. 
   print("Checksum = " + str(checksum))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
