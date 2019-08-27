import csv
import codecs
datas = codecs.open('/mnt/disk0/workspace/Text_Clustet/data/b.txt', 'r',encoding='utf-8')
line = datas.readline()
print(line)
with open('/mnt/disk0/workspace/Text_Clustet/data/c.csv','w+',encoding='utf-8') as csvfile:
#定义一个写变量
	writeCSV = csv.writer(csvfile)
	writeCSV.writerow(line)
line =datas.readline()

