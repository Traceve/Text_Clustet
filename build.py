import re
import codecs
from data_pre import *
words,word_to_id = read_vocab("/mnt/disk0/workspace/Text_Clustet/data/vocab.txt")
a = process_file("/mnt/disk0/workspace/Text_Clustet/data/train1.txt",word_to_id, max_length=200)
print(a)
c=[]
'''
embeddings1 = np.zeros([len(a),len(a[0])*200])
#def em(a,word_to_id):
embeddings= cc()
b=np.zeros([1,len(a[0])*200])
print(len(b))
print(b)
c=[]
for i in range(len(a)):
    j = 0
    while j < 200 :
        print("qqqqqqqqqqqqqqqqqqq")
        if a[i][j] in word_to_id.values():
            #print(embeddings[a[i][j]])
            b += embeddings[a[i][j]]
            print(b)
        #j+=1
    #print("fffffffffffffffffffff")
    #c.append(b)
    #return c
        #print(c)
    #f1 = open('/mnt/disk0/workspace/Text_Clustet/data/b.txt', 'w',encoding='utf-8')
    #f1.write('\n'+ c)
    #f1.close()
#d = em(a,word_to_id)
#print("efwewewe")
#np.savez_compressed("/mnt/disk0/workspace/Text_Clustet/data/b.txt", d)
'''



#print(len(a))
#np.savetxt("/mnt/disk0/workspace/Text_Clustet/data/a.txt", a)


'''
    for w in line:
        if 'x' != w.flag:
            line0.append(w.word)
    train.append(' '.join(line0))
f1 = open('/mnt/disk0/workspace/Text_Clustet/data/vector_word100', 'w',encoding='utf-8')
f1.write('\n'.join(train))
f1.close()
'''