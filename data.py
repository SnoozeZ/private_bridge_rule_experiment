# -*- coding: cp936 -*-
#���ļ��ж�ȡ����
filename = 'forestfires.csv'
f = file(filename)
strlistlist = []
output = []
while True:
    line = f.readline()
    if len(line) == 0:
        break
    strlist = line.split(',')
    print strlist
    strlistlist.append(strlist)
f.close()
print "���"
print strlistlist

for strlist in strlistlist:
    if strlist[0] == 'X':
        continue
    strtemp = [0]*82
    #first
    strtemp[int(strlist[0])-1] = 1;
    #second
    strtemp[int(strlist[1])-1+9] = 1;
    #third
    month =['jan','feb','mar','apr','may','jun']
    
    print strtemp

    
raw_input()
