import codecs

from data_pre import *
from config import TCNNConfig
import os
#contens,label = read_file("/mnt/disk0/workspace/Text_Clustet/data/train.txt")
import sys
import jieba.posseg as pseg
config = TCNNConfig("/mnt/disk0/workspace/Text_Clustet/data")
build_vocab(config.train_dir, config.vocab_dir, 120000)
words, word_to_id = read_vocab(config.vocab_dir)

'''
train_contents = open("/mnt/disk0/workspace/Text_Clustet/data/contents1.txt",'r',encoding="utf-8")
train_lines = train_contents.read().split('\n')
train = []
num = 0
for line in train_lines:
    num += 1
    if num%1000 == 0:
        print (num)
    words = pseg.cut(line)
    line0 = []
    for w in words:
        if 'x' != w.flag:
            line0.append(w.word)
    train.append(' '.join(line0))
f1 = open('/mnt/disk0/workspace/Text_Clustet/data/vector_word100', 'w',encoding='utf-8')
f1.write('\n'.join(train))
f1.close()
'''
x_train = process_file(config.train_dir, config.word_to_id, 200)