import random
import time
import multiprocessing as mp
import threading
import logging
import teller as t

def async_cashier_walk(student, q_out, enable_logging):
    """Simulates the External I/O gap: Student walks to cashier independently"""
    if enable_logging:
        logging.info(f"[External I/O] > {student['name']} goes to cashier. Queues up in W2 line.")
    time.sleep(random.uniform(0.02, 0.05)) # Asynchronous delay
    student["task"] = "P2"
    q_out.put(student)

def async_time_gap(student, q_out, enable_logging):
    """Simulates the Time Gap: Student leaves and returns on schedule"""
    if enable_logging:
        logging.info(f"[Time Gap] > {student['name']} leaves and returns for schedule. Queues up in W3 line.")
    time.sleep(random.uniform(0.02, 0.05)) # Asynchronous delay
    student["task"] = "P3"
    q_out.put(student)

def worker_1(q_in, q_out, enable_logging):
    threads = []
    while True:
        student = q_in.get()
        if student is None:
            break
        
        t.process_window1(student["name"], enable_logging, "Window 1")
        
        # Student leaves window to walk to cashier (Worker is free for next student)
        th = threading.Thread(target=async_cashier_walk, args=(student, q_out, enable_logging))
        th.start()
        threads.append(th)
        
    # Wait for all students to finish walking before closing the queue
    for th in threads:
        th.join()
    q_out.put(None)

def worker_2(q_in, q_out, enable_logging):
    threads = []
    while True:
        student = q_in.get()
        if student is None:
            break
            
        t.process_window2(student["name"], enable_logging, "Window 2")
        
        # Student leaves window to wait for release schedule (Worker is free)
        th = threading.Thread(target=async_time_gap, args=(student, q_out, enable_logging))
        th.start()
        threads.append(th)
        
    for th in threads:
        th.join()
    q_out.put(None)

def worker_3(q_in, enable_logging, logbook_lock):
    while True:
        student = q_in.get()
        if student is None:
            break
            
        t.process_window3(student["name"], enable_logging, "Window 3")

        t.sign_logbook(student["name"], enable_logging, logbook_lock, "Window 3")

def parallel(initial_students, enable_logging):
    if enable_logging:
        logging.info("=" * 60)
        logging.info(" PARALLEL PROCESSING STARTED (3 Independent Windows)")
        logging.info("=" * 60)

    start_time = time.perf_counter()

    # Create queues and the Critical Section Lock
    q1, q2, q3 = mp.Queue(), mp.Queue(), mp.Queue()
    logbook_lock = mp.Lock()

    for student in initial_students:
        if student["task"] == "P1": q1.put(student)
        elif student["task"] == "P2": q2.put(student)
        elif student["task"] == "P3": q3.put(student)

    q1.put(None)

    # Pass the lock to Window 3
    p1 = mp.Process(target=worker_1, args=(q1, q2, enable_logging))
    p2 = mp.Process(target=worker_2, args=(q2, q3, enable_logging))
    p3 = mp.Process(target=worker_3, args=(q3, enable_logging, logbook_lock))

    p1.start(); p2.start(); p3.start()
    p1.join(); p2.join(); p3.join()

    elapsed_time = time.perf_counter() - start_time

    if enable_logging:
        logging.info("-" * 60)
        logging.info(f"Parallel Completed in {elapsed_time:.3f} seconds")
        logging.info("-" * 60)

    return elapsed_time