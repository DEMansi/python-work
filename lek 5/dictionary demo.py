d={876:"Kunjal",890:"Mansi",765:"Hamza",564:"Parthiv",456:"Rahul",}

print(d)
print(d[564])
print(d.get(456))
print(d.items())
print(d.keys)
print(d.values())
print(d.pop(890))
print(d)
d1={333:"Mansi",444:"Taksh"}
d.update(d1)
print(d)
d.popitem()
print(d)

for i in d:
    print(i,":",d[i])
    
