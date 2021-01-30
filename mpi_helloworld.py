#mpipy.py

from mpi4py import MPI

'''
remember that there are multiple copies of this code
running as different processes, possibly on different
machines.

to execute code:
$ mpirun -np <number_of_processes> python <filename>
'''

# I wrote this comment using vim. 


comm = MPI.COMM_WORLD
my_rank = comm.Get_rank() # when all the copies run this, they each get a rank
size = comm.Get_size()

# rank 0 process will receive a message from each other process.
# POINT OF DIVERGENCE
if my_rank != 0:
    message = "Hello from process " + str(my_rank)
    comm.send(message, dest=0) # send message to the rank 0 process
else:
    # if this is rank 0 process, retrieve messages from all the rest
    for procid in range(1, size):
        message = comm.recv(source=procid)
        print(f"Message from process {procid}: {message}")
MPI.Finalize
