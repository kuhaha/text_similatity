import numpy as np

"""
Sequence Model
"""
import Levenshtein

def levenshtein_similarity(x, y):
    """ returns the levenshtein similarity between two sequences 
    
    """
    lev_dist = Levenshtein.distance(x, y)
    max_len = max(len(x), len(y))
    return 1 - float(lev_dist / max_len)


"""
Set Model 
"""

def jaccard_similarity(x,y):
    """ returns the jaccard similarity between two lists 
    
    """
    i = len(set.intersection(*[set(x), set(y)]))
    u = len(set.union(*[set(x), set(y)]))
    return i / float(u)


def simpson_coefficient(x, y):
    """ returns the simpson coefficient between two lists 
    
    """    
    i = len(set.intersection(*[set(x), set(y)]))
    m = min(len(set(x)), len(set(y)) )
    return i / float(m)


def simpson_similarity(x, y):
    """ alias to simpson_coefficient(x ,y)  
    
    """
    return  simpson_coefficient(x, y)



def lcs_seqlen(a, b):
    """ Dynamic programming algorithm for finding 
        length of the longest common sub-sequence  of a[0..m-1] and b[0..n-1]
    """
    m, n = len(a), len(b)
    # `c` is the (m+1)x(n+1) table with zero value initially in each cell    
    c = np.zeros((m + 1, n + 1), dtype=int)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
    return c[-1][-1]

def lcs_seq(a, b):
    s = []
    m, n = len(a), len(b)
    c = np.zeros((m + 1, n + 1), dtype=int)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
                
    i, j = m, n            
    while i > 0 and j > 0:
#         print(f'a:{a[i-1]}, b:{b[j-1]}')
        if a[i-1] == b[j-1]:
            s = [a[i-1]] + s
            i, j = i-1, j-1
        elif c[i-1][j] >= c[i][j-1]:
            i -= 1
        else:
            j -= 1
    s = ''.join(s) if type(a) is str else s
    s = tuple(s) if type(a) is tuple else s
    return s

def lcs_strlen1(a, b):
    """Dynamic programming algorithm for finding
        length of longest common substring of a[0..m-1] and b[0..n-1]
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
    return result

"""
use difflib: builtin functions for comparing sequences
cf.  https://docs.python.org/3/library/difflib.html
"""
from difflib import SequenceMatcher

def lcs_strlen(a,b):
    match = SequenceMatcher(None, a, b).find_longest_match()
    return match.size

def lcs_str(a,b):
    match = SequenceMatcher(None, a, b, autojunk=False).find_longest_match()
    return a[match.a:match.a+match.size]

