for i in range(65,91,1):
    if i==65:
        print(end="   ")
    print(chr(i),end=" ")

for i in range(26):
    print()
    temp=65+i
    flag=1
    for j in range(26):

        # if i==0:
        #     print(chr(temp),end=" ")

        if flag==1:
            print(chr(temp),end="  ")
            flag=0

        print(chr(temp),end=" ")

        temp+=1

        if temp==91:
            temp=65


alpha1=[]
alpha2=[]
a=[]
b=[]
cipher=""

for i in range(65,91,1):
    alpha1.append(chr(i))

keyword=input('\n\nenter the keyword : \n').replace(" ","").upper()
plane_text=input('enter the plane text : \n').replace(" ","").upper()

length1=len(keyword)
length2=len(plane_text)

data1= int(length2 / length1)
data2 = length2 % length1


for i in range(data1):
    for j in keyword:
        a.append(j)

for i in range(data2):
    a.append(a[i])

for i in plane_text:
    b.append(i)

for i in range(len(b)):
    c_index =  alpha1.index(b[i])

    askiicode=ord(a[i])

    if (askiicode +c_index > 90):
        temp = (64 + ((askiicode +c_index) - 90))
        alpha2.append(chr(temp))
    else:
        alpha2.append(chr(askiicode+c_index))


for i in alpha2:
    cipher+=i

print('#Aditya Pukale')
# print('The Encrypted text is:',alpha2)

print('The Encrypted text is : '+cipher)
#Aditya Pukale
#Aditya Pukale
#Aditya Pukale