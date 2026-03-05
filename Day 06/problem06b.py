# The problem input is a string of numbers with
# each number representing the number of blocks
# stored in a given memory bank. The goal of the
# reallocation routine is to balance the blocks
# between the memory banks. The reallocation
# routine operates in cycles. In each cycle, it
# finds the memory bank with the most blocks (ties
# won by the lowest-numbered memory bank) and
# redistributes those blocks among the banks. To
# do this, it removes all of the blocks from the
# selected bank, then moves to the next (by index)
# memory bank and inserts one of the blocks. It
# continues doing this until it runs out of
# blocks; if it reaches the last memory bank, it
# wraps around to the first one.
#
# Given the initial block counts in your puzzle
# input, how many cycles are in the infinite loop
# that arises?

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


# Take the string of numbers, split it up into
# separate numbers, and convert to a list of
# integers.
def parseInput(values):
   return [ int(v) for v in values.split() ]

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to list of
   # integers.   
   fileInput = readFile("input6b.txt")
   memory = parseInput(fileInput[0])

   # Continue to redistribute memory until a state
   # occurs that has been seen before. We not only
   # store memory states seen, but also the number
   # of cycles that occurred to see the state.
   seen_states = set()
   seen_states.add(tuple(memory))
   occurrence = dict()
   occurrence[tuple(memory)] = 0
   cycles = 0
   done = False
   while not done:
      # Increment the number of cycles.
      cycles += 1
      
      # Choose and clear largest memory location.
      largest = max(memory)
      index = memory.index(largest)
      memory[index] = 0

      # Distribute data across memory.
      while largest > 0:
         index = (index + 1) % len(memory)
         memory[index] += 1
         largest -= 1

      # Check to see if the current state of
      # memory has been seen before.
      current = tuple(memory)
      # If so, then done.
      if current in seen_states:
         done = True
      # Otherwise, add current memory state to set
      # and the number of cycles to reach the
      # state to the dictionary.
      else:
         seen_states.add(current)
         occurrence[current] = cycles
      
   # Display the size of the loop needed to repeat
   # the memory state.
   print("Size of loop = " + str(cycles - occurrence[current]))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
