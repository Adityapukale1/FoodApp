plane_text = input('Enter your msg here :\n').replace(" ","")
fp=""
sp=""

for i in range(len(plane_text)):
    if i%2==0:
        fp += plane_text[i]
    else:
        sp += plane_text[i]


print('The encrypted text is : '+fp+sp)