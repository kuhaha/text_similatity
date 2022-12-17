"""
Scoring
"""
import numpy as np
class Scorer:
    def __init__(self, cutoff=0.5):
        self.cutoff = cutoff
        
    def count_score(self, data):
        """ count based scoring for 2-d list `data` """
        count = lambda x : sum([len(s) for s in x])
        m = count(data)
        p = count([[x for x in a if x>self.cutoff] for a in data])
        return p / float(m)       

