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
    """ Find length of the longest common sub-sequence between `a` , `b`
    """
    m, n = len(a), len(b)
    c = np.zeros((m + 1, n + 1), dtype=int)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
    return c[-1][-1]

def lcs_seq(a, b):
    s = ""
    i, j = len(a), len(b)
    while i > 0 and j > 0:
        if a[i-1] == b[j-1]:
            s = a[i-1] + s
            i, j = i-1, j-1
        elif c[i-1][j] >= c[i][j-1]:
            i -= 1
        else:
            j -= 1
    return s

def lcs_strlen(a, b):
     """ Finding length of longest common substring of a[0..m-1] and b[0..n-1]
         Create a table to store lengths of longest common suffixes of substrings.
         Note that LCSuff[i][j] contains the length of longest common suffix of
         a[0...i-1] and a[0...j-1]. 
    """
    m, n = len(a), len(b)
    
    # `c` is the table with zero value initially in each cell    
    c = np.zeros((m + 1, n + 1), dtype=int)
    result = 0
    # Following steps to build LCSuff[m+1][n+1] in bottom up fashion
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

def lcs_str_size(a,b):
    match = SequenceMatcher(None, a, b).find_longest_match()
    return match.size

def lcs_str(a,b):
    match = SequenceMatcher(None, a, b, autojunk=False).find_longest_match()
    return a[match.a:match.a+match.size]