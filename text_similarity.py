import numpy as np

"""
Sequence Model
"""
import Levenshtein

def levenshtein_similarity(x, y):
    """ returns the levenshtein similarity between sequences `x` and `y`
    
    """
    lev_dist = Levenshtein.distance(x, y)
    max_len = max(len(x), len(y))
    return 1 - float(lev_dist / max_len)


"""
Set Model 
"""

def jaccard_similarity(x,y):
    """ returns the jaccard similarity between `x` and `y`
    
    """
    n = len(set.intersection(*[set(x), set(y)]))
    u = len(set.union(*[set(x), set(y)]))
    return n / float(u)


def simpson_similarity(x, y):
    """ returns the simpson coefficient between `x` and `y` 
    
    """    
    n = len(set.intersection(*[set(x), set(y)]))
    m = min(len(set(x)), len(set(y)) )
    return n / float(m)

"""
Bag Model
"""

"""
Structural Similarity:
 Similarity of structures based on pair-wise similarities of the lower-level elements

"""

# Set 
def set_similarity(a, b):
    pass

# Sequence  
def seq_similarity(a, b):
    pass


""" 
LCSeq: Longest Common Subsequence
 where elements are not necessarily consecutive 

Local implementation using dynamic programming
"""

def LCSeq(a, b, sizeOnly=True):
    """ Finding the longest common subsequence of a[0..m-1] and b[0..n-1]
    """

    m, n = len(a), len(b)
    c = np.zeros((m + 1, n + 1), dtype=int)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
    if sizeOnly:
        return c[-1][-1]
    
    s = []
    i, j = m, n            
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            s = [a[i-1]] + s
            i, j = i-1, j-1
        elif c[i-1][j] >= c[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    #  transform return type the that of parameter `a`        
    s = ''.join(s) if type(a) is str else s
    s = tuple(s) if type(a) is tuple else s
    return s


"""
LCStr: Longest Common Substring
  where elements must be consecutive 

use difflib: builtin functions for comparing sequences
cf.  https://docs.python.org/3/library/difflib.html
"""
from difflib import SequenceMatcher

def LCStr(a, b, sizeOnly=True):
    match = SequenceMatcher(None, a, b).find_longest_match()
    if sizeOnly:
        return match.size
    else:
        return a[match.a: match.a + match.size]

""" 
 Local implementation using dynamic programming
"""
def LCStr2(a, b, sizeOnly=True):
    """ Finding length of longest common substring of a[0..m-1] and b[0..n-1]
    """
    m, n = len(a), len(b)      
    # `c` is the (m+1)x(n+1) table with zero value initially in each cell    
    c = np.zeros((m + 1, n + 1), dtype=int)
    result = 0
    # Following steps to build c[m+1][n+1] in bottom up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if (a[i-1] == b[j-1]):
                c[i][j] = c[i-1][j-1] + 1
                result = max(result, c[i][j])
            else:
                c[i][j] = 0
    if sizeOnly:
        return result

    s = []
    i, j = m, n            
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            s = [a[i-1]] + s
            i, j = i-1, j-1
        elif c[i-1][j] >= c[i][j-1]:
            i -= 1
        else:
            j -= 1
    #  transform return type the that of parameter `a`        
    s = ''.join(s) if type(a) is str else s
    s = tuple(s) if type(a) is tuple else s
    return s