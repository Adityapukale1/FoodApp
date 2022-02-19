d={}
a=[]
b=[]

def takingCiphertext():

    cipherText = input('Enter the keyword here:\n').upper()

    # deleting the repeted text
    for i in cipherText:
        if i in a:
            continue
        else:
            a.append(i)


#Generating the matrix
def generateMatrix():

    m1 = 0
    alphabet = 65

    for i in range(1,6,1):
        for j in range(1,6,1):

            condition = True

            if (m1 != len(a)):
                keys = int(str(i) + str(j))
                values = a[m1]
                m1 += 1

            else:
                keys = int(str(i) + str(j))

                while (condition):
                    m = chr(alphabet)

                    if m in a:
                        if (m == 'I'):  # checking i is present to omit j
                            alphabet += 2
                        else:
                            alphabet += 1

                    else:
                        # special condition for i/j to fit in 5*5 matrix
                        if 'J' in a and m == 'I':
                            alphabet += 1

                        # special condition for i/j to fit in 5*5 matrix
                        elif (m == 'I'):
                            values = "I"
                            alphabet += 2
                            condition = False

                        # In normal scenario
                        else:
                            values = m
                            alphabet += 1
                            condition = False

            d[keys] = values




# generating the cipher text

def Encryption():

    # finding_the_index=0

    text=input('Enter sentenece to encrypt it :\n').upper().replace(" ","")

    a.clear()

    # getting all the input text into the list
    for i in text:
        a.append(i)

    # adding x at the end of the list if group of two can't be formed
    no_of_x=len(a)%2


    for i in range(no_of_x):
        a.append('X')

    # main logic to cipher the text

    for i in range(0,len(a),2):


        row = 1
        temp = []
        temp2 = []

        global temp1
        temp1 = 0

        text1=a[i]
        text2=a[i+1]

        if text1=='J' :
            text1='I'

        if text2 == 'J' :
            text2 = 'I'

        while row<6:
            # print('temp1--->', temp1,'row',row,'col',col)
            # print('row---',row)
            temp.clear()
            temp2.clear()

            for col in range(1,6,1):
                temp.append(d[int(str(row) + str(col))])  #row wise apeending
                temp2.append(d[int(str(col) + str(row))])  #col wise apeending

            if temp1==0:
                # print('checking row possibility')
                # print('text1='+text1,'text2 ='+text2)
                if text1 in temp:
                    if text2 in temp:
                        # print('they are in same row')

                        finding_the_index=temp.index(text1)
                        if finding_the_index==4:
                            b.append(temp[0])
                        else:
                            b.append(temp[finding_the_index+1])


                        finding_the_index = temp.index(text2)
                        if finding_the_index==4:
                            b.append(temp[0])
                        else:
                            b.append(temp[finding_the_index+1])

                        break

                if text1 in temp2:
                    if text2 in temp2:
                        # print('they are in same column')

                        finding_the_index = temp2.index(text1)
                        if finding_the_index == 4:
                            b.append(temp2[0])
                        else:
                            b.append(temp2[finding_the_index+1])

                        finding_the_index = temp2.index(text2)
                        if finding_the_index == 4:
                            b.append(temp2[0])
                        else:
                            b.append(temp2[finding_the_index+1])

                        break

            else:
                # print('they are diagonal to each other')

                listOfKeys = [key for (key, value) in d.items() if value == text1]
                listOfKeys1 = [key for (key, value) in d.items() if value == text2]
                # print(listOfKeys)

                m1=str(listOfKeys)
                j1=str(listOfKeys1)

                b.append(d[int(str(m1[1]) + str(j1[2]))])
                b.append(d[int(str(j1[1]) + str(m1[2]))])

                break

            if row>4:

                if temp1==0:
                    row = 1

                temp1 = 1

            else:
                row+=1

    cipherd_text=""
    for jj in b:
        cipherd_text+=jj

    print('In list representation :',b)
    print("the cipher text is:  ",cipherd_text)

def displayMatrix():
    m = 0

    for i in d:
        print(d[i], end="     ")
        m += 1
        if m == 5:
            print("\n")
            m = 0

    if d[55]!='Z':
        print('Something wrong in the matrix')

takingCiphertext()
generateMatrix()
displayMatrix()
Encryption()

