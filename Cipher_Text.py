text=input('Enter any string you want to\n\n')
a=''
b=''
temp=''


key=int(input("enter a key to perform cipher operation :    \n\n"))

text=text.lower()

for i in text:
    if i.isspace()==True or i.isdigit()==True:
        b+=i

    elif(ord(i)+key>122):
        temp= (96 + ((ord(i)+key)-122))
        a = chr((temp))
        b += a

    else:
        a = chr(ord(i) + key)
        b += a

finalText=b;

print("The original string is :  "+text +"\n\n")

print("The cipher String is :  "+finalText)











# rows, cols = (5, 5)
#
# # method 2a
# a=[[111]*5]*5 #1
#
# arr = [[0 for i in range(cols)] for j in range(rows)] #2
#
# # lets change the first element of the
# # first row to 1 and print the array
# arr[0][0] = 555
# a[0][0]=456
#
#
# for i in a:
#     print(i)
#
# for row in arr:
#     print(row)