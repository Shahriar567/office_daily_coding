

# Make a heap min tree

class BinHeap:
    def __init__(self):
        self.heaplist=[0]
        self.size = 0

    def insert(self, i):
        self.heaplist.append(i)
        self.size += 1
        self.perUp(self.size)

    def perUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i//2]:
                temp = self.heaplist[i//2]
                self.heaplist[i//2] = self.heaplist[i]
                self.heaplist[i] = temp

            i = i //2

    def remove(self):
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.size -= 1
        self.heaplist.pop()
        self.percDown(1)
        return retval


    def percDown(self,i):
        while (i * 2) <= self.size:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heaplist[i*2] < self.heaplist[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.heaplist = [0] + alist[:]
        print(self.heaplist)
        while (i > 0):
            self.percDown(i)
            i = i - 1



bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.remove())
print(bh.remove())
print(bh.remove())
print(bh.remove())
print(bh.remove())
