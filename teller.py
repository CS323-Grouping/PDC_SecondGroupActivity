import time
import random
import logging

def process_window1(student_name, enable_logging, worker_name="Window 1"):
    t = random.uniform(0.01, 0.05)
    time.sleep(t)
    if enable_logging:
        logging.info(f"[{worker_name}] Acknowledged request for {student_name:<10} in {t:.3f}s")

def process_window2(student_name, enable_logging, worker_name="Window 2"):
    t = random.uniform(0.01, 0.05)
    time.sleep(t)
    if enable_logging:
        logging.info(f"[{worker_name}] Payment verified for   {student_name:<10} in {t:.3f}s")

def process_window3(student_name, enable_logging, worker_name="Window 3"):
    t = random.uniform(0.01, 0.05)
    time.sleep(t)
    if enable_logging:
        logging.info(f"[{worker_name}] Released grades for    {student_name:<10} in {t:.3f}s")

def sign_logbook(student_name, enable_logging, lock, worker_name="Window 3"):
    """CRITICAL SECTION: Only one student can sign the physical logbook at a time."""
    with lock:
        t = random.uniform(0.01, 0.02)
        time.sleep(t)
        if enable_logging:
            logging.info(f"[{worker_name}] {student_name:<10} signed the shared logbook in {t:.3f}s")