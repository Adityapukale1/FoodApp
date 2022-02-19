print('Transposition 2')  #name of pgm

count = int(input('Enter total key no:  '))
key=[]
temp=0


# taking key from user
for i in range(count):
    key.append(int(input(f'Enter key no {i+1}    :  ')))

locationOfKey=[]

#finding the index position of key in ascending order
for i in range(count):
    temp = key.index(i+1)
    locationOfKey.append(temp)

planeText= input('\nEnter plane Text\n').replace(" ","").upper()

print('\n')

for i in key:
    print(i,end=" ")

print('\n')

j= len(planeText) % count

if j!=0:
    for i in range(count-j):
        planeText+='X'

for i in range(len(planeText)):

    print(planeText[i],end=" ")

    if int(i+1) % int(max(key)) ==0:
        print()


temp=0
temp1=0
second=""

for i in locationOfKey:
    temp1=i

    for j in range(len(planeText)):

        if temp == 0:
            second+=planeText[temp1]
            # print(planeText[temp1])
            temp=1

        elif temp==1:

            if temp1+count<len(planeText):
                second+=planeText[temp1+count]
                temp1+=count
            else:
                temp=0
                break


print('Cipher Text is :  '+second)

print('\n')
for i in key:
    print(i,end=" ")

print('\n')

for i in range(len(second)):

    print(second[i],end=" ")

    if int(i+1) % int(max(key)) ==0:
        print()

temp=0
temp1=0
planeText=""
for i in locationOfKey:
    temp1=i

    for j in range(len(second)):

        if temp == 0:
            planeText+=second[temp1]
            # print(planeText[temp1])
            temp=1

        elif temp==1:

            if temp1+count<len(second):
                planeText+=second[temp1+count]
                temp1+=count
            else:
                temp=0
                break


print('The output is : '+planeText)

# attackpostponeduntiltwoamxyz