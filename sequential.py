import time
import logging
from collections import deque
import teller as t

def sequential(initial_students, enable_logging):
    if enable_logging:
        logging.info("=" * 60)
        logging.info(" SEQUENTIAL PROCESSING STARTED (Single Bottleneck Queue)")
        logging.info("=" * 60)
        
    start_time = time.perf_counter()
    
    # Initialize the single massive queue
    queue = deque(initial_students)
    worker_name = "SingleWorker"
    
    while queue:
        # Worker takes the first student in line
        student = queue.popleft()
        current_task = student["task"]

        if current_task == "P1":
            t.process_window1(student["name"], enable_logging, worker_name)
            # Student needs to pay, update state and fall back in line
            student["task"] = "P2"
            queue.append(student)
            
        elif current_task == "P2":
            t.process_window2(student["name"], enable_logging, worker_name)
            # Student needs to claim, update state and fall back in line
            student["task"] = "P3"
            queue.append(student)
            
        elif current_task == "P3":
            t.process_window3(student["name"], enable_logging, worker_name)
            # Transaction complete, student leaves the queue permanently

    elapsed_time = time.perf_counter() - start_time
    
    if enable_logging:
        logging.info("-" * 60)
        logging.info(f"Sequential Completed in {elapsed_time:.3f} seconds")
        logging.info("-" * 60)

    return elapsed_time