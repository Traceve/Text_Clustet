from collections import Counter

import jieba
import re
from gensim.models import Word2Vec
import numpy as np
import codecs
import tensorflow.contrib.keras as kr
import sys
import jieba.posseg as pseg

def open_file(filename, mode='r'):
    return open(filename, mode, encoding='utf-8', errors='ignore')#以UTF-8的格式代开文件并返回
def read_file(filename):
    contents, labels = [], []
    with open_file(filename) as f:
        for line in f:
            try:
                label, content1,content2 = line.strip().split('\t')
                if content1 and content2:
                    contents.append(jieba.lcut(content1,content2))
                    labels.append(label)
            except:
                pass
    return contents, labels
def build_vocab(train_dir, vocab_dir, vocab_size=50000):
    """根据训练集构建词汇表，存储"""
    data_train, _ = read_file(train_dir)

    all_data = []
    for content in data_train:
        all_data.extend(content)

    counter = Counter(all_data)
    count_pairs = counter.most_common(vocab_size - 1)
    words, _ = list(zip(*count_pairs))
    # 添加一个 <PAD> 来将所有文本pad为同一长度
    words = ['<PAD>'] + list(words)
    open_file(vocab_dir, mode='w').write('\n'.join(words) + '\n')
def read_vocab(vocab_dir):
    """读取词汇表"""
    # words = open_file(vocab_dir).read().strip().split('\n')
    with open_file(vocab_dir) as fp:
        # 如果是py2 则每个值都转化为unicode
        words = [_.strip() for _ in fp.readlines()]
    word_to_id = dict(zip(words, range(len(words))))
    return words, word_to_id

#f = open_file("/mnt/disk0/workspace/Text_Clustet/data/train.txt", "r")
contents, labels = read_file("/mnt/disk0/workspace/Text_Clustet/data/train.txt")
build_vocab("/mnt/disk0/workspace/Text_Clustet/data/train.txt", "/mnt/disk0/workspace/Text_Clustet/data/vocab.txt", 50000)
#words, word_to_id = read_vocab("E:/Machine Learning/vocab.txt")
'''
vocab_size = len(words)
vocab = word_to_id

file_r = codecs.open("E:/Machine Learning/vector_word.txt", 'r', encoding='utf-8')
line = file_r.readline()
voc_size, vec_dim = map(int, line.split(' '))
embeddings = np.zeros([len(vocab), vec_dim])
line = file_r.readline()
while line:
    items = line.split(' ')
    word = items[0]
    vec = np.asarray(items[1:], dtype='float32')
    if word in vocab:
        word_idx = vocab[word]
        embeddings[word_idx] = np.asarray(vec)
    line = file_r.readline()
np.savez_compressed(config.vector_word_npz, embeddings=embeddings)
'''