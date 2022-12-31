"""
Transformers
"""
import MeCab
from janome.tokenizer import Tokenizer

def para_seq(doc, sep=None, limit=10):
    """ transforms `doc` to a sequence of paragraphs 
    """
    if sep is None:
        lines = doc.splitlines()
    else:
        lines = doc.split(sep)
   
    lines = [p.strip() for p in lines if len(p.strip())>limit]
    return lines

def sent_seq(text, sep=None, limit=5):
    """ transforms `text` to a sequence of sentences
       (replace all separators to newlines the call `para_seq()`)
    """
    if sep is None:
        sep = ['.', '?', '!', '。', '？', '！']
    if type(sep) is not list:
        sep = [sep]
    for sp in sep:
        text =  text.replace(sp, "\n")
    
    return para_seq(text, limit=limit)
    

def word_seq(text, parser=None):
    """ transforms `text` to a sequence of words
      e.g. 'hello, world' => ['hello','world']
         　'吾輩は猫である'=>['吾輩','は','猫','で','ある']
        (parser='mecab' or parser='janome' created by `create_parser`)
      
    """
    
    if parser is None:
        return text.split()
    
    if type(parser) is str:
        return text.split(sep=parser)
   
    return parser(text)

def create_parser(worker='janome', parts_of_speech=['名詞'], stop_words=[]):
    """ parser factory generates parser 
      @parms: `parts_of_speech`, `stop_word`
    """
    def _mecab(text):
        """ mecab parser
        """
        tagger = MeCab.Tagger()
        node = tagger.parseToNode(text)
        rs = []
        while node:
            word = node.surface
            if node.feature.split(",")[0] == u"動詞": 
                 word = node.feature.split(",")[6]
                    
            hinshi = node.feature.split(",")[0]
            if hinshi in parts_of_speech and word not in stop_words:
                rs += [word]

            node = node.next
            
        return rs
    

    def _janome(text):
        """ janome parser [default]
        """
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
    
