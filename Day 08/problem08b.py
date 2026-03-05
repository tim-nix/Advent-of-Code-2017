# The problem input is a list of instructions for
# modifying the contents of registers. Each
# instruction consists of several parts: the
# register to modify, whether to increase or
# decrease that register's value, the amount by
# which to increase or decrease it, and a
# condition. If the condition fails, skip the
# instruction without modifying the register. The
# registers all start at 0.
#
# What is the largest value in any register during
# this process?

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


# From the file input, create a list of
# instructions in which each original instruction
# (string) is broken into parts (split on
# whitespace), and each number is converted to
# an integer.
def parseInput(values):
   instructions = list()
   for line in values:
      # Split on whitespace.
      line = line.split()
      # Iterate through the parts and convert to
      # an integer if the part is a number.
      for i in range(len(line)):
         if line[i].isdigit():
            line[i] = int(line[i])
         elif line[i][0] == '-':
            line[i] = int(line[i])

      # Add the modified instruction to the list.
      instructions.append(line)

   # Return the list of instructions.
   return instructions

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to list of
   # instructions.   
   fileInput = readFile("input8b.txt")
   instructions = parseInput(fileInput)

   registers = dict()
   highest_seen = 0
   # Iterate through each instruction.
   for i in instructions:
      # If either of the involved registers are
      # not known, then add them to the collection
      # of registers.
      if i[0] not in registers:
         registers[i[0]] = 0

      if i[4] not in registers:
         registers[i[4]] = 0

      # Handle 'greater than'.
      if i[5] == '>':
         if registers[i[4]] > i[6]:
            if i[1] == 'inc':
               registers[i[0]] += i[2]
            elif i[1] == 'dec':
               registers[i[0]] -= i[2]
            
      # Handle 'greater than or equal to'.     
      elif i[5] == '>=':
         if registers[i[4]] >= i[6]:
            if i[1] == 'inc':
               registers[i[0]] += i[2]
            elif i[1] == 'dec':
               registers[i[0]] -= i[2]

      # Handle 'less than'.
      elif i[5] == '<':
         if registers[i[4]] < i[6]:
            if i[1] == 'inc':
               registers[i[0]] += i[2]
            elif i[1] == 'dec':
               registers[i[0]] -= i[2]

      # Handle 'less than or equal to'.
      elif i[5] == '<=':
         if registers[i[4]] <= i[6]:
            if i[1] == 'inc':
               registers[i[0]] += i[2]
            elif i[1] == 'dec':
               registers[i[0]] -= i[2]
               
      # Handle 'equal to'.
      elif i[5] == '==':
         if registers[i[4]] == i[6]:
            if i[1] == 'inc':
               registers[i[0]] += i[2]
            elif i[1] == 'dec':
               registers[i[0]] -= i[2]

      # Handle 'not equal to'.
      elif i[5] == '!=':
         if registers[i[4]] != i[6]:
            if i[1] == 'inc':
               registers[i[0]] += i[2]
            elif i[1] == 'dec':
               registers[i[0]] -= i[2]

      # Find the largest value in any register
      # after the execution of the current
      # instruction.
      max_register = max(registers, key=registers.get)
      if registers[max_register] > highest_seen:
         highest_seen = registers[max_register]
   
   # Display the largest value in a register. 
   print("Largest value = " + str(highest_seen))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
