"""
Scoring Functions
"""
class Scorer:
    def __init__(self):
        pass
    
    def count_score(self, data, cutoff=0.5):
        """ Computes a score from 1-d list `data`, 
         Each element in the list is a tuple of (i, j, lower_level_score)  
        """
        if data == []:
            return 0.0
        targets = [d[2] for d in data if d[2] > cutoff]
        return len(targets) / float(len(data))
    
    def max_score(self, data, cutoff=0.5):
        targets = [d[2] for d in data if d[2] > cutoff] + [0.0]
        return max(targets)
    
    def avg_score(self, data, cutoff=0.5):
        if data == []:
            return 0.0
        targets = [d[2] for d in data if d[2] > cutoff]
        return sum(targets)/float(len(data)) 
    

def score(data, scorer='count', cutoff=0.5):
    """ common interface for calling a scoring function by name (`scorer`)   
    """
    func = getattr(Scorer(), f'{scorer}_score')
    return func(data, cutoff=cutoff)
