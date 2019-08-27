import codecs
import csv
import codecs
from data_pre import *
words,word_to_id = read_vocab("/mnt/disk0/workspace/Text_Clustet/data/vocab.txt")
file_r = codecs.open("/mnt/disk0/workspace/Text_Clustet/data/vector_word1.txt", 'r', encoding='utf-8')
a = process_file("/mnt/disk0/workspace/Text_Clustet/data/train.txt",word_to_id, max_length=200)
#f1 = open('/mnt/disk0/workspace/Text_Clustet/data/b.txt', 'w+',newline=None,encoding='utf-8')
csvfile =codecs.open('/mnt/disk0/workspace/Text_Clustet/data/Cluster_train.csv','w+',encoding='utf-8')
c = []
data =[]
for j in range(len(a)):
    for i in a[j]:
        for line in file_r:
            items = line[:-1].split(' ')
            word = items[0]
            vec = items[1:]
            if words[i] == word:
                c.append('\t'.join(vec))
                file_r = codecs.open("/mnt/disk0/workspace/Text_Clustet/data/vector_word1.txt", 'r', encoding='utf-8')
                break
    data.append('\t'.join(c)+'\t'+str(j))
    c=[]
    line1 = data[j].split('\t')
    writeCSV = csv.writer(csvfile)
    writeCSV.writerow(line1)
    #f1.write(data[j]+'\r\n')
#f1.close()
