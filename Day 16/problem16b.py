# The problem input is a string containing a
# sequence of program dance moves. There are
# sixteen programs in total, named a through p.
# They start by standing in a line: a stands in
# position 0, b stands in position 1, and so on
# until p, which stands in position 15. The
# programs' dance consists of a sequence of dance
# moves:
# - Spin, written sX, makes X programs move from
#   the end to the front, but maintain their order
#   otherwise. (For example, s3 on abcde produces
#   cdeab).
# - Exchange, written xA/B, makes the programs at
#   positions A and B swap places.
# - Partner, written pA/B, makes the programs
#   named A and B swap places.
# Keeping the positions they ended up in from
# their previous dance, the programs perform it
# again and again: including the first dance, a
# total of one billion (1000000000) times.
#
# In what order are the programs standing after
# their billion dances?

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


# Convert the file input (string) into a list of
# tuples with each tuple corresponding to a single
# dance move.
def parseInput(values):
   moves = list()

   # Dance moves are originally comma-delimited.
   parts = values.split(',')

   # Iterate through the dance moves and convert,
   # adding each to the list of moves.
   for p in parts:
      # If move is a 'spin', then first character
      # is 's' and rest is an integer.
      if p[0] == 's':
         moves.append(('s', int(p[1:])))

      # If move is an 'exchange', then first
      # character is an 'x' and the rest are two
      # integers separated by a '/'.
      elif p[0] == 'x':
         parts = p[1:].split('/')
         moves.append(('x', int(parts[0]), int(parts[1])))

      # If move is 'partner', then first character
      # is a 'p' and the second and fourth
      # characters are the programs to swap.
      elif p[0] == 'p':
         moves.append(('p', p[1], p[3]))

   # Return the list of moves.
   return moves


# This function performs the sequence of dance
# moves a single time. It takes a starting
# position of programs, performs the dance
# sequence, and returns the resulting position of
# programs.
def performDance(programs):
   # Iterate through all moves.
   for move in moves:
      # Handle spin.
      if move[0] == 's':
         cut_i = num_programs - move[1]
         programs = programs[cut_i:] + programs[:cut_i]

      # Handle exchange.
      elif move[0] == 'x':
         programs[move[1]], programs[move[2]] = programs[move[2]], programs[move[1]]

      # Handle partner.
      elif move[0] == 'p':
         first = programs.index(move[1])
         second = programs.index(move[2])
         programs[first], programs[second] = programs[second], programs[first]

   return programs


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it into the
   # starting values for the two generators.
   fileInput = readFile("input16b.txt")
   moves = parseInput(fileInput[0])

   # Initialize the list of programs twice (one to
   # perform the dance and one as a reference).
   num_programs = 16
   programs = [ chr(c) for c in range(ord('a'), ord('a') + num_programs) ]
   check = [ chr(c) for c in range(ord('a'), ord('a') + num_programs) ]

   # Complete the sequence of moves this many
   # times.
   max_dances = 1000000000

   # Find the number of times of performing the
   # dance sequence until the programs return to
   # their original sequence.
   done = False
   loop = 0
   while not done:
      # Increment the loop count.
      loop += 1

      # Perform the sequence of moves.
      programs = performDance(programs)

      # If the program positions match the
      # starting positions, then end loop.
      if programs == check:
         done = True

   # Calculate the remainder sequences that need
   # to be performed.
   residue = max_dances % loop

   # Perform the remainder sequences.
   for _ in range(residue):
      programs = performDance(programs)
      
   # Display the resulting program order after all
   # dance moves are performed.
   print("Resulting program order = " + ''.join(programs))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
