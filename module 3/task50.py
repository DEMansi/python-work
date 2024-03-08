#Write a Python function that checks whether a passed string is palindrome or not

s = input("enter String = ")
def Palindrome(s):
        
        if s==s[::-1]:
                
                print(s,"palindrom string")
        else:
                print(s,"Not palindrome string")

Palindrome(s)
