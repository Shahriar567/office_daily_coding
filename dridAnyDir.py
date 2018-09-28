
#You are in an infinite 2D grid where you can move in any of the 8 directions:
#(x,y) to
#  (x+1, y),
#  (x - 1, y),
#  (x, y+1),
#  (x, y-1),
#  (x-1, y-1),
#  (x+1,y+1),
#  (x-1,y+1),
#  (x+1,y-1)
#You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.
#Example:


def anyGrid(seq):
    x1, y1 = seq[0]
    x2, y2 = seq[1]
    count = 0
    if (abs(x1-x2) > 1 or abs(y1-y2) > 1 or abs(x1-y2) > 1 or abs(x2-y1) > 2):
        #print("Sorry do you want me to jump ?")
        return 0 
    elif len(seq) == 2:
        #print(" This is the end count. ",count)
        return count + 1 
    else:
        #print("this is the going count", count)
        count = 1 + anyGrid(seq[1:])
        return count


print(anyGrid([(0,0),(0,1),(1,1),(2,2),(2,3),(3,3)]))

seq = [(1,2),(1,3),(2,3),(3,3)]
#print(len(seq))
