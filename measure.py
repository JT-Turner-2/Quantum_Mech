import numpy as np
import sympy as sym


def S_z_measure(state):
    # Should return array giving state of S_z (0 for +z or 1 for -z) for each particle
    n = int(np.log2(len(state)))
    Sz_values = np.arange(-n/2, n/2 + 1) # All possible states of Sz
    probabilities = np.zeros(len(Sz_values))
    for i, m in enumerate(Sz_values):
        projection = np.zeros(2**n)
        for j in range(2**n):
            if (j//(2**(n-1-m))) % 2 == 0:
                projection[j] = 1
        probabilities[i] = abs(np.dot(state, projection))**2

    probabilities /= sum(probabilities)
    random_Sz = np.random.choice(Sz_values, p=probabilities)  # Pick a random value of Sz weighted by its corresponding probability
    return (probabilities,random_Sz)

### TESTING

# Define the quantum state in computational basis
state = np.array([1/sym.sqrt(2), 0, 0, 1/sym.sqrt(2)])

# Define the number of particles in the state
N = 2


probabilities=S_z_measure(state,N)[0]
random_Sz=S_z_measure(state,N)[1]
print("Probabilities of Sz:", probabilities)
print("Randomly picked value of Sz:", random_Sz)
