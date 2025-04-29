import random

for i in range(1, 101):
    n = random.randint(1, 100)
    print(f"{i:3d}) {n:3d}", end=" ")
    if n % 7 == 0:
        print("Lucky number!", end="")
    print()

    if i % 5 == 0:
        print("---") 
