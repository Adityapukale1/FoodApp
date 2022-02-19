keyword=input('\n\nenter the keyword : \n').replace(" ","").upper()
plane_text=input('enter the plane text : \n').replace(" ","").upper()

length1 = len(keyword)  #5
length2 = len(plane_text) #3

a=[]
b=[]



if length1> length2:


    data1= int(length2 / length1)# 3/5 = 1
    data2 = length2 % length1 # 3%5 = 2


    if data1>data2:
        big=data1
        small=data2
    else:
        big = data2
        small = data1


    for i in range(big):
        a.append(keyword[i])

    for i in range(small):
        a.append(a[i])

    for i in plane_text:
        b.append(i)

    print(a)

    print(b)

else:

    data1 = int(length2 / length1)  # 3/5 = 1
    data2 = length2 % length1  # 3%5 = 2

    for i in range(data1):
        for j in keyword:
            a.append(j)

    for i in range(data2):
        a.append(a[i])

    for i in plane_text:
        b.append(i)

    print(a)

    print(b)
