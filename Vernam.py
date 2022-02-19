#Aditya Pukale RN. 42 BE-A CSE ©Aditya Enterprizes

plain_text=input('Enter the plain text : \n').replace(" ","").upper()

keyword=input('\nEnter the keyword : \n').replace(" ","").upper()

pt=plain_text
kw=keyword



length1 = len(keyword)  #5

length2 = len(plain_text) #3

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

    for i in plain_text:
        b.append(i)

else:

    data1 = int(length2 / length1)  # 3/5 = 1
    data2 = length2 % length1  # 3%5 = 2

    for i in range(data1):
        for j in keyword:
            a.append(j)

    for i in range(data2):
        a.append(a[i])

    for i in plain_text:
        b.append(i)

plane_num=[]
key_num=[]
count=[]

data=""

for i in plain_text:
    plane_num.append(ord(i)-65)

for i in keyword:
    key_num.append(ord(i)-65)

temp=0
for i in range(len(plane_num)):
    temp = plane_num[i]+key_num[i]

    if temp>25:
        temp=temp-26

    count.append(temp)


plain_text=''

for i in count:
    plain_text += chr(65+i)


# print(count)
print("\nAssigning number to each character of plain text:\n"+pt+"  -->")
print(plane_num,"\n")

print("Assigning number to each character of keyword:\n"+kw+"  -->")
print(key_num,"\n")

print("Adding the numbers (subtract the no. 26 from added no if greater than 26 else leave it):")
print(count,"\n")
print("CIPHER TEXT : " + plain_text)
