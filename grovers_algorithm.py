from basic_ops import *
from function_helpers import measure, generate_basis_state, run_everything
from actual_diffuser import*
def grovers_algorithm (oracle, n):
    state_size = n + 1  # check to make sure this is correct
    psi = generate_basis_state(1, state_size)
    #step 1 Hadamard
    psi=run_everything(psi,U_H())
    # nexts steps need to repeat until sufficent probability. todo assign value
    #step 2 - Oracle
    psi=oracle(psi)
    #step 3 - diffuser
    psi=diffuser(oracle,n,psi)
    #Step 4 - measure
    measurement=measure(psi)
    return measurement
