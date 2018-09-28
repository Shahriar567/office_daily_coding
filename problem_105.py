

#Given a function f, and N return a debounced f of N milliseconds.
#That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.


import time
from threading import Thread

def helperFunc():
    print("I am a helper function. Please let me help")



def funct(N):
    time.sleep(N)
    thread  = Thread(target = helperFunc, args = ())
    thread.start()


funct(10)

