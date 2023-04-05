# File defining basic operations that act on states (2n element np array for n particles)
# Each operation should take in the initial state and an identifier of which particles to act on and return the end state
# TODO: determine if we want to use SE or simple matrix mechanics to model our operators
import numpy as np
import astropy
from astropy import units as u
from astropy.constants import hbar
import cmath
# Defining Pauli spin mats
SIGMA_1 = np.array[[complex(0), complex(1, 0)], [complex(1, 0), complex(0)]]
SIGMA_2 = np.array[[complex(0), complex(0, -1)], [complex(0, 1), complex(0)]]
SIGMA_2 = np.array[[complex(1), complex(0)], [complex(0), complex(-1)]]
def U_x(state, target_particle):
    # NOT operator acting on target particle
    # n = number of particles in system
    n = len(state)//2
    # Construct matrix:
    mat = [1]
    for _ in range(n-1):
        mat = np.kron(mat, np.identity(2))
    mat = np.kron(mat, )
    return state


