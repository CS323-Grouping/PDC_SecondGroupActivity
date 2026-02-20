import sequential as sq
import parallel as pr

grades = ["Alice", "Bob", "Charlie", "David", "Eve"]
students = [f"Student {i}" for i in range(1, 16)]

if __name__ == "__main__":
    while True:
        a = input("Show Processes(T/F)? ")
        if a.lower() == "t":
            do_print = True
            break
        elif a.lower() == "f":
            do_print = False
            break
        else:
            print("Invalid")

    runs = 5 # e change ra ang number  if dili sya convincing ang pag test niya.

    total_sq = 0
    total_pr = 0

    for _ in range(runs):
        total_sq += sq.sequential(students, do_print)
        total_pr += pr.parallel(students, do_print)

    time_sq = total_sq / runs
    time_pr = total_pr / runs
    speedup = time_sq / time_pr

    print("\n===== PERFORMANCE SUMMARY =====")
    print(f"Sequential Average Time: {time_sq:.4f} seconds")
    print(f"Parallel Average Time:   {time_pr:.4f} seconds")
    print(f"Speedup:                 {speedup:.2f}x")
