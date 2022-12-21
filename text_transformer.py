"""
Transformers
"""

def word_seq(text, parser=None, weighted=False):
    """ transforms text to a sequence of words """
    
    if parser is None:
        return text.split()
    
    if type(parser) is str:
        return text.split(sep=parser)
   
    return parser(text)
    

def word_bag(text, weighted=False):
    """ transforms text to a bag (allowing duplicates) of words """
    pass

def word_set(text, weighted=False):
    """ transforms text to a set (removing duplicates) of words """
    bag = word_bag(text,weighted=weighted)
    return set(bag)

    
