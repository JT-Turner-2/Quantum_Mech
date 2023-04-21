from basic_ops import *
from function_helpers import measure, generate_basis_state, run_everything


def grover_algorithm (oracle, n):
    # Function to run grover's algorithm, given an oracle identifying an answer and n
    # n is number of particles in system

    # First, initialize a uniform superposition by starting in state 0 and apply Hadamard to all
    psi = generate_basis_state(0, n)
    psi = run_everything(psi, U_H)
    dim = len(psi) # also known as big N in literature

    # Now apply oracle and then diffusion operator number of steps times
    number_of_steps = int(np.ceil(np.sqrt(dim)))
    for _ in range(number_of_steps):
        psi = oracle(psi)
        psi = diffuser(oracle, n, psi)
        print(psi)
    #Step 4 - measure
    measurement = measure(psi)
    return measurement


def generate_oracle(answer):
    # Function to generate an oracle function.
    # answer is the answer of the oracle (ie: which element is the one we are searching for)
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


oracle_1 = generate_oracle(0)
m = grover_algorithm(oracle_1, 3)
print(m)