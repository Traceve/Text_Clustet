from data_pre import *
#contens,label = read_file("/mnt/disk0/workspace/Text_Clustet/data/train.txt")
#build_vocab("/mnt/disk0/workspace/Text_Clustet/data/train.txt", "/mnt/disk0/workspace/Text_Clustet/data/vocab.txt", 120000)
import sys
import jieba.posseg as pseg
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