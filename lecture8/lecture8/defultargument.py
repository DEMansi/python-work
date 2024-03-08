#defultargument

def test(a=20,b=45,c=56,d=89):
    print("A:",a,"B:",b,"C:",c,"D:",d)

test(1,2,3,4)
test(1,2,3)
test(1,2)
test(1)
test()

#keyword argument

test(b=100,d=200)
