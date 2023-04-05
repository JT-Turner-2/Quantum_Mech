# File defining basic operations that act on states (2n element np array for n particles)
# Each operation should take in the initial state and an identifier of which particles to act on and return the end state
# TODO: determine if we want to use SE or simple matrix mechanics to model our operators
import numpy as np
import astropy
from astropy import units as u
from astropy.constants import hbar
import cmath
#idk if cmath is installed in my enviroment state is array of complext

def U_x(state, target_particle):
    # NOT operator acting on target particle
    #TODO: finish this
    return state


