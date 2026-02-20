import time
import teller as t



def seqeuntial(grades, do_print):
    now = time.time()
    for student in grades:
        t.process_grade(student, do_print)

    end = time.time()
    taken = end - now
    print(f"Sequential Ended in : {taken:.2f}")

    return taken