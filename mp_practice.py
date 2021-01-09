# multiprocessing practice

import time
import multiprocessing
import numpy as np

def do_something(num, queue):
    print("Sleeping...")
    time.sleep(2)
    queue.put(np.ones((2, 2, 2))*num * 2)


def main():

    start = time.time()

    result_queue = multiprocessing.Queue()


    p1 = multiprocessing.Process(target=do_something, args=[2, result_queue])
    p2 = multiprocessing.Process(target=do_something, args=[2, result_queue])

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    output = [result_queue.get() for job in [p1, p2]]
    print(output[0])


    finish = time.time()

    print(f"Code finished in {finish - start} seconds.")



if __name__ == "__main__":
    main()
