# -*- coding: cp936 -*-
#���ļ��ж�ȡ����
filename = 'transaction.txt'
f = file(filename)
transaction = []
while True:
    line = f.readline()
    if len(line) == 0:
        break
    record = line.split(' ')
    transaction.append(line)
f.close()


raw_input()
