"""
Transformers
"""
import MeCab
from janome.tokenizer import Tokenizer

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

def create_parser(worker='janome', parts_of_speech=['名詞'], stop_words=[]):
    """ mecab parser
    """
    def _mecab(text):
        tagger = MeCab.Tagger()
        node = tagger.parseToNode(text)
        rs = []
        while node:
            word = node.surface
            if node.feature.split(",")[0] == u"動詞": 
                 word=node.feature.split(",")[6]
                    
            hinshi = node.feature.split(",")[0]
            if hinshi in parts_of_speech and word not in stop_words:
                rs += [word]

            node = node.next
            
        return rs
    
    """ janome parser [default]
    """
    def _janome(text):
        t = Tokenizer()
        rs = []
        for token in t.tokenize(text):
            word = token.base_form
            hinshi = token.part_of_speech.split(',')[0]
            if hinshi in parts_of_speech and word not in stop_words:
                rs += [word]
    
        return rs
    if worker == 'mecab':
        return _mecab
    else:
        return _janome
    
