# Main script for our quantum computer
'''
def generate_basis_state(k, n):
    # Generate kth basis state of comp basis for n particle system
    state = np.zeros(2**n)
    state[k] = 1
    return state
    '''
# Module imports
import numpy as np
import matplotlib.pyplot as plt

# Other script imports
from basic_ops import *
from function_helpers import *
from grovers_algorithim import *
from deutsch_jorza.py import*
#classical implementation
def classical_implementation(state):
  counter=0
  x=0
  check=state[x]
  if check==1:
    counter=counter+1
    return counter
  else:
    counter=counter+1
    x=x+1
    if x>len(state):
      print("no successful matches")
      return -1
  
  
    #create the graph bit
# replace the following zeroes with whatever we want to put in
state=0
answer=0
n=0
classical counter=classical_implementation(state)
grover_counter_holder=0
preferred_result=0 # whateverwe want the perferred result to be
measurement, grover_counter=grover_algorithm (oracle, n)
while measurement != preferred_result:
    grover_counter_holder=grover_counter_holder+grover_counter
    measurement, grover_counter=grover_algorithm (oracle, n)
 
  
