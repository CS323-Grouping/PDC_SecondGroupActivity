import time
import multiprocessing as mp
import logging
import teller as t

def worker_1(q_in, q_out, enable_logging):
    while True:
        student = q_in.get()
        if student is None:  # Sentinel value indicating no more students
            q_out.put(None)  # Pass the sentinel to the next window
            break
        
        t.process_window1(student["name"], enable_logging, "Window 1")
        student["task"] = "P2"
        q_out.put(student)   # Send student directly to Window 2's queue

def worker_2(q_in, q_out, enable_logging):
    while True:
        student = q_in.get()
        if student is None:
            q_out.put(None)
            break
            
        t.process_window2(student["name"], enable_logging, "Window 2")
        student["task"] = "P3"
        q_out.put(student)   # Send student directly to Window 3's queue

def worker_3(q_in, enable_logging):
    while True:
        student = q_in.get()
        if student is None:
            break
            
        t.process_window3(student["name"], enable_logging, "Window 3")
        # Transaction complete, student exits

def parallel(initial_students, enable_logging):
    if enable_logging:
        logging.info("=" * 60)
        logging.info(" PARALLEL PROCESSING STARTED (3 Independent Windows)")
        logging.info("=" * 60)

    start_time = time.perf_counter()

    # Create safe communication queues between processes
    q1, q2, q3 = mp.Queue(), mp.Queue(), mp.Queue()

    # Pre-populate queues based on where students are starting
    for student in initial_students:
        if student["task"] == "P1":
            q1.put(student)
        elif student["task"] == "P2":
            q2.put(student)
        elif student["task"] == "P3":
            q3.put(student)

    # Put a sentinel in Queue 1 to tell Window 1 when the initial line is finished
    q1.put(None)

    # Initialize the worker processes
    p1 = mp.Process(target=worker_1, args=(q1, q2, enable_logging))
    p2 = mp.Process(target=worker_2, args=(q2, q3, enable_logging))
    p3 = mp.Process(target=worker_3, args=(q3, enable_logging))

    # Start the workers simultaneously
    p1.start()
    p2.start()
    p3.start()

    # Wait for all workers to finish their queues
    p1.join()
    p2.join()
    p3.join()

    elapsed_time = time.perf_counter() - start_time

    if enable_logging:
        logging.info("-" * 60)
        logging.info(f"✔ Parallel Completed in {elapsed_time:.3f} seconds")
        logging.info("-" * 60)

    return elapsed_time