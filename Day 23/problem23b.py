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
# After setting register a to 1, if the program
# were to run to completion, what value would be
# left in register h?

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


# Test to see if the number is prime. If so,
# return True. Otherwise, return False.
def isPrime(number):
   # Even numbers greater than 2 are not prime.
   if (number > 2) and (number % 2 == 0):
      return False

   # Test odd numbers for primality.
   div = 3
   while (div * div) <= number:
      if number % div == 0:
         return False
      div += 2

   # If all test are passed, number is prime.
   return True


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to integer.
   fileInput = readFile("input23b.txt")
   instructions = parseInput(fileInput)

   '''
   # Set up initial conditions.
   mul_invoked = 0
   registers = dict()
   registers['a'] = 1
   registers['b'] = 0
   registers['c'] = 0
   checkval = 0
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

      print('registers[b] = ' + str(registers['b']))
      print('registers[c] = ' + str(registers['c']))
      time.sleep(0.5)
   '''

   # Test the number of composite numbers within
   # the range of 107,900 through 124,900.
   count = 0
   start = 107900
   stop  = 124901
   step  = 17
   for num in range(start, stop, step):
      if not isPrime(num):
         count += 1
   
   # Display the number of composite numbers
   # between 107900 and 124900 (stepping by 17).
   print("Number of composites = " + str(count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))

   # Analyzing the execution of the code, it tests
   # values between 107900 (stored in register[b])
   # and 124900 (stored in register[c]) with a
   # step value of 17. Each number is tested for
   # primality and if NOT prime, register[h] is
   # incremented (decremented by -1).
        
    
        
