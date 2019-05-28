a=int(input('enter initial reading\n'))
b=int(input('enter final reading\n'))
p=int(b-a)
if (0<=p<=100):
    a=int(p*3)
    print(a)
elif ((p>100)and(p<=300)):
    b=int((100*3)+((p-100)*6))
    print(b)
elif ((p>=100)and(p>=300)and(p<=500)):
    c=int((100*3)+(200*6)+((p-300)*10))
    print(c)
elif (p>500):
    d=int((100*3)+(200*6)+((200)*10)+((p-500)*11))
    print(d)

    


