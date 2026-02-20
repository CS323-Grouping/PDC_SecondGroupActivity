import time

def process_window1(student, do_print):
    time.sleep(0.1)
    if do_print: print(f"Window 1: Acknowledged {student}")

def process_window2(student, do_print):
    time.sleep(0.1)
    if do_print: print(f"Window 2: Payment done for {student}")

def process_window3(student, do_print):
    time.sleep(0.1)
    if do_print: print(f"Window 3: Released grade for {student}")