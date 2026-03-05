# The problem input is a sequence of assembly
# instructions. The assembly operates on a set of
# registers that are each named with a single
# letter and that can each hold a single integer.
# Each register starts with a value of 0. Two
# copies of the instructions are executed
# concurrently. Each running copy of the program
# has its own set of registers and follows the
# code independently - in fact, the programs don't
# even necessarily run at the same speed.
# The instruction types follow:
# - snd X sends the value of X to the other
#   program. These values wait in a queue until
#   that program is ready to receive them. Each
#   program has its own message queue, so a
#   program can never receive a message it sent.
# - set X Y sets register X to value of Y.
# - add X Y increases register X by value of Y.
# - mul X Y sets register X to the result of
#   multiplying the value contained in register X
#   by the value of Y.
# - mod X Y sets register X to the remainder of
#   dividing the value contained in register X by
#   the value of Y (that is, it sets X to the
#   result of X modulo Y).
# - rcv X receives the next value and stores it in
#   register X. If no values are in the queue, the
#   program waits for a value to be sent to it.
#   Programs do not continue to the next instruc-
#   tion until they have received a value. Values
#   are received in the order they are sent.
# - jgz X Y jumps with an offset of the value of
#   Y, but only if the value of X is greater than
#   zero.
# Each program also has its own program ID (one 0
# and the other 1); the register p should begin
# with this value. Many of the instructions can
# take either a register (a single letter) or a
# number. The value of a register is the integer
# it contains; the value of a number is that
# number. After each jump instruction, the program
# continues with the instruction to which the jump
# jumped. After any other instruction, the program
# continues with the next instruction. Continuing
# (or jumping) off either end of the program
# terminates it.
#
# Once both programs have terminated (regardless
# of what caused them to do so), how many times
# did program 1 send a value?

import time     # For timing the execution

# Message queues.
queue_0 = list()
queue_1 = list()
send_1 = 0

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


# This function encapsulates the interpreter of
# the assembly program. Since assembly execution
# will pause and resume based on availability of
# messages to receive, then execution location is
# passed in (and returned) as pc, and registers
# are passed in (and returned).
def assembly(program, pc, registers):
   # Tracking how many times Program 1 sends.
   global send_1

   # For deadlock detection. Changed to True if pc
   # is ever changed.
   progress = False

   # Execute assembly program instruction at
   # the location specified by pc.
   while pc < len(instructions):
      command = instructions[pc]

      # Set instruction.
      if command[0] == 'set':
         if isinstance(command[2], int):
            registers[command[1]] = command[2]
         else:
            registers[command[1]] = registers[command[2]]

         pc += 1
         progress = True

      # Add instruction.
      elif command[0] == 'add':
         if command[1] not in registers:
            registers[command[1]] = 0
            
         if isinstance(command[2], int):
            registers[command[1]] += command[2]
         else:
            registers[command[1]] += registers[command[2]]

         pc += 1
         progress = True

      # Multiply instruction.
      elif command[0] == 'mul':
         if command[1] not in registers:
            registers[command[1]] = 0
         if isinstance(command[2], int):
            registers[command[1]] *= command[2]
         else:
            registers[command[1]] *= registers[command[2]]

         pc += 1
         progress = True

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
            progress = True
         else:
            pc += 1
            progress = True

      # Send instruction.
      elif command[0] == 'snd':
         value = 0
         if isinstance(command[1], int):
            value = command[1]
         else:
            if command[1] not in registers:
               registers[command[1]] = 0
               
            value = registers[command[1]]

         # If Program 0, send to Program 1.
         if program == 0:
            queue_1.append(value)

         # If Program 1, send to Program 0.
         elif program == 1:
            queue_0.append(value)
            # This is what we are tracking.
            send_1 += 1

         pc += 1
         progress = True

      # Receive instruction.
      elif command[0] == 'rcv':
         if (program == 0) and (len(queue_0) == 0):
            return (False, pc, registers, progress)
         elif (program == 1) and (len(queue_1) == 0):
            return (False, pc, registers, progress)
         elif program == 0:
            registers[command[1]] = queue_0.pop(0)
         elif program == 1:
            registers[command[1]] = queue_1.pop(0)

         pc += 1
         progress = True

   return (True, pc, registers, True)



if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to integer.
   fileInput = readFile("input18b.txt")
   instructions = parseInput(fileInput)

   # Set up dictionary of registers, pc, and flags
   # for Program 0 and Program 1.
   registers_0 = dict()
   registers_0['p'] = 0
   registers_1 = dict()
   registers_1['p'] = 1
   pc_0 = 0
   pc_1 = 0
   done_0 = False
   done_1 = False

   # As long as both programs are not complete and
   # no deadlock is detected, keep running each.
   while (not done_0) and (not done_1):
      # Execute Program 0 until complete or wait.
      if not done_0:
         done_0, pc_0, registers_0, progress_0 = assembly(0, pc_0, registers_0)

      # Execute Program 1 until complete or wait.
      if not done_1:
         done_1, pc_1, registers_1, progress_1 = assembly(1, pc_1, registers_1)

      # Check for deadlock. If so, exit.
      if (not progress_0) and (not progress_1):
         break
      
   # Display the number of times that Program 1
   # sent a value.
   print("Times that Program 1 sent a value = " + str(send_1))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))

        
    
        
