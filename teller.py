import time
import random
import logging

def process_window1(student_name, enable_logging, worker_name="Window 1"):
    # Simulated processing time
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