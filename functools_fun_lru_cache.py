import time
from functools import lru_cache
def time_it(f):
     def inner(*args, **kwargs):
         s = time.time()
         ret = f(*args, **kwargs)
         e = time.time()
         print(args[0],end='--> ')
         print('%0.20f' % (e-s))
         return ret
     return inner


@lru_cache(maxsize=None)
def fibo(x):
    if x<2:
        return x
    return fibo(x-1) + fibo(x-2)

#print(fibo(100))

#print("*"*100)
#print(fibo(100))

@lru_cache(maxsize=None)
def foo(x):
    print("Start")
    time.sleep(3)
    print("end")
    return x

print(foo(1))
print(foo(2))
print(foo(1))
