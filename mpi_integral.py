#mpi_integral.py

from mpi4py import MPI
import sys
import numpy as np

comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
size = comm.Get_size()

NUM_TERMS = 8

def f(x):
    # function to integrate
    return x**2

def integ(func, x_arr):
    # trapezoidal sum given function and list of x values
    area = 0
    for i in range(len(x_arr)-1):
        area += (1/2)*(func(x_arr[i]) + func(x_arr[i+1]))*abs(x_arr[i+1]-x_arr[i])
    return area

def get_input():
    # get user input
    try:
        a = input("Integrate from ")
        b = input(" to ")
        return (float(a), float(b))
    
    except EOFError as e:
        print(e)


interval = get_input()
pieces = np.linspace(interval[1]-interval[0], size*NUM_TERMS)


# each process calculates 8 term sum, returns it to root, reduces answer
if my_rank != 0:
    my_piece = pieces[my_rank*NUM_TERMS:(my_rank+1)*NUM_TERMS - 1]
    p_result = integ(f, my_piece)
else:
    my_piece = pieces[0:7]
    p_result = integ(f, my_piece)

total = comm.reduce(p_result, op=SUM, root=0)

if my_rank == 0:
    print(f"Integral from {interval[0]} to {interval[1]} is: {total}")
    print(f"{NUM_TERMS*size} trapezoids were used.")


MPI.Finalize
