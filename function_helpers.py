import numpy as np
import sympy as sym
import random

def random_sz_values(psi, sz_vals, sz_probs=None):
    # Determine the number of particles
    num_particles = int(np.log2(len(psi)))
    sz_vals = np.array([-.5, .5])

    # If sz_probs is not specified, set it to be uniform
    if sz_probs is None:
        sz_probs = [1/len(sz_vals)] * len(sz_vals)

    # Choose a random Sz value for each particle
    particle_sz = [random.choices(sz_vals, sz_probs)[0] for i in range(num_particles)]

    # Return the chosen Sz value for each particle as a list
    return particle_sz


def measure(state):
    # Takes in a state as defined by its rep. in comp. basis
    # Gives measurement in comp basis
    probabilities = state * np.conjugate(state)
    probabilities = np.array(probabilities, dtype='float64')  # Deal with type issues with 0 object
    measured_state = np.random.choice(range(len(state)), p=probabilities)
    return measured_state


def generate_basis_state(k, n):
    # Generate kth basis state of comp basis for n particle system
    state = np.zeros(2**n)
    state[k] = 1
    return state

# TESTING
#
# psi = np.array([1/2, 1/2, 0, 0, 0, 0, 1/2, -1/2])
# print(measure(psi))


#
# # Define the possible Sz values and their probabilities
#
# sz_probs = [0.2, 0.8]
#
# # Call the random_sz_values function to get the chosen Sz values for each particle
# particle_sz = random_sz_values(psi, sz_vals, sz_probs)
#
# # Print the chosen Sz value for each particle
# print("Particle Sz values:")
# for i in range(len(particle_sz)):
#     print(f"Particle {i+1}: {particle_sz[i]}")

def run_everything (state,operator):
    n=int(np.log2(len(state)))
    for i in range(n):
        state=operator(state,i)
    return state
def find_num_particles(psi):
    n=int(np.log2(psi))
    return n
