import numpy as np
import sympy as sym

# Define the Pauli matrices
sigma_x = np.array([[0, 1], [1, 0]])
sigma_y = np.array([[0, -1j], [1j, 0]])
sigma_z = np.array([[1, 0], [0, -1]])

# Define the ladder operators
def Splus(j, n):
    """
    Returns the ladder operator S+ acting on the jth particle in a state of n particles.
    """
    op_list = [np.eye(2)] * n
    op_list[j] = sigma_x
    return np.kron(op_list[0], np.kron(op_list[1], op_list[2:]))

def Sminus(j, n):
    """
    Returns the ladder operator S- acting on the jth particle in a state of n particles.
    """
    op_list = [np.eye(2)] * n
    op_list[j] = sigma_x
    return np.kron(op_list[0], np.kron(op_list[1], op_list[2:]))

# Define the Sz operator
def Sz(n):
    """
    Returns the operator for the total spin along the z-axis of n spin-1/2 particles.
    """
    op_list = [sigma_z] * n
    return np.sum(np.kron(op_list[0], np.kron(op_list[1], op_list[2:])))

# Define a function to calculate the probabilities of Sz
import numpy as np

# Define the Pauli matrices
sigma_x = np.array([[0, 1], [1, 0]])
sigma_y = np.array([[0, -1j], [1j, 0]])
sigma_z = np.array([[1, 0], [0, -1]])

# Define the ladder operators
def Splus(j, n):
    """
    Returns the ladder operator S+ acting on the jth particle in a state of n particles.
    """
    op_list = [np.eye(2)] * n
    op_list[j] = sigma_x
    return np.kron(op_list[0], np.kron(op_list[1], op_list[2:]))

def Sminus(j, n):
    """
    Returns the ladder operator S- acting on the jth particle in a state of n particles.
    """
    op_list = [np.eye(2)] * n
    op_list[j] = sigma_x
    return np.kron(op_list[0], np.kron(op_list[1], op_list[2:]))

# Define the Sz operator
def Sz(n):
    """
    Returns the operator for the total spin along the z-axis of n spin-1/2 particles.
    """
    op_list = []
    for i in range(n):
        op = np.eye(2)
        for j in range(i):
            op = np.kron(op, np.eye(2))
        op = np.kron(op, sigma_z)
        for j in range(i+1, n):
            op = np.kron(op, np.eye(2))
        op_list.append(op)
    return np.zeros((2**n, 2**n))

# Define a function to calculate the probabilities of Sz
def probabilities_Sz(state, n):
    """
    Calculates the probabilities of obtaining each eigenvalue of Sz given a quantum state of n particles.
    """
    # Calculate the eigenvalues and eigenvectors of Sz
    eigenvalues, eigenvectors = np.linalg.eigh(Sz(n))

    # Project the state onto each eigenstate of Sz and calculate the probabilities
    probabilities = []
    for i in range(len(eigenvalues)):
        eigenvector = eigenvectors[:, i]
        projection = np.dot(np.conj(np.transpose(eigenvector)), state)
        probability = np.abs(projection)**2
        probabilities.append(probability)

    return probabilities


# Example usage
n = 3
state = np.array([1, 0, 0, 0, 0, 0, 0, 0]) / np.sqrt(2)
probabilities = probabilities_Sz(state, n)
print(probabilities)
def measure(probablities):
    result=np.random.choice(1,0, p=[probabilities_Sz(state, n)])
#measure the state of eigenstate of Sz of all particles. Return 0,1 where 0 is pluz z and 1 is minus z
# weighted probability
    return result

# Example usage
n = 3
state = np.array([1, 0, 0, 0, 0, 0, 0, 0]) / np.sqrt(2)
probabilities = probabilities_Sz(state, n)
print(probabilities)
yeet=measure(probabilities)
print(yeet)
