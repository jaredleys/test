print('Hello World')

print(1 + 2)


# Heads or tails coin flip

import random

val = input("Enter a number: ")

print(val)

x = random.uniform(0,1)

print(x)

if 0 <= x <= 1/2:
    print("The flip landed on Tails!")
else:
    print("The flip landed on Heads!")