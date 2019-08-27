#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import re
import time


from gensim.models import Word2Vec

import jieba

stoplist = {}.fromkeys([line.strip() for line in open("/mnt/disk0/workspace/Text_Clustet/data/stopwords.txt","rb")])
class Get_Sentences(object):
    def __init__(self, file_names):
        self.filenames = file_names

    def __iter__(self):
        for file_name in self.filenames:
            index = 1
            with open(file_name, 'r',encoding="utf-8") as f:
                for line in f:
                    print(str(index) + ' ' + line[0:20])
                    index += 1
                    yield [word for word in (jieba.lcut(re.sub('[\d ×()]', '', line))) if word not in stoplist]


def train_word2vec(train_dir,vector_word_filename):
    print('Train Word2Vec...')
    t1 = time.time()
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = Get_Sentences([train_dir])
    model = Word2Vec(sentences, sg=1, hs=1, min_count=1, window=3, size=200, workers=4, iter=2)
    model.wv.save_word2vec_format(vector_word_filename, binary=False)
    print('-------------------------------------------')
    print("Training word2vec model cost %.3f seconds...\n" % (time.time() - t1))



if __name__ == '__main__':
    train_word2vec("/mnt/disk0/workspace/Text_Clustet/data/contents1.txt","/mnt/disk0/workspace/Text_Clustet/data/vector_word.txt")