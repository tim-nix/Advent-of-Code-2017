# The problem input is a list of potential
# passphrases. A passphrase consists of a series
# of words (lowercase letters) separated by
# spaces. To ensure security, a valid passphrase
# must contain no duplicate words.
#
# How many passphrases are valid?

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


# Convert the list of strings into a list in which
# each string is broken down into a list of
# strings split on the whitespace of the orginal.
def parseInput(values):
   string_list = list()
   for line in values:
      string_list.append(line.split())

   # Return the list of lists of strings.
   return string_list

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to integer.   
   fileInput = readFile("input4b.txt")
   passphrases = parseInput(fileInput)

   # Iterate through the list of possible
   # passphrases and count each valid one.
   count = 0
   for p in passphrases:
      if len(p) == len(set(p)):
         count += 1
      
   # Display the number of valid passphrases. 
   print("Number of valid passphrases = " + str(count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
