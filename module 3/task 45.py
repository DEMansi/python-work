#Write a Python program to combine values in python list of dictionaries. 
#Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
#300}, o {'item': 'item1', 'amount': 750}]

from collections import Counter
a= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
b = Counter()
for d in a:
    b[d['item']] += d['amount']
print(b) 
 
