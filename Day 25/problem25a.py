# The problem input is a list of instructions for
# a Turing machine. Its parts consist of:
# - A tape which contains 0 repeated infinitely to
#   the left and right.
# - A cursor, which can move left or right along
#   the tape and read or write values at its
#   current position.
# - A set of states, each containing rules about
#   what to do based on the current value under
#   the cursor.
# Each slot on the tape has two possible values: 0
# (the starting value for all slots) and 1. Based
# on whether the cursor is pointing at a 0 or a 1,
# the current state says what value to write at
# the current position of the cursor, whether to
# move the cursor left or right one slot, and
# which state to use next. The CPU can confirm
# that the Turing machine is working by taking a
# diagnostic checksum after a specific number of
# steps (given in the blueprint). Once the
# specified number of steps have been executed,
# the Turing machine should pause; once it does,
# count the number of times 1 appears on the tape.
#
# Recreate the Turing machine. What is the
# diagnostic checksum it produces once it's
# working again?

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
   

# Convert the file input instructions into a
# dictionary of tuples, with the key being the
# start and the value being a tuple containing the
# instructions for what to do in the given state.
# Also, extract the starting state (on the first
# line) and the number of steps to take (on the
# second line).
def parseInput(values):
   instructions = dict()

   # Extract start state and the number of steps.
   start = values[0][15]
   parts = values[1].split()
   steps = int(parts[5])

   # Parse each state.
   i = 3
   while i < len(values):
      # Extract the state
      state = values[i+0][9]

      # Extract actions on tape = 0.
      write_0 = int(values[i+2][22])
      parts = values[i+3].split()
      move_0 = parts[-1][:-1]
      next_0 = values[i+4][26]

      # Extract actions on tape = 1.
      write_1 = int(values[i+6][22])
      parts = values[i+7].split()
      move_1 = parts[-1][:-1]
      next_1 = values[i+8][26]

      # Add value for key state.
      instructions[state] = (write_0, move_0, next_0, write_1, move_1, next_1)

      # Move to next state.
      i += 10

   # Return start state, number of steps, and
   # instructions that occur for each state.
   return (start, steps, instructions)


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to integer.
   fileInput = readFile("input25b.txt")
   state, steps, instructions = parseInput(fileInput)

   # Initialize the tape and tape head location.
   tape = dict()
   position = 0

   # Iterate for the given number of steps.
   for _ in range(steps):
      # If the given position on the tape is not
      # defined, then set it to 0.
      if position not in tape:
         tape[position] = 0

      # If current tape location is 0...
      if tape[position] == 0:
         # Assign the tape location to value.
         tape[position] = instructions[state][0]

         # Move the tape head
         if instructions[state][1] == 'right':
            position += 1
         else:
            position -= 1

         # Update the state.
         state = instructions[state][2]

      # If current tape location is 1...
      else:
         # Assign the tape location to value.
         tape[position] = instructions[state][3]

         # Move the tape head
         if instructions[state][4] == 'right':
            position += 1
         else:
            position -= 1

         # Update the state.
         state = instructions[state][5]

   # Calculate the checksum
   checksum = 0
   for key in tape:
      checksum += tape[key]
      
   # Display the diagnostic checksum.
   print("Diagnostic checksum = " + str(checksum))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
