# Sonali Katakdhond RN. 43 BE-A CSE

def Trans_Tech_one(text, key):
    railFence = [['\n' for i in range(len(text))]
            for j in range(key)]

    down = False
    r, c = 0, 0

    for i in range(len(text)):

        if (r == 0) or (r == key - 1):
            down = not down

        railFence[r][c] = text[i]
        c += 1

        if down:
            r += 1
        else:
            r -= 1
    result = []
    for i in range(key):
        for j in range(len(text)):
            if railFence[i][j] != '\n':
                result.append(railFence[i][j])
    return ("".join(result))


if __name__ == "__main__":

    plain_text = input('Enter plain text :')
    key = int(input('Enter Key :'))


    print("Cipher Text : ",Trans_Tech_one(plain_text, key))
