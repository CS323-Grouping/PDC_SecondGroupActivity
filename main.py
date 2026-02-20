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
    time_sq = sq.sequential(students, do_print)
    time_pr = pr.parallel(students, do_print)
    speedup = time_sq / time_pr

    print(f"Speedup {speedup}")


