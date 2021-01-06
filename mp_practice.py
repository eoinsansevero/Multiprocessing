# multiprocessing practice

import time
import multiprocessing

def do_something():
    print("Sleeping...")
    time.sleep(2)

def main():

    start = time.time()

    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.time()

    print(f"Code finished in {finish - start} seconds.")



if __name__ == "__main__":
    main()
