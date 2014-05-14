# -*- coding: cp936 -*-
#从文件中读取数据
transaction = []

def calAllConf(index1,index2):
    m=n=0
    global transaction
    for record in transaction:
        if record[index1]=='1' and record[index2]=='1':
            n += 1
        if record[index1]=='1' or record[index2]=='1':
            m += 1
    if m == 0:
        return 0.0
    return float(n)/float(m)    
    
#读取文件
filename = 'transaction.txt'
f = file(filename)

while True:
    line = f.readline()
    if len(line) == 0:
        break
    record = line.split(',')
    record.pop()
    transaction.append(record)
f.close()

#计算item之间distance的值
size = len(transaction[1])
distance =  [[0 for col in range(size)] for row in range(size)]
for index1 in range(size):
    for index2 in range(size):
        distance[index1][index2] = 1 - calAllConf(index1,index2)
#输出
output = file('distance.txt','w')
for i in distance:
    for j in i:
        output.write(str(j)+' ')
    output.write('\n')
output.close()
print("Finished.")

raw_input()
