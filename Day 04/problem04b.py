# The problem input is a list of potential
# passphrases. A passphrase consists of a series
# of words (lowercase letters) separated by
# spaces. To ensure security, a valid passphrase
# must contain no duplicate words. For added
# security, yet another system policy has been put
# in place. Now, a valid passphrase must contain
# no two words that are anagrams of each other -
# that is, a passphrase is invalid if any word's
# letters can be rearranged to form any other
# word in the passphrase.
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

   
   count = 0
   # Iterate through each passphrase.
   for p in passphrases:
      # Compare each string in the passphrase with
      # every other string in the passphrase.
      # Initially assume the passphrase is valid.
      valid = True
      for i in range(len(p)-1):
         for j in range(i+1, len(p)):
            # If both strings contain the same
            # number of characters and the same
            # number of unique characters, then
            # continue to check for invalid.
            if (len(p[i]) == len(p[j])) and (len(set(p[i])) == len(set(p[j]))):
               letters = set(p[i])
               letter_check = list()
               # If the count of unique letters is
               # the same in both, then invalid.
               for key in letters:
                  letter_check.append(list(p[i]).count(key) == list(p[j]).count(key))
               valid = not all(letter_check)

               # If invalid, no need to check this
               # passphrase further.
               if not valid:
                  break

         # If invalid, no need to check this
         # passphrase further.
         if not valid:
            break

      # If still valid, increment the count.
      if valid:
         count += 1
                        
      
   # Display the number of valid passphrases. 
   print("Number of valid passphrases = " + str(count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
