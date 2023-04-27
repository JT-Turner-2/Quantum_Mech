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
NUM_TRIALS = 20
classical_data = []
grover_data = []
m_range = range(2, 8)
for m in m_range:
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

lengths = np.array([2**m for m in m_range])
length_space = np.linspace(lengths.min(), lengths.max())

# Fit to our model
# First, define fitting functions
def linear_fit_func(x, a, b):
    return a*x+b


def sqrt_fit_func(x, a, b):
    return a*np.sqrt(x) + b


# Now actually do the fits
popt_classical, pcov_classical = curve_fit(linear_fit_func, lengths, classical_avg, sigma=classical_err, absolute_sigma=True)
popt_grover, pcov_grover = curve_fit(sqrt_fit_func, lengths, grover_avg)

# plot the classical case
plt.figure()
plt.plot(lengths, classical_data, '.', c="blue")
plt.plot(lengths, classical_avg, 's', c='red', markersize=5)
plt.errorbar(lengths, classical_avg, yerr=classical_err, ecolor='darkred', ls='none', capsize=3, capthick=2)
plt.plot(length_space, linear_fit_func(length_space, *popt_classical), c='black')
plt.xlabel("Length of List")
plt.ylabel("Iterations")
plt.title("Iterations for Classical Algorithm")
plt.show()


# Plot for grover's algorithm
plt.figure()
plt.plot(lengths, grover_data, '.', c="blue")
plt.plot(lengths, grover_avg, 's', c='red', markersize=5)
plt.errorbar(lengths, grover_avg, yerr=grover_err, ecolor='darkred', ls='none', capsize=3, capthick=2)
plt.plot(length_space, sqrt_fit_func(length_space, *popt_grover), c='black')
plt.xlabel("Length of List")
plt.ylabel("Iterations")
plt.title(r"Iterations for Grover's Algorithm")
plt.show()

