import numpy as np

# Define the quantum state
state = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])

# Define the number of particles in the state
N = 2

def S_z_measure(state,N):
    Sz_values = np.arange(-N/2, N/2 + 1) # All possible states of Sz
    probabilities = np.zeros(len(Sz_values))
    for i, m in enumerate(Sz_values):
        projection = np.zeros(2**N)
        for j in range(2**N):
            if (j//(2**(N-1-m))) % 2 == 0:
                projection[j] = 1
        probabilities[i] = abs(np.dot(state, projection))**2


    probabilities /= sum(probabilities)
    random_Sz = np.random.choice(Sz_values, p=probabilities) # Pick a random value of Sz weighted by its corresponding probability
    return(probabilities,random_Sz)

probabilities=S_z_measure(state,N)[0]
random_Sz=S_z_measure(state,N)[1]
print("Probabilities of Sz:", probabilities)
print("Randomly picked value of Sz:", random_Sz)
