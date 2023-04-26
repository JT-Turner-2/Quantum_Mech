# Main script for our quantum computer

# Module imports
import numpy as np
import matplotlib.pyplot as plt

# Other script imports
from basic_ops import *
from function_helpers import *
from grovers_algorithm import *
from deutsch_jozsa import *


# classical implementation
def classical_implementation(target_list):
    # Returns how long it takes to find element labeled 1 in a list, state
    counter = 0
    for elem in target_list:
        counter += 1
        if elem == 1:
            # We have found it, end the process
            return counter
    raise ValueError("There is no element to find")


def test_grover(target_list):
    # Run grover's algorithm on a np.array with all zeros and one 1 in it
    # Also keep track of # of operations
    counter = 0

    # First, actually find out how long the list is
    N = len(target_list)  # Number of elements in list
    target_pos = np.where(target_list == 1)[0][0]
    m = int(np.ceil(np.log2(N)))  # how many particles we need to use (make sure to round up)

    # Now generate our oracle, encoding our problem
    oracle = generate_oracle(target_pos)
    # Finally run grover's algorithm until we get the right answer (or stop after 100 attempts)
    for _ in range(100):
        ans, c = grover_algorithm(oracle, m)
        counter += c  # increment the counter based on how many operation grover's algorithm did
        if ans == target_pos:
            # We got the right answer
            return counter
        else:
            print('failed')
        # Otherwise, we try again
    # It's not good if our code didn't work after 100 attempts, we should probably raise an error to say that
    raise RuntimeError("Grover's Algorithm failed after 100 attempts")

        # create the graph bit

def generate_test_data(num_particles):
    # Generates a test np array for a given number of particles
    size = 2 ** num_particles
    arr = np.zeros(size)
    ans = np.random.randint(size)
    arr[ans] = 1
    return arr

# # replace the following zeroes with whatever we want to put in
# state = 0
# answer = 0
# n = 0
#
# classical_counter_list=[]
# grover_counter_list=[]
# i=0
# while i>20:
#   grover_counter_holder = 0
#   classical_counter = classical_implementation(state)
#   classical_counter_list.append(classical_counter)
#   preferred_result = 0  # whateverwe want the perferred result to be
#   measurement, grover_counter = grover_algorithm(oracle, n)
#   while measurement != preferred_result:
#     grover_counter_holder = grover_counter_holder + grover_counter
#     measurement, grover_counter = grover_algorithm(oracle, n)
#   grover_counter_holder=grover_counter_holder+grover_counter
#   grover_counter_list.append(grover_counter_holder)
#   i=i+1

#
#
#
#
# #averge calcs
# classical_average=np.mean(classical_counter_list)
# grover_average=np.mean(grover_counter_list)
#
# #plot code
# implementation=["Classical","Quantum"]
# values=[classical_average,grover_average]
# plt.bar(implementation,values)
# plt.xlabel("Implementation")
# plt.ylabel("Iterations")
# plt.title("Effectivness of Classical versus Grover's Algoritim")
# plt.show()
#
  
