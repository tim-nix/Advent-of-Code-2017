# The problem input is a sequence of assembly
# instructions. The assembly operates on a set of
# registers that are each named with a single
# letter and that can each hold a single integer.
# Each register starts with a value of 0. The
# instruction types follow:
# - snd X plays a sound with a frequency equal to
#   the value of X.
# - set X Y sets register X to value of Y.
# - add X Y increases register X by value of Y.
# - mul X Y sets register X to the result of
#   multiplying the value contained in register X
#   by the value of Y.
# - mod X Y sets register X to the remainder of
#   dividing the value contained in register X by
#   the value of Y (that is, it sets X to the
#   result of X modulo Y).
# - rcv X recovers the frequency of the last sound
#   played, but only when the value of X is not
#   zero. (If it is zero, the command does
#   nothing.)
# - jgz X Y jumps with an offset of the value of
#   Y, but only if the value of X is greater than
#   zero.
# Many of the instructions can take either a
# register (a single letter) or a number. The
# value of a register is the integer it contains;
# the value of a number is that number. After each
# jump instruction, the program continues with the
# instruction to which the jump jumped. After any
# other instruction, the program continues with
# the next instruction. Continuing (or jumping)
# off either end of the program terminates it.
#
# What is the value of the recovered frequency
# (the value of the most recently played sound)
# the first time a rcv instruction is executed
# with a non-zero value?

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
   fileInput = readFile("input18b.txt")
   instructions = parseInput(fileInput)

   # Set up dictionary of registers and add
   # register for sound and recovery.
   registers = dict()
   registers['sound'] = 0
   registers['recover'] = 0

   # Execute assembly program.
   pc = 0
   while pc < len(instructions):
      command = instructions[pc]

      # Set instruction.
      if command[0] == 'set':
         if isinstance(command[2], int):
            registers[command[1]] = command[2]
         else:
            registers[command[1]] = registers[command[2]]

         pc += 1

      # Add instruction.
      elif command[0] == 'add':
         if command[1] not in registers:
            registers[command[1]] = 0
         if isinstance(command[2], int):
            registers[command[1]] += command[2]
         else:
            registers[command[1]] += registers[command[2]]

         pc += 1

      # Multiply instruction.
      elif command[0] == 'mul':
         if command[1] not in registers:
            registers[command[1]] = 0
         if isinstance(command[2], int):
            registers[command[1]] *= command[2]
         else:
            registers[command[1]] *= registers[command[2]]

         pc += 1

      # Modulus instruction.
      elif command[0] == 'mod':
         if command[1] not in registers:
            registers[command[1]] = 0
         if isinstance(command[2], int):
            registers[command[1]] %= command[2]
         else:
            registers[command[1]] %= registers[command[2]]
            
         pc += 1

      # Jump if greater than zero instruction.
      elif command[0] == 'jgz':
         test_val = 0
         offset = 0
         if isinstance(command[1], int):
            test_val = command[1]
         else:
            test_val = registers[command[1]]

         if isinstance(command[2], int):
            offset = command[2]
         else:
            offset = registers[command[2]]

         if test_val > 0:
            pc += offset
         else:
            pc += 1

      # Sound instruction.
      elif command[0] == 'snd':
         if isinstance(command[1], int):
            registers['sound'] = command[1]
         else:
            registers['sound'] = registers[command[1]]

         pc += 1

      # Recover instruction.
      elif command[0] == 'rcv':
         test_val = 0
         if isinstance(command[1], int):
            test_val = command[1]
         else:
            test_val = registers[command[1]]

         if test_val > 0:
            # This is the event that should
            # store then needed value and
            # terminate the assembly program.
            registers['recover'] = registers['sound']
            pc += len(instructions)
         else:
            pc += 1         
      
   # Display the value of the recovered frequency.
   print("Recovered frequency = " + str(registers['recover']))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
