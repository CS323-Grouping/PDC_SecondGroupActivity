import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import List
import teller as t


def run_parallel(students: List[list], do_print: bool) -> float:
    """Execute teller windows in parallel and return execution time."""

    windows = (
        t.process_window1,
        t.process_window2,
        t.process_window3,
    )

    print("\n" + "=" * 50)
    print("        PARALLEL PROCESSING STARTED")
    print("=" * 50)
    print(f"Processing {len(students)} students "
          f"across {len(windows)} windows...\n")

    start_time = time.perf_counter()

    with ProcessPoolExecutor(max_workers=len(windows)) as executor:
        futures = [
            executor.submit(window, students, do_print)
            for window in windows
        ]

        for i, future in enumerate(as_completed(futures), start=1):
            future.result()
            print(f"✓ Window {i} finished")

    elapsed_time = time.perf_counter() - start_time

    print("\n" + "-" * 50)
    print(f"✔ Completed in {elapsed_time:.2f} seconds")
    print("-" * 50)

    return elapsed_time
