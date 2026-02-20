import time
import logging
import multiprocessing as mp
from collections import deque
import teller as t

def sequential(initial_students, enable_logging):
    if enable_logging:
        logging.info("=" * 60)
        logging.info(" SEQUENTIAL PROCESSING STARTED (Single Bottleneck Queue)")
        logging.info("=" * 60)
        
    start_time = time.perf_counter()
    
    queue = deque(initial_students)
    worker_name = "SingleWorker"
    logbook_lock = mp.Lock() # Created to satisfy the function call
    
    while queue:
        student = queue.popleft()
        current_task = student["task"]

        if current_task == "P1":
            t.process_window1(student["name"], enable_logging, worker_name)
            
            # Explicitly log the gap before putting them back in line
            if enable_logging:
                logging.info(f"[External I/O] > {student['name']} goes to cashier. Queues up in W2 line.")
                
            student["task"] = "P2"
            queue.append(student)
            
        elif current_task == "P2":
            t.process_window2(student["name"], enable_logging, worker_name)
            
            if enable_logging:
                logging.info(f"[Time Gap] > {student['name']} leaves and returns for schedule. Queues up in W1 line.")
                
            student["task"] = "P3"
            queue.append(student)
            
        elif current_task == "P3":
            t.process_window3(student["name"], enable_logging, worker_name)
            # Process the Critical Section
            t.sign_logbook(student["name"], enable_logging, logbook_lock, worker_name)
            # Transaction complete, student leaves the queue permanently

    elapsed_time = time.perf_counter() - start_time
    
    if enable_logging:
        logging.info("-" * 60)
        logging.info(f"Sequential Completed in {elapsed_time:.3f} seconds")
        logging.info("-" * 60)

    return elapsed_time