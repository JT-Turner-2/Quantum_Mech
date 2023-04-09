# File defining basic operations that act on states (2n element np array for n particles)
# Each operation should take in the initial state and an identifier of which particles to act on and return the end state
import numpy as np
import sympy as sym
# Using sympy for sqrt 2 to be exact -- may need to change this, but hopefully will work

# Defining Pauli spin mats
SIGMA_1 = np.array([[complex(0), complex(1, 0)], [complex(1, 0), complex(0)]])
SIGMA_2 = np.array([[complex(0), complex(0, -1)], [complex(0, 1), complex(0)]])
SIGMA_3 = np.array([[complex(1), complex(0)], [complex(0), complex(-1)]])


def single_particle_op_mat(small_mat, target_particle, n):
    # Get the matrix representation of acting with matrix small_mat on the target particle
    # n is the total number of particles
    mat = [1]
    for i in range(n):
        if i == target_particle:
            # If this is the position of the target particle, apply small_mat
            mat = np.kron(mat, small_mat)
        else:
            # Otherwise, do nothing by applying the identity
            mat = np.kron(mat, np.identity(2))
    return mat


def U_x(state, target_particle):
    # NOT operator acting on target particle (particle #)
    # n = number of particles in system
    n = len(state)//2
    # Construct matrix:
    mat = single_particle_op_mat(SIGMA_1, target_particle, n)
    return np.matmul(mat, state)


def U_y(state, target_particle):
    # pi rotation around y axis
    # n = number of particles in system
    n = len(state)//2
    # Construct matrix:
    mat = single_particle_op_mat(SIGMA_2, target_particle, n)
    return np.matmul(mat, state)


def U_z(state, target_particle):
    # Pi rotation around z axis
    # n = number of particles in system
    n = len(state)//2
    # Construct matrix:
    mat = single_particle_op_mat(SIGMA_3, target_particle, n)
    return np.matmul(mat, state)


def U_H(state, target_particle):
    # Hadamard gate
    n = len(state)//2
    # 2x2 matrix for Hadamard gate acting on one particle:
    small_mat = 1/(sym.sqrt(2)) * np.array([[1, 1], [1, -1]])
    # 2n x 2n matrix to act on state:
    mat = single_particle_op_mat(small_mat, target_particle, n)
    return np.matmul(mat, state)


def to_bin_str(num: int, dig: int):
    # Take num and create a binary string of given length out of it
    return f'{num:b}'.zfill(dig)


def bin_swap(m: int, n: int, num: int):
    # Swap mth and nth binary digits of num and return resulting integer
    n, m = n+1, m+1  # adjust for negative index
    bin_rep = list(to_bin_str(num, max(n, m)+1))
    bin_rep[-m], bin_rep[-n] = bin_rep[-n], bin_rep[-m]
    int_rep = int(''.join(bin_rep), 2)
    return int_rep


def U_CNOT(state, target_particle, control_particle):
    # Perform CNOT operation
    return


