from collections import defaultdict
def foo():
    foo.cnt=vars(foo).setdefault('cnt',-0)
    foo.cnt+=1
    return foo.cnt
dd = defaultdict(foo)
