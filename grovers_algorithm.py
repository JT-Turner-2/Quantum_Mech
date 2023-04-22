import numpy as np

from basic_ops import *
from function_helpers import measure, generate_basis_state, run_everything


def grover_algorithm (oracle, n):
    counter=0
    # Function to run grover's algorithm, given an oracle identifying an answer and n
    # n is number of particles in system

    # First, initialize a uniform superposition by starting in state 0 and apply Hadamard to all
    psi = generate_basis_state(0, n)
    psi = run_everything(psi, U_H)
    dim = len(psi) # also known as big N in literature

    # Now apply oracle and then diffusion operator number of steps times
    number_of_steps = int(np.sqrt(dim)) # TODO May need to modify this calculation with a constant
    for _ in range(number_of_steps):
        psi = oracle(psi)
        counter=counter+dim
        psi = diffuser(oracle, psi)
        counter=counter+np.sqrt(dim)
    # Now measure the state; should give desired output with high probability
    measurement = measure(psi)
    return measurement, counter


def generate_oracle(answer):
    # Function to generate an oracle function.
    # answer is the answer of the oracle (ie: index of element we are searching for)
    def oracle_func(state):
        dim = len(state)
        # first, do some error checking:
        if answer >= dim:
            raise ValueError("State is not big enough -- oracle answer too large")
        # Now construct oracle matrix
        mat = np.identity(dim)
        mat[answer, answer] = -1
        return mat @ state
    return oracle_func


def diffuser(oracle, psi):
    # Step 1- Hadamard
    psi = run_everything(psi, U_H)
    # Step 2 - U_x
    # psi = run_everything(psi, U_x)
    # Step 3 - oracle should be the controlled z gate
    psi = z_0(psi)
    # Step 4 - U_x
    # psi = run_everything(psi, U_x)
    # Step 5- Hadamard
    psi = run_everything(psi, U_H)
    return psi


def z_0(state):
    # z_0 gate (as described in Wright)
    dim = len(state)
    mat = -1 * np.identity(dim)
    mat[0, 0] = 1
    return mat @ state

# oracle_1 = generate_oracle(1)
# m = grover_algorithm(oracle_1, 6)
# print(m)
