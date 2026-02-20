import logging
import random
import copy
import sequential as sq
import parallel as pr

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(message)s',
    datefmt='%H:%M:%S'
)

def generate_students(p1_count, p2_count, p3_count):
    """Generates the mixed queue of students based on user input."""
    students = [{"name": f"Student {i}", "task": "P1"} for i in range(1, p1_count + 1)] + \
               [{"name": f"Student {i}", "task": "P2"} for i in range(p1_count + 1, p1_count + p2_count + 1)] + \
               [{"name": f"Student {i}", "task": "P3"} for i in range(p1_count + p2_count + 1, p1_count + p2_count + p3_count + 1)]
    
    # Shuffle to simulate a realistic, randomized line outside the registrar
    random.shuffle(students)
    return students

if __name__ == "__main__":
    print("\n" + "="*60)
    print("          USTP REGISTRAR BENCHMARK CONFIGURATION")
    print("="*60)
    
    print("\n--- PROCESS CONTEXT ---")
    print("[P1] Request Phase   : Acknowledge form, price fee, send to external cashier.")
    print("[P2] Payment Phase   : Verify cashier receipt, issue releasing slip.")
    print("[P3] Releasing Phase : Receive releasing slip, hand out official grades.")
    print("-" * 60 + "\n")
    
    # Get the number of runs
    while True:
        try:
            runs_for_average = int(input("How many times to run for averaging? (e.g., 3 or 5): "))
            if runs_for_average > 0: 
                break
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("\n--- STUDENT QUEUE SETUP ---")
    # Get the number of students for each queue
    while True:
        try:
            p1_count = int(input("Enter number of students starting at Window 1 (P1): "))
            p2_count = int(input("Enter number of students starting at Window 2 (P2): "))
            p3_count = int(input("Enter number of students starting at Window 3 (P3): "))
            if p1_count >= 0 and p2_count >= 0 and p3_count >= 0: 
                break
            print("Please enter positive integers or zero.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    print("\n--- LOGGING SETUP ---")
    while True:
        a = input("Show Processes Logging (T/F)? ")
        if a.lower() == "t":
            enable_logging = True
            break
        elif a.lower() == "f":
            enable_logging = False
            break
        else:
            print("Invalid input. Please enter T or F.")
            
    # If logging is enabled and there are multiple runs, ask if they want to mute subsequent runs
    mute_subsequent_runs = True
    if enable_logging and runs_for_average > 1:
        while True:
            m = input("Mute detailed logging for subsequent runs to keep output clean (T/F)? ")
            if m.lower() == 't':
                mute_subsequent_runs = True
                break
            elif m.lower() == 'f':
                mute_subsequent_runs = False
                break
            else:
                print("Invalid input. Please enter T or F.")

    total_sq = 0
    total_pr = 0
    total_students = p1_count + p2_count + p3_count
    
    seq_run_times = []
    par_run_times = []

    print("\n" + "="*60)
    print("Starting Benchmark Suite...")
    print(f"Total Runs for Average: {runs_for_average}")
    print(f"Total Queue Size: {total_students} Students")
    print("="*60)

    for i in range(runs_for_average):
        run_number = i + 1
        print(f"\n>>>>> STARTED BENCHMARK RUN {run_number} OF {runs_for_average} <<<<<")
        
        # Determine if this specific run should print detailed logs
        if enable_logging:
            log_this_run = False if (mute_subsequent_runs and i > 0) else True
        else:
            log_this_run = False
        
        if enable_logging and mute_subsequent_runs and i > 0:
            print("(Detailed process logging muted for this run to keep output clean)")
        
        base_queue = generate_students(p1_count, p2_count, p3_count)
        seq_queue = copy.deepcopy(base_queue)
        par_queue = copy.deepcopy(base_queue)

        seq_time = sq.sequential(seq_queue, log_this_run)
        total_sq += seq_time
        seq_run_times.append(seq_time)

        par_time = pr.parallel(par_queue, log_this_run)
        total_pr += par_time
        par_run_times.append(par_time)
        
        print(f">>>>> COMPLETED BENCHMARK RUN {run_number} <<<<<\n")

    time_sq = total_sq / runs_for_average
    time_pr = total_pr / runs_for_average
    speedup = time_sq / time_pr

    # ==========================================
    # FORMATTED UNIFORM PERFORMANCE SUMMARY TABLE
    # ==========================================
    print("\n" + "="*60)
    print(f"{'PERFORMANCE SUMMARY':^60}")
    print("="*60)
    print(f"Queue Config: P1 = {p1_count} | P2 = {p2_count} | P3 = {p3_count} | Total = {total_students}")
    print("-" * 60)
    
    # Table Header with strict widths
    print(f"{'RUN #':<10} | {'SEQUENTIAL (s)':<16} | {'PARALLEL (s)':<14} | {'SPEEDUP':<10}")
    print("-" * 60)
    
    # Table Rows with strictly enforced uniform widths
    for i in range(runs_for_average):
        run_speedup = seq_run_times[i] / par_run_times[i]
        speedup_str = f"{run_speedup:.2f}x"
        run_label = f"Run {i+1}"
        
        print(f"{run_label:<10} | {seq_run_times[i]:<16.4f} | {par_run_times[i]:<14.4f} | {speedup_str:<10}")
    
    print("-" * 60)
    print("AVERAGES:")
    print(f"{'Sequential Avg Time:':<23} {time_sq:.4f} seconds")
    print(f"{'Parallel Avg Time:':<23} {time_pr:.4f} seconds")
    print("-" * 60)
    print(f"{'OVERALL SPEEDUP RATIO:':<23} {speedup:.2f}x")
    print("="*60 + "\n")