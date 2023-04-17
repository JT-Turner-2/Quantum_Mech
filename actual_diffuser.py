from basic_ops import *
from function_helpers import measure, generate_basis_state, run_everything
def diffuser (oracle,n):
    state_size=n+1 # check to make sure this is correct
    psi = generate_basis_state(1, state_size)
    # Step 1- Hadamard
    psi=run_everything(psi,U_H())
    #Step 2 - U_z
    psi=run_everything(psi,U_z())
    # Step 3 - oracle
    psi=oracle(psi)
    #Step 4- Hadamard
    psi=run_everything(psi,U_H())
    return psi