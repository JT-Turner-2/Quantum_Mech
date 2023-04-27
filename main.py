# Main script for our quantum computer

# Module imports
import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

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
    for _ in range(50):
        ans, c = grover_algorithm(oracle, m)
        counter += c  # increment the counter based on how many operation grover's algorithm did
        if ans == target_pos:
            # We got the right answer
            return counter
        # Otherwise, we try again
    # It's not good if our code didn't work after 100 attempts, we should probably raise an error to say that
    raise RuntimeError("Grover's Algorithm failed after 50 attempts")

        # create the graph bit

def generate_test_data(num_particles):
    # Generates a test np array for a given number of particles
    size = 2 ** num_particles
    arr = np.zeros(size)
    ans = np.random.randint(size)
    arr[ans] = 1
    return arr


# Perform algorithms and count\
NUM_TRIALS = 10
classical_data = []
grover_data = []
for m in range(3, 6):
    # Note our implementation doesn't work that well for m=2
    classical_list = []
    grover_list = []
    for _ in range(NUM_TRIALS):
        testlist = generate_test_data(m)
        classical_counter = classical_implementation(testlist)
        classical_list.append(classical_counter)
        grover_counter = test_grover(testlist)
        grover_list.append(grover_counter)

    classical_data.append(classical_list)
    grover_data.append(grover_list)
    print(f"Process complete for m={m}")
# Now get the data in a nice format, take averages, errors, etc...
classical_data = np.array(classical_data)
classical_avg = np.mean(classical_data, axis=1)
classical_err = np.std(classical_data, axis=1) / np.sqrt(NUM_TRIALS)

grover_data = np.array(grover_data)
grover_avg = np.mean(grover_data, axis=1)
grover_err = np.std(grover_data, axis=1) / np.sqrt(NUM_TRIALS)

lengths = np.array([2**m for m in range(3, 6)])


# Fit to our model
def linear_fit_func(x, a, b):
    return a*x+b


popt_classical, pcov_classical = curve_fit(linear_fit_func, lengths, classical_avg)

# plot the classical case
plt.figure()
plt.plot(lengths, classical_data, '.', c="blue")
plt.plot(lengths, classical_avg, 's', c='red', markersize=5)
plt.errorbar(lengths, classical_avg, yerr=classical_err, ecolor='darkred', ls='none', capsize=3, capthick=2)
plt.plot(lengths, linear_fit_func(lengths, *popt_classical), c='black')
plt.xlabel("Length of List")
plt.ylabel("Iterations")
plt.title("Iterations for Classical Algorithm")
plt.show()


# Plot for grover's algorithm
plt.figure()
plt.plot(lengths, grover_data, '.', c="blue")
plt.plot(lengths, grover_avg, 's', c='red', markersize=5)
plt.errorbar(lengths, grover_avg, yerr=grover_err, ecolor='darkred', ls='none', capsize=3, capthick=2)
plt.xlabel("Length of List")
plt.ylabel("Iterations")
plt.title("Iterations for Grover's Algorithm")
plt.show()





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
  
