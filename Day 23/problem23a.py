# The problem input is an assembly program. The
# code consists of the following instructions:
# - set X Y sets register X to the value of Y.
# - sub X Y decreases register X by the value of
#   Y.
# - mul X Y sets register X to the result of
#   multiplying the value contained in register X
#   by the value of Y.
# - jnz X Y jumps with an offset of the value of
#   Y, but only if the value of X is not zero. (An
#   offset of 2 skips the next instruction, an
#   offset of -1 jumps to the previous
#   instruction, and so on.)
# Only the instructions listed above are used. The
# eight registers here, named a through h, all
# start at 0.
#
# If you run the program, how many times is the
# 'mul' instruction invoked?

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
   

# Convert the file input (string representation of
# the instructions into a list of tuples with each
# tuple representing an instruction.
def parseInput(values):
   instructions = list()

   # Iterate through each line of text.
   for line in values:
      # Split text into parts based on whitespace.
      parts = line.split()

      # Check for integer for first operand and,
      # if so, convert it.
      if parts[1].isdigit() or parts[1][0] == '-':
         parts[1] = int(parts[1])

      # Check for integer for second operand and,
      # if so, convert it.
      if (len(parts) > 2) and (parts[2].isdigit() or parts[2][0] == '-'):
         parts[2] = int(parts[2])

      # Convert instruction to tuple and add it to
      # the list.
      instructions.append(tuple(parts))

   # Return instructions.
   return instructions


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to integer.
   fileInput = readFile("input23b.txt")
   instructions = parseInput(fileInput)

   # Set up initial conditions.
   mul_invoked = 0
   registers = dict()
   pc = 0

   # Execute the program.
   while pc < len(instructions):
      command = instructions[pc]

      # Handle the set command.
      if command[0] == 'set':
         if isinstance(command[2], int):
            registers[command[1]] = command[2]
         else:
            registers[command[1]] = registers[command[2]]

         pc += 1

      # Handle the subtract command.
      elif command[0] == 'sub':
         if command[1] not in registers:
            registers[command[1]] = 0
         if isinstance(command[2], int):
            registers[command[1]] -= command[2]
         else:
            if command[2] not in registers:
               registers[command[2]] = 0
            registers[command[1]] -= registers[command[2]]

         pc += 1

      # Handle the multiply command.
      elif command[0] == 'mul':
         if command[1] not in registers:
            registers[command[1]] = 0
         if isinstance(command[2], int):
            registers[command[1]] *= command[2]
         else:
            if command[2] not in registers:
               registers[command[2]] = 0
            registers[command[1]] *= registers[command[2]]

         # The 'mul' command was invoked. 
         mul_invoked += 1
         pc += 1

      # Handle the jump not zero command.
      elif command[0] == 'jnz':
         test_val = 0
         offset = 0
         if isinstance(command[1], int):
            test_val = command[1]
         else:
            if command[1] not in registers:
               registers[command[1]] = 0
            test_val = registers[command[1]]

         if isinstance(command[2], int):
            offset = command[2]
         else:
            if command[2] not in registers:
               registers[command[2]] = 0
            offset = registers[command[2]]

         if test_val != 0:
            pc += offset
         else:
            pc += 1
   
   # Display the number of times that the command
   # 'mul' was invoked.
   print("Command mul invoked = " + str(mul_invoked))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
