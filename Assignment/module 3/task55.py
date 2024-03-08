#How will you set the starting value in generating random numbers?


import random

print('Random number with seed 40')
for i in range(3):
    
    random.seed(40)
    print(random.randint(25, 50))
