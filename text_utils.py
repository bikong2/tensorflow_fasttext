# -*- coding: utf-8 -*-
# @author: lixihua9@126.com

from nltk.tokenize import word_tokenize


# 英文分词
def TokenizeText(text):
    return word_tokenize(text.lower())


# --ngrams=2,3,4        
def ParseNgramsOpts(opts):
    ngrams = [int(g) for g in opts.split(',')]
    ngrams = [g for g in ngrams if (g > 1 and g < 7)]
    return ngrams


# ngrams = [2, 3, 4]
# words = [我 是 中 国 人]
# nglist = [我是 是中 中国 国人 我是中 是中国 中国人 我是中国 是中国人]
def GenerateNgrams(words, ngrams):
    nglist = []
    for ng in ngrams:
        for word in words:
            nglist.extend([word[n:n+ng] for n in range(len(word)-ng+1)])
    return nglist
