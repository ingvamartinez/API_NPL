"""
Importamos las liberias necesarias para vectorizar
el texto
"""
import os
import re
import pickle
from sklearn.feature_extraction.text import HashingVectorizer

cur_dir:str=os.path.dirname(__file__)

stop=pickle.load(open(os.path.join(cur_dir,'pkl_objects','stopwords.pkl'),'rb'))

def tokenizer(text):
    """
    Se crea la funcion que tokenizara por medio de la funcion split
    """
    text = re.sub('<[^>]*>','',text)
    emo = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)',text.lower())
    text = re.sub('[\W]+',' ',text.lower())+' '.join(emo).replace('-','')
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized

vect:HashingVectorizer = HashingVectorizer(decode_error='ignore',
                                           n_features=2**21,
                                           preprocessor=None,
                                           tokenizer=tokenizer)
