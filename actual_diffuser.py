from basic_ops import *
from function_helpers import measure, generate_basis_state, run_everything
def diffuser (oracle,n,psi):
    # Step 1- Hadamard
    psi=run_everything(psi,U_H())
    #Step 2 - U_z
    psi=run_everything(psi,U_z())
    # Step 3 - oracle
    psi=oracle(psi)
    #Step 4- Hadamard
    psi=run_everything(psi,U_H())
    return psi