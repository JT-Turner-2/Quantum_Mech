import numpy as np
import random

def random_sz_values(psi, sz_vals, sz_probs=None):
    # Determine the number of particles
    num_particles = int(np.log2(len(psi)))

    # If sz_probs is not specified, set it to be uniform
    if sz_probs is None:
        sz_probs = [1/len(sz_vals)] * len(sz_vals)

    # Choose a random Sz value for each particle
    particle_sz = [random.choices(sz_vals, sz_probs)[0] for i in range(num_particles)]

    # Return the chosen Sz value for each particle as a list
    return particle_sz

#example
psi = np.array([1/2, 1/2, 0, 0, 0, 0, 1/2, -1/2])

# Define the possible Sz values and their probabilities
sz_vals = np.array([-1, 0, 1])
sz_probs = [0.2, 0.6, 0.2]

# Call the random_sz_values function to get the chosen Sz values for each particle
particle_sz = random_sz_values(psi, sz_vals, sz_probs)

# Print the chosen Sz value for each particle
print("Particle Sz values:")
for i in range(len(particle_sz)):
    print(f"Particle {i+1}: {particle_sz[i]}")