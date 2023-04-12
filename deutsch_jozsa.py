# Testing our computer by running Deutsch-Jozsa algorithm.
import numpy as np
import sympy as sym


from basic_ops import *
from function_helpers import measure, generate_basis_state


def run_deutsch_jozsa(oracle, n):
    # n+1  particle state (n x + 1 y)
    state_size = n+1
    psi = generate_basis_state(1, state_size)  # 000...001 is the first basis state
    # now put every particle through Hadamard gate
    for i in range(state_size):
        psi = U_H(psi, i)
    # Apply oracle
    psi = oracle(psi)
    # Put particles through Hadamard gate again (except for last one)
    for i in range(state_size-1):
        psi = U_H(psi, i)

    # Now for measuring: we only care about the state of the first particle
    # If it is 0, we return constant, otherwise, the oracle is an even algorithm
    measurement = measure(psi)
    if measurement < 2**n:
        return "constant"
    else:
        return "even"


def dj_oracle_1(state):
    # Oracle for DJ algorithm
    # This one is constant (0)
    return state

def dj_oracle_2(state):
    # Oracle for DJ algorithm
    # This one is constant (1). We will just apply a not gate to last particle
    n = int(np.log2(len(state)))
    state = U_x(state, n)
    return state

def dj_oracle_3(state):
    # This oracle will be even. Let's do with by applying a CNOT gate to half the particles
    n = int(np.log2(len(state)))
    if n % 2 != 0:
        raise ValueError("Need even number of particles")
    for i in range(n//2):
        state = U_CNOT(state, i, n-1)  # particle i controls, particle n (y) is target
    return state



