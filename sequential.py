import time




def seqeuntial(grades):
    now = time.time()
    for student in grades: # Kani pud is sequential
        time.sleep(0.1) # Simulate time delay para kanang real world delay mag search sa document
        print(f"Processed {student}")

    end = time.time()
    taken = end - now
    print(f"Sequential Ended in : {taken:.2f}")