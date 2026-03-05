# The problem input is a list of positions,
# velocities, and accelerations for particles.
# Each particle is listed in order (starting with
# particle 0, then particle 1, particle 2, and so
# on). For each particle, it provides the X, Y,
# and Z coordinates for the particle's position
# (p), velocity (v), and acceleration (a), each in
# the format <X,Y,Z>. Each tick, all particles are
# updated simultaneously. A particle's properties
# are updated in the following order:
# - Increase the X velocity by the X acceleration.
# - Increase the Y velocity by the Y acceleration.
# - Increase the Z velocity by the Z acceleration.
# - Increase the X position by the X velocity.
# - Increase the Y position by the Y velocity.
# - Increase the Z position by the Z velocity.
# We need to know which particle will stay closest
# to position <0,0,0> in the long term. Measure
# this using the Manhattan distance, which in this
# situation is simply the sum of the absolute
# values of a particle's X, Y, and Z position.
#
# Which particle will stay closest to position
# <0,0,0> in the long term?

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
   

# Convert the file input into a list containing
# the position, velocity, and acceleration of each
# particle.
def parseInput(values):
   particles = list()

   # Iterate through each line of date.
   p_num = 0
   for line in values:
      # Remove everything but numbers and commas.
      line = line.replace('=', '')
      line = line.replace('<', '')
      line = line.replace('>', '')
      line = line.replace('p', '')
      line = line.replace('v', '')
      line = line.replace('a', '')

      # Split on the commas and convert to integer.
      parts = [ int(p) for p in line.split(',') ]

      # Build separate tuples for position,
      # velocity, and acceleration.
      p = (parts[0], parts[1], parts[2])
      v = (parts[3], parts[4], parts[5])
      a = (parts[6], parts[7], parts[8])

      # Append all three as a tuple.
      particles.append((p_num, p, v, a))
      p_num += 1

   # Return particle data.
   return particles
      

#
def distance(position):
   return abs(position[0]) + abs(position[1]) + abs(position[2])


if __name__ == '__main__':
   # Start the timer
   start_time = time.time()

   # Read the input file and convert to integer.
   fileInput = readFile("input20b.txt")
   particles = parseInput(fileInput)

   # Simulate movement of particles for 1000 ticks.
   # 1000 is chosen after some trial and error;
   # that is, it works for this data set but not
   # generally.
   for _ in range(1000):
      # Generate list of new positions and
      # velocities.
      new_particles = list()
      for num, p, v, a in particles:
         new_v = (v[0] + a[0], v[1] + a[1], v[2] + a[2])
         new_p = (p[0] + new_v[0], p[1] + new_v[1], p[2] + new_v[2])
         new_particles.append((num, new_p, new_v, a))

      # Sort the particles based on Manhattan
      # distance from (0,0,0).
      particles = sorted(new_particles, key=lambda x: distance(x[1]))

   # Display the particle number that is closest
   # to (0,0,0).
   print("Particle closest to (0,0,0) = " + str(particles[0][0]))

   # Stop the timer and print the execution time.
   print("\n\n--- %s seconds ---" % (time.time() - start_time))
        
    
        
