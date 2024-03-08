#Write a Python function to check whether a number is in a given range

def test_range(n):
    if n in range(1,9999+1):
        return n,"is in Range"
    else :
        return n,"is not in range"
n=int(input("enter value = "))
print(test_range(n))


