


# Pratice with yeild. 


def pYeild():
    yield 1
    yield 2
    yield 3



def getPrimes(n):
    i = 2
    while i < n :
        prime = True # reset the `prime` variable before the inner loop
        for a in xrange(2, i):
            if i%a == 0:
                prime = False
                break
        if prime:
            yield i
        i += 1 # don't forget to advance `i`


for item in getPrimes(10):
    print item



