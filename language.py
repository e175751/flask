import janome
import codecs
from janome.tokenizer import Tokenizer
import collections
import re

class language:
    def __init__(self,sentence):
        self.sentence = sentence

    def lang_Preparation(self):
        # CorpusElementのリスト
        naive_corpus = []
        naive_tokenizer = Tokenizer()

        tokens = naive_tokenizer.tokenize(self.sentence)
        element = CorpusElement(self.sentence, tokens)
        naive_corpus.append(element)
        return naive_corpus

    def load_pn_dict(self):
        dic = {}
        key = []
        value = []

        with codecs.open('./data_lang/pn_ja.dic', 'r') as f:
            lines = f.readlines()

            for line in lines:
                columns = line.split(':')
                count=0
                for i in columns:
                    if(count==0):
                        key.append(i)
                        count+=1
                    elif(count==3):
                        value.append(i.rstrip('\n'))
                        count=0
                    else:
                        count+=1

        dic = dict(zip(key, value))    
        return dic

    # トークンリストから極性値リストを得る
    def get_pn_scores(self,tokens, pn_dic):
        scores = []
        
        for surface in [t.surface for t in tokens if t.part_of_speech.split(',')[0] in ['動詞','名詞', '形容詞', '副詞']]:
            if surface in pn_dic:
                scores.append(pn_dic[surface])
            
        return scores

    def run(self):
        naive_corpus = self.lang_Preparation()
        pn_dic = self.load_pn_dict()

        for element in naive_corpus:
            element.pn_score = self.get_pn_scores(element.tokens, pn_dic)
            
        score = 0.0
        list=[]
        for i in element.pn_score:
            list.append(float(i))
            
        if(len(list)==0):
            pass
        else:
            score = sum(list)/len(list)
        return score

class CorpusElement:
    def __init__(self, text='', tokens=[], pn_scores=[]):
        self.text = text # テキスト本文
        self.tokens = tokens # 構文木解析されたトークンのリスト
        self.pn_scores = pn_scores # 感情極性値(後述)
