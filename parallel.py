import teller as t
import time
from multiprocessing import Pool, cpu_count

def parallel(grades, do_print):
    now = time.time()
    args = [(g, do_print) for g in grades]
    with Pool(cpu_count()) as p:
        p.starmap(t.process_grade, args)
    end = time.time()
    taken = end - now
    print(f"Parallelism ended in {taken:.2f}")
    return taken

