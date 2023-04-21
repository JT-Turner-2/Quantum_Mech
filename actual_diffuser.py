from basic_ops import *
from function_helpers import measure, generate_basis_state, run_everything
def diffuser (oracle,n,psi):
    # Step 1- Hadamard
    psi = run_everything(psi, U_H)
    # Step 2 - U_x
    psi = run_everything(psi, U_x)
    # Step 3 - oracle should be the controlled z gate
    psi = oracle(psi)
    # Step 4 - U_x
    psi = run_everything(psi, U_x)
    # Step 5- Hadamard
    psi = run_everything(psi, U_H)
    return psi
#todo make sure the controlled z gzte makes sense
# DO NOT LOOP IN HERE!
