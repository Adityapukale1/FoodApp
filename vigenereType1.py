key = (input('Enter the key :   '))

key1=[]

for i in key:
    key1.append(i)

plainText =input('\nEnter plain text : \n').upper().replace(" ","")
cipherText=""

print(key1)
data=int(0)
for i in range(len(plainText)):

    if i<3:
        value = i
    else:
        value =  int(i) % int(len(key1))

    # print(value)

    data= (ord(plainText[i])) + int(key1[value])


    if data > 90:
        data -= 26


    cipherText += chr(data )


# print(data)
print(cipherText)


