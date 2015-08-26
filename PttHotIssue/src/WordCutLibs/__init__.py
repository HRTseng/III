import codecs
import jieba
import pytagcloud

dict_path = 'static/dict/dict.big.txt'
user_dict_path = 'static/dict/dict(0701-0715).txt'
stop_word_path = 'static/dict/stopword(0701-0715).txt'

stopwords = None

jieba.set_dictionary(dict_path)
jieba.load_userdict(user_dict_path)
with codecs.open(stop_word_path,'r','utf-8') as f:
    stopwords=f.read() 
    f.close()