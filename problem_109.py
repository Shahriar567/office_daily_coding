
#Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.
#For example, 10101010 should be 01010101. 11100010 should be 11010001.


def swapBits(aL):
#    assert len(L) == 8
    L = list(map(int, aL))

    for i in range(0,len(L), 2):
        temp = L[i]
        L[i] = L[i+1]
        L[i+1] = temp
   
    L = map(str, L)
    return "".join(L)


print(swapBits("11100010"))

