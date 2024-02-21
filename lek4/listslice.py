# 17 16 15 14 13  12     11 10  9 8  7      6   5  4  3   2  1   -
l=[1,2,3,1.1,2.2,"tops",10,True,1,2,False,"py",10,20,100,200,90]
#= 0 1 2 3  4   5     6    7  8   9 10  11   12  13 14  15  16  +
      # [s:and:jamp]
print(l[:1])
print(l[15::5])
print(l[13:])
print(l[1:10:5])
print(l[::15])

print(l[:-16])
print(l[-15::3])
print(l[-4:])
print(l[-15:-5:5])
print(l[::-5])
