import time
import random

def process_student(student_id):
    total = 0
    
    # Simulate record search and grade processing
    for _ in range(1000000):
        total += random.randint(1, 5)
    
    return total

students = 20

start_time = time.time()

for i in range(students):
    process_student(i)

sequential_time = time.time() - start_time

print("Sequential Time:", sequential_time)
