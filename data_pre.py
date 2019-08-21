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
    """读取文件数据"""
    contents, labels = [], []
    with open_file(filename) as f:
        for line in f:
            try:
                label, content = line.strip().split('\t')
                if content:
                    contents.append(jieba.lcut(content))
                    labels.append(label)
            except:
                pass
    return contents, labels
def build_vocab(train_dir, vocab_dir, vocab_size=120000):
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
    with open_file(vocab_dir) as fp:
        # 如果是py2 则每个值都转化为unicode
        words = [_.strip() for _ in fp.readlines()]
    word_to_id = dict(zip(words, range(len(words))))
    return words, word_to_id
def process_file(filename, word_to_id, cat_to_id, max_length=200):
    """将文件转换为id表示"""
    contents, labels = read_file(filename)
    data_id, label_id = [], []
    for i in range(len(contents)):
        data_id.append([word_to_id[x] for x in contents[i] if x in word_to_id])
        label_id.append(cat_to_id[labels[i]])

