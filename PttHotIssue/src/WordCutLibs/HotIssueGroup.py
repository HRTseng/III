#-*- encoding: utf-8 -*-
'''
Created on 2015年7月28日

@author: Cymon Dez
'''
import jieba

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import linear_kernel
import WordCutLibs

related_dict = {}

def get_related_news(articles ,base_art_index):
    
    if related_dict.get(base_art_index) is not None :
        return related_dict.get(base_art_index)
    
    corpus = []
    for art in articles :
        corpus.append( ' '.join( jieba.cut(art.context) ) )
    ls = [w for w in  WordCutLibs.stopwords.split('\n')]
    vectorizer = CountVectorizer(stop_words=ls)
    X = vectorizer.fit_transform(corpus)
    #word = vectorizer.get_feature_names()
    #stopword = vectorizer.get_stop_words()
    
    
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(X)
    #weight = tfidf.toarray()
    
    target = base_art_index #設定目標標題     #index順序同SQL
    
    
    cosine_similarities = linear_kernel(tfidf[target], tfidf).flatten().argsort()
    
    max_len = len(cosine_similarities)
    bnd = -11 if max_len >= 10 else -(max_len)
    related_docs_indices = cosine_similarities[: bnd:-1]
    
    res = [ articles[idx] for idx in related_docs_indices ]
    related_dict[base_art_index] = res
    return res
    