# Given a set of closed intervals, find the smallest set of numbers that covers
# all the intervals. If there are multiple smallest sets, return any of them.
# For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of
# numbers that covers all these intervals is {3, 6}.


def findInterval(L):
    assert len(L) >0

    for i in range(len(L)):
        print(L[i])


findInterval([[0, 3], [2, 6], [3, 4], [6, 9]])
