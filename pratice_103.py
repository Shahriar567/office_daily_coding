
def repeatString(aStr, cStr):
    if len(aStr) < len(cStr): 
        return null

    my_dic = {}
    for i in aStr:
        if i in cStr:
            print(i)


repeatString("abcdefg","abc")

