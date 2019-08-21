from data_pre import *
contents, labels = [], []#定义两个空列表
with open_file("/mnt/disk0/workspace/Text_Clustet/data/train.txt",'r') as f:
    for line in f:
        print(line)
        try:
            label, content = line.strip().split('\t')# 移除每行头尾空格或换行符，然后根据tab把label和content分到list里
            if content:
                contents.append(content)
                labels.append(label)
        except:
            pass
all_data = []#定义个空的集合

f = open(r'/mnt/disk0/workspace/Text_Clustet/data/contents1.txt','w',encoding='utf-8')
#f = open(r'E:/Machine Learning/small/train88888.txt','w',encoding='utf-8-sig')
#f.write('\n'.join(labels))
f.write('\n'.join(contents))
f.close()