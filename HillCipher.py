# for i in range(65,91,1):
#     print(chr(i))

j=1
k=1
keys=[]
p=[]
c=[]
print('Enter the key in matrix at ')
for i in range(9):
    keys.append(int(input(f'position {k}{j} :  ')))
    j+=1

    if j==4:
        j=1
        k+=1

planeText=input('\nEnter plane Text :\n').replace(" ","").upper()


check=len(planeText)%3

for i in range(check):
    planeText+='X'

for i in planeText:

    j=(ord(i)-65)
    p.append(j)


print(p)


for i in range(0 ,len(p) ,3):
    for j in range(0,9,3):

        k = int(( (keys[j] * p[i]) + (keys[j+1] * p[i+1]) + (keys[j+2] * p[i+2]) ) % 26)

        c.append(k)



ans =""
for i in c:
    ans+=chr(i+65)
    # print(chr(i+65))

print("\n\n"+ans)


