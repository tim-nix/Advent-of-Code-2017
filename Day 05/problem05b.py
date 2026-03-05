# The problem input is a list of integer values
# in which each denote an offset for each jump
# within a program execution. Jumps are relative:
# -1 moves to the previous instruction, and 2
# skips the next one. Start at the first
# instruction in the list. The goal is to follow
# the jumps until one leads outside the list. In
# addition, these instructions are a little
# strange; after each jump, if the offset was
# three or more, decrease it by 1. Otherwise,
# increase it by 1.
#
# Given the list of jump offsets, how many steps
# does it take to reach the exit?

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


# Convert the list of numbers (as strings) to a
# list of integers.
def parseInput(values):
   return [ int(v) for v in values ]

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to list of
   # integers.   
   fileInput = readFile("input5b.txt")
   offsets = parseInput(fileInput)

   # Iterate through offsets, updating the value
   # of the instruction pointer (ip) until the
   # program exits (ip is greater than the number
   # of instructions.
   steps = 0
   ip = 0
   while ip < len(offsets):
      # Calculate the next ip value.
      next_ip = ip + offsets[ip]

      # If the offset was three or more, decrease
      # it by 1. 
      if offsets[ip] >= 3:
         offsets[ip] -= 1
      # Otherwise, increase it by 1.
      else:
         offsets[ip] += 1

      # Update the ip.
      ip = next_ip

      # Increment the number of steps taken.
      steps += 1
   
   # Display the number of steps needed to exit. 
   print("Number of steps = " + str(steps))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
