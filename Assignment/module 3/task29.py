#Write a Python program to unzip a list of tuples into individual lists. 

z1=[('Mansi', 9), ('Aarohi', 25), ('Ridhi', 3), ('Jeeny', 8)]

a=[[name for name,roll in z1],[roll for name,roll in z1]]
print(a)
