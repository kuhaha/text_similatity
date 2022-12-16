"""
Sequence model
"""    
import Levenshtein
def levenshtein_similarity(x, y):
    """ returns the levenshtein similarity between two lists """
    lev_dist = Levenshtein.distance(x, y)
    max_len = max(len(x), len(y))
    return 1 - float(lev_dist / max_len)

"""
Set model 
"""
def jaccard_similarity(x,y):
    """ returns the jaccard similarity between two lists """
    i = len(set.intersection(*[set(x), set(y)]))
    u = len(set.union(*[set(x), set(y)]))
    return i / float(u)

def simpson_coefficient(x, y):
    """ returns the simpson coefficient between two lists """
    i = len(set.intersection(*[set(x), set(y)]))
    m = min(len(set(x)), len(set(y)) )
    return i / float(m)

def simpson_similarity(x, y):
    """ alias to simpson_coefficient(x ,y)  """
    return  simpson_coefficient(x, y)

"""
Transformers
"""

def word_seq(text, filter={}, weighted=False):
    """" transforms text to a sequence of words """"
    pass

def word_bag(text, filter={}, weighted=False):
    """" transforms text to a bag (allowing duplicates) of words """"
    pass

def word_set(text, filter={}, weighted=False):
    """" transforms text to a set (removing duplicates) of words """"
    bag = word_bag(text, filter=filter, wrighted)
    return set(bag)

"""
Scoring
"""

def 

