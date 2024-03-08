#Write a Python program to create and display all combinations of letters, 
#selecting each letter from a different key in a dictionary.

import itertools      
d ={'1':['a','b'], '2':['c','d']}
for i in itertools.product(*[d[j] for j in sorted(d.keys())]):
    print(''.join(i))
