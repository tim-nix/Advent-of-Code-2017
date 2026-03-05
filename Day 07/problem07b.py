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
# Given that exactly one program is the wrong
# weight, what would its weight need to be to
# balance the entire tower?

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


# From the input file data, convert to a list of
# program names, mapping of programs that are
# called by other programs (uppers), mapping of
# programs to the programs they call (mapping),
# and the weight carried by each program.
def parseInput(values):
   programs = set()
   uppers = set()
   mappings = dict()
   weights = dict()
   # Iterate through each line of text.
   for line in values:
      # If the line contains the '->' string, then
      # add the corresponding parts to the correct
      # sets and dictionaries.
      if '->' in line:
         line = line.replace(',', '')
         parts = line.split()

         # Add the left element as a program name.
         programs.add(parts[0])

         # Add the weight of the left element.
         weights[parts[0]] = int(parts[1][1:-1])

         # Add the right program names as 'uppers'
         # and map the left element to all right
         # program names.
         mappings[parts[0]] = list()
         for p in parts[3:]:
            uppers.add(p)
            mappings[parts[0]].append(p)
            
      # Otherwise, just add the program name to
      # 'programs' and the weight to 'weights'.
      else:
         parts = line.split()
         programs.add(parts[0])
         weights[parts[0]] = int(parts[1][1:-1])

   # Return the two sets.
   return (programs, uppers, mappings, weights)



# From the 'current' program, recurse to calculate
# the weight of each sub-tower. If an imbalance is
# found, print out the correction.
def recurseWeight(current, mappings, weights):
   # If a leaf node, return the program weight.
   if current not in mappings:
      return weights[current]

   # Otherwise, recurse on each sub-program,
   # calculate the weight, and determine if an
   # imbalance exists.
   else:
      # Find the weight of each sub-tower.
      total_weights = list()
      for tower in mappings[current]:
         total_weights.append(recurseWeight(tower, mappings, weights))

      # If tower weights are different, then an
      # imbalance exits.
      if len(set(total_weights)) > 1:
         # Find index of minority total_weights.
         # Assumption is that all weights will be
         # the same except for the minority weight.
         minority_index = None
         majority_weight = 0
         for w in total_weights:
            if total_weights.count(w) == 1:
               minority_index = total_weights.index(w)
            else:
               majority_weight = w

         # Identify the problem program and the
         # needed weight to balance the tower.
         problem_program = mappings[current][minority_index]
         delta_weight = majority_weight - total_weights[minority_index]
         new_weight = weights[problem_program] + delta_weight

         # Display the problem program and the
         # corrected weight.
         print('problem program = ' + problem_program)
         print('weight correction = ' + str(new_weight))

         # Return the corrected weight (seems
         # simpler than trying to break out of the
         # recursion.
         return weights[current] + len(mappings[current]) * majority_weight

      # Otherwise, all is balanced, so return the
      # total weight.
      else:
         return weights[current] + sum(total_weights)


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to needed
   # data structures.
   fileInput = readFile("input7b.txt")
   programs, uppers, mappings, weights = parseInput(fileInput)

   # The difference between all programs and upper
   # programs is the base program.
   base = list(programs.difference(uppers))[0]

   # Starting with the base program, recurse to
   # calculate the weight of each tower, looking
   # for the imbalance.
   recurseWeight(base, mappings, weights)

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
