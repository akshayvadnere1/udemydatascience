# Python Basics
import numpy as np

list_of_numbers = [1, 2, 3, 4, 5, 6, 7]

for number in list_of_numbers:
    if number % 2 == 0:
        print(number, " is even")
    else:
        print(number, " is odd")
print("All Done")

random_list = np.random.normal(25.0, 5.0, 10)
print(random_list)
