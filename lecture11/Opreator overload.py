class Point:

    def __init__(self,x,y): 
        print("init called")
        self.x=x
        self.y=y
    def __str__(self):
        print("str called")
        return "({0},{1})".format(self.x,self.y)
    def __add__(self,obj):
        print("add called")
        x=self.x+obj.x
        y=self.y+obj.y
        return point(x,y)

p1=point(10,20)
print(p1)
p2=point(30,40)
print(p2)
print("Addition of Objects :",p1+p2)
