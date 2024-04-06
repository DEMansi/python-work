#Write a Python program to read last n lines of a file.

n=int(input("enter N number : "))
def lastnlines(f,n):
	with open('demo.txt') as f:
		for i in (f.readlines() [-n:]):
			print(i)

lastnlines('demo.txt',n)
