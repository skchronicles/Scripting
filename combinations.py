from __future__ import generators

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc

def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss

def xpermutations(items):
    return xcombinations(items, len(items))

if __name__=="__main__":
    print "Permutations of 'love'"
    for p in xpermutations(['l','o','v','e']): print ''.join(p)

    print
    print "Combinations of 2 letters from 'love'"
    for c in xcombinations(['l','o','v','e'],2): print ''.join(c)

    print
    print "Unique Combinations of 2 letters from 'love'"
    for i in range(6):
        for uc in xuniqueCombinations(['a','b','c','d','e'],i): print ''.join(uc)

    print
    print "Selections of 2 letters from 'love'"
    for s in xselections(['l','o','v','e'],2): print ''.join(s)

    print
    print map(''.join, list(xpermutations('done')))
