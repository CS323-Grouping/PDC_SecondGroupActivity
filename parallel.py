import teller as t
import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def parallel(students, do_print):
    now = time.time()

    with ProcessPoolExecutor() as executor:
        future_window1 = executor.submit(t.process_window1, students, do_print)
        future_window2 = executor.submit(t.process_window2, students, do_print)
        future_window3 = executor.submit(t.process_window3, students, do_print)

        _ = future_window1.result()
        _ = future_window2.result()
        _ = future_window3.result()

    end = time.time()
    taken = end - now
    print(f"Task Parallelism Ended in: {taken:.2f} seconds")
    return taken
