# The problem input is a data stream of
# characters. The characters represent groups;
# sequences that begin with { and end with }.
# Within a group, there are zero or more other
# things, separated by commas: either another
# group or garbage. Since groups can contain
# other groups, a } only closes the most-recently-
# opened unclosed group - that is, they are
# nestable. Your puzzle input represents a single,
# large group which itself contains many smaller
# ones. Sometimes, instead of a group, you will
# find garbage. Garbage begins with < and ends
# with >. Between those angle brackets, almost any
# character can appear, including { and }. Within
# garbage, < has no special meaning. In a futile
# attempt to clean up the garbage, some program
# has canceled some of the characters within it
# using !: inside garbage, any character that
# comes after ! should be ignored, including <, >,
# and even another !. Outside garbage, you only
# find well-formed groups, and garbage always
# terminates according to the rules above.
#
# Your goal is to find the total score for all
# groups in your input. Each group is assigned a
# score which is one more than the score of the
# group that immediately contains it. (The
# outermost group gets a score of 1.)

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

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and the first (and only)
   # string in the list is the input.   
   fileInput = readFile("input9b.txt")
   groups = fileInput[0]

   total_score = 0
   garbage = False
   ignore = False
   open_groups = 0
   # Iterate through the characters in the stream.
   for char in groups:
      # If the character is not contained within
      # garbage, then process it.
      if not garbage:
         # Start of a new group.
         if char == '{':
            open_groups += 1

         # End of a group.
         elif (open_groups > 0) and (char == '}'):
            total_score += open_groups
            open_groups -= 1

         # Start of garbage.
         elif char == '<':
            garbage = True

      # Otherwise, if not in an ignore state, '!'
      # means ignore the next character.
      elif (not ignore) and (char == '!'):
         ignore = True

      # Otherwise, if in an ignore state, ignore
      # the current character and end ignore state.
      elif ignore:
         ignore = False

      # Otherwise, '>' means end garbage state.
      elif char == '>':
         garbage = False
         
   
   # Display the total score of all groups. 
   print("Total score = " + str(total_score))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
