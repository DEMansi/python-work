#Write a Python program to count the frequency of words in a file.

from collections import Counter
file=open("demo.txt","r")
tmp=Counter(file.read().split())
print(tmp)
file.close()
