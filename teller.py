import time
import random

def process_window1(student, do_print):
    rand = random.randint(10, 150)
    t = 0.001 * rand
    time.sleep(t)
    if do_print: print(f"Worker: Acknowledged {student} in {t:.3f}s")

def process_window2(student, do_print):
    rand = random.randint(10, 150)
    t = 0.001 * rand
    time.sleep(t)
    if do_print: print(f"Worker: Payment done for {student} in {t:.3f}s")

def process_window3(student, do_print):
    rand = random.randint(10, 150)
    t = 0.001 * rand
    time.sleep(t)
    if do_print: print(f"Worker: Released grade for {student} in {t:.3f}s")