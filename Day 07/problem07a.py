# The problem input is a list of program names,
# their weight, and (if they're holding a disc)
# the names of the programs immediately above them
# balancing on that disc. A recursive algorithm
# has gotten out of hand, and now the programs are
# balanced precariously in a large tower. One
# program at the bottom supports the entire tower.
# It's holding a large disc, and on the disc are
# balanced several more sub-towers. At the bottom
# of these sub-towers, standing on the bottom
# disc, are other programs, each holding their own
# disc, and so on. At the very tops of these
# sub-sub-sub-...-towers, many programs stand
# simply keeping the disc below them balanced but
# with no disc of their own.
#
# What is the name of the bottom program?

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


# This function generates two sets. The set of
# programs contains all programs listed alone or
# on the left side of the '->' string. The set of
# programs with a known lower level ('uppers') are
# all programs listed on the right side of the
# '->' string.
def parseInput(values):
   programs = set()
   uppers = set()
   # Iterate through each line of text.
   for line in values:
      # If the line contains the '->' string, then
      # add the left program to 'programs' and all
      # programs of the right side to 'uppers'.
      if '->' in line:
         line = line.replace(',', '')
         parts = line.split()
         programs.add(parts[0])
         for p in parts[3:]:
            uppers.add(p)
      # Otherwise, just add the program name to
      # 'programs'.
      else:
         parts = line.split()
         programs.add(parts[0])

   # Return the two sets.
   return (programs, uppers)
      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to list of
   # integers.   
   fileInput = readFile("input7b.txt")
   programs, uppers = parseInput(fileInput)

   # The difference between all programs and upper
   # programs is the base program.
   difference = list(programs.difference(uppers))
      
   # Display the program at the base of the
   # recursive tower. 
   print("Base of tower = " + str(difference[0]))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
