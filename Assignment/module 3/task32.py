
#Write a Python script to sort (ascending and descending) a dictionary by value. 

d={"a":1,"b":2,"c":3,"d":4,"e":5}

b=sorted([(key,value) for (key,value) in d.items()])
print(b)
print(b[::-1])
