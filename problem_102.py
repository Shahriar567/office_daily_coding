
#Given a list of integers and a number K, return which contiguous elements of the list sum to K.
#For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4].


def problem102(L):
    assert len(L) > 0
    arr = []

    if L[0] + 1 != L[1] and len(L) < 1:
        return arr
    else:
        if L[0] + 1 == L[1]:
            print("it is happening")
            arr.append(L[0])
            return problem102(L[1:])

seq = [1,2,3,4,5]

print(problem102(seq))


