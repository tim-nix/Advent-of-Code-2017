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
# Count all of the characters within the garbage.
# The leading and trailing < and > don't count,
# nor do any canceled characters or the ! doing
# the canceling.

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

   garbage = False
   ignore = False
   char_count = 0
   # Iterate through the characters in the stream.
   for char in groups:
      # If the character is not contained within
      # garbage, then process it (or skip it).
      if not garbage:
         # Start of garbage.
         if char == '<':
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

      # Otherwise, character is garbage so
      # increment count.
      else:
         char_count += 1
         
   
   # Display the total character count of garbage
   # excluding '<' and '>'. 
   print("Garbage count = " + str(char_count))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
