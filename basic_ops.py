# File defining basic operations that act on states (2n element np array for n particles)
# Each operation should take in the initial state and an identifier of which particles to act on and return the end state
# TODO: determine if we want to use SE or simple matrix mechanics to model our operators
import numpy as np

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

