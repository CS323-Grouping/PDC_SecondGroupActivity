import time
import random
from multiprocessing import Pool, cpu_count

def process_student(student_id):
    total = 0
    for _ in range(1000000):
        total += random.randint(1, 5)
    return total

def run_sequential(students):
    start_time = time.time()
    
    for i in range(students):
        process_student(i)
    
    return time.time() - start_time

def run_parallel(students):
    start_time = time.time()
    
    with Pool(cpu_count()) as pool:
        pool.map(process_student, range(students))
    
    return time.time() - start_time


if __name__ == "__main__":
    students = 20
    
    sequential_time = run_sequential(students)
    print("Sequential Time:", sequential_time)
    
    parallel_time = run_parallel(students)
    print("Parallel Time:", parallel_time)
    
    speedup = sequential_time / parallel_time
    print("Speedup:", speedup)
    