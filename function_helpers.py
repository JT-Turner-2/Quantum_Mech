import numpy as np
import random

def random_sz_values(psi, sz_vals):

    num_particles = int(np.log2(len(psi)))


    particle_sz = [random.choice(sz_vals) for i in range(num_particles)]

    # Return the chosen Sz value for each particle as a list
    return particle_sz
#example implementation
psi = np.array([1/2, 1/2, 0, 0, 0, 0, 1/2, -1/2])


sz_vals = np.array([-1, 0, 1])


particle_sz = random_sz_values(psi, sz_vals)

# Print the chosen Sz value for each particle
print("Particle Sz values:")
for i in range(len(particle_sz)):
    print(f"Particle {i+1}: {particle_sz[i]}")