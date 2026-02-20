import teller as t
import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def parallel(grades, do_print):
    now = time.time()

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(t.process_grade, g, do_print) for g in grades]

        for f in as_completed(futures):
            _ = f.result()

    end = time.time()
    taken = end - now
    print(f"Parallelism ended in {taken:.2f}")
    return taken

