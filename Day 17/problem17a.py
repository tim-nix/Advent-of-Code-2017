# The problem input is an integer value denoting
# the number of steps taken before inserting the
# next value. The spin lock starts with a circular
# buffer containing only the value 0, which it
# marks as the current position. It then steps
# forward through the circular buffer some number
# of steps (the problem input) before inserting
# the first new value, 1, after the value it
# stopped on. The inserted value becomes the
# current position. Then, it steps forward from
# there the same number of steps, and wherever it
# stops, inserts after it the second new value, 2,
# and uses that as the new current position again.
# It repeats this process of stepping forward,
# inserting a new value, and using the location of
# the inserted value as the new current position a
# total of 2017 times, inserting 2017 as its final
# operation, and ending with a total of 2018
# values (including 0) in the circular buffer.
#
# What is the value after 2017 in your completed
# circular buffer?

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

   # Read the input file and convert to integer.
   fileInput = readFile("input17b.txt")
   num_steps = int(fileInput[0])

   # Set up the initial conditions.
   spinlock = [ 0 ]
   spin_times = 2017
   current = 0
   count = 0

   # Iterate the specified number of times.
   for _ in range(spin_times):
      # Increment the insert value.
      count += 1

      # Calculate the insert location.
      current = ((current + num_steps) % len(spinlock)) + 1

      # Insert the value in the spinlock
      spinlock.insert(current, count)
   
   # Display the value after the last value
   # inserted in the spinlock (2017).
   print("Value after last added = " + str(spinlock[current + 1]))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
