# The problem input consists of a list of number
# pairs in which the first number is the layer of
# the firewall and the second number is the range
# of the scanner that moves back and forth across
# the layer. Your plan is to hitch a ride on a
# packet about to move through the firewall. The
# packet will travel along the top of each layer,
# and it moves at one layer per picosecond. Each
# picosecond, the packet moves one layer forward
# (its first move takes it into layer 0), and then
# the scanners move one step. If there is a
# scanner at the top of the layer as your packet
# enters it, you are caught. (If a scanner moves
# into the top of its layer while you are there,
# you are not caught: it doesn't have time to
# notice you before you leave.) You can't control
# the speed of the packet, but you can delay it
# any number of picoseconds. For each picosecond
# you delay the packet before beginning your trip,
# all security scanners move one step. You're not
# in the firewall during this time; you don't
# enter layer 0 until you stop delaying the
# packet.
#
# What is the fewest number of picoseconds that
# you need to delay the packet to pass through the
# firewall without being caught?

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


# Convert the file input into a list of tuples
# with integer values.
def parseInput(values):
   layers = list()
   for line in values:
      parts = line.split(':')
      layers.append((int(parts[0]), int(parts[1])))

   return layers

      
if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert it into a
   # list of ranges for each scanning layer.
   fileInput = readFile("input13b.txt")
   layers = parseInput(fileInput)


   # Increasingly delay the start time until a
   # path is found.
   delay = 0
   found = False
   while not found:
      found = True
      # Iterate through the layers.
      for location, scan_range in layers:
         # Calculate the period of the scanner.
         period = 2 * (scan_range - 1)
         # Determine if the scanner is at location 0
         # when the packet is at the given layer.
         if ((delay + location) % period) == 0:
            # If so, then not a safe path.
            found = False
            break

      # If safe path was not found, then delay by
      # one more picosecond.
      if not found:
         delay += 1

   # Display the fewest number of picoseconds that
   # you need to delay.
   print("Delay time = " + str(delay))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
