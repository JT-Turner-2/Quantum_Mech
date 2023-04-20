# File defining basic operations that act on states (2n element np array for n particles)
# Each operation should take in the initial state and an identifier of which particles to act on and return the end state
import numpy as np
import sympy as sym
# Using sympy for sqrt 2 to be exact -- may need to change this, but hopefully will work
from function_helpers import find_num_particles

# Defining Pauli spin mats
SIGMA_1 = np.array([[complex(0), complex(1, 0)], [complex(1, 0), complex(0)]])
SIGMA_2 = np.array([[complex(0), complex(0, -1)], [complex(0, 1), complex(0)]])
SIGMA_3 = np.array([[complex(1), complex(0)], [complex(0), complex(-1)]])


def single_particle_op_mat(small_mat, target_particle: int, n: int):
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


def U_x(state, target_particle: int):
    # NOT operator acting on target particle (particle #)
    # n = number of particles in system
    n = find_num_particles(state)
    # Construct matrix:
    mat = single_particle_op_mat(SIGMA_1, target_particle, n)
    return mat @ state


def U_y(state, target_particle: int):
    # pi rotation around y axis
    # n = number of particles in system
    n = find_num_particles(state)
    # Construct matrix:
    mat = single_particle_op_mat(SIGMA_2, target_particle, n)
    return mat @ state


def U_z(state, target_particle: int):
    # Pi rotation around z axis
    # n = number of particles in system
    n = find_num_particles(state)
    # Construct matrix:
    mat = single_particle_op_mat(SIGMA_3, target_particle, n)
    return mat @ state


def U_H(state, target_particle: int):
    # Hadamard gate
    n = find_num_particles(state)
    # 2x2 matrix for Hadamard gate acting on one particle:
    small_mat = 1/(sym.sqrt(2)) * np.array([[1, 1], [1, -1]])
    # 2n x 2n matrix to act on state:
    mat = single_particle_op_mat(small_mat, target_particle, n)
    return mat @ state


def to_bin_str(num: int, dig: int):
    # Take num and create a binary string of given length out of it
    return f'{num:b}'.zfill(dig)


def bin_swap(m: int, n: int, num_to_swap: int, dig_number: int):
    # Swap mth and nth binary digits of num and return resulting integer
    bin_rep = list(to_bin_str(num_to_swap, dig_number))
    bin_rep[m], bin_rep[n] = bin_rep[n], bin_rep[m]
    int_rep = int(''.join(bin_rep), 2)
    return int_rep


def kronecker_delta(m,n):
    if m == n:
        return 1
    else:
        return 0


def U_CNOT(state, control_particle: int, target_particle: int):
    # Perform CNOT operation
    # To do this, we will need a new basis state where C and T are the first two particle
    n = find_num_particles(state)  # number of particles
    if target_particle == control_particle:
        raise ValueError("Target and Control particles must be different")

    if target_particle > n or control_particle > n:
        raise ValueError("Invalid target or control particle: not enough particles in system")
    # To begin, we define our new basis state. Let integers represent the corresponding state in the computational basis
    # The only operation we will need is rearranging the basis vectors to create our new basis
    comp = [x for x in range(len(state))]
    new_basis = [bin_swap(0, control_particle, x, n) for x in comp]
    if target_particle == 0:
        # The target particle is now in the control particle position
        new_basis = [bin_swap(1, control_particle, x, n) for x in new_basis]
    else:
        new_basis = [bin_swap(1, target_particle, x, n) for x in new_basis]
    # Now define a change of basis matrix
    basis_change_mat = np.array([[kronecker_delta(c, b) for c in comp] for b in new_basis])
    # We can make U_CNOT matrix in new_basis as:
    mat_new_basis = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ]
    for _ in range(n - 2):
        mat_new_basis = np.kron(mat_new_basis, np.identity(2))
    mat_comp_basis = np.transpose(basis_change_mat) @ mat_new_basis @ basis_change_mat
    return mat_comp_basis @ state

