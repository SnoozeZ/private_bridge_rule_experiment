# -*- coding: cp936 -*-
#从文件中读取数据
filename = 'forestfires - 副本.csv'
f = file(filename)
strlistlist = []
transaction = []
while True:
    line = f.readline()
    if len(line) == 0:
        break
    strlist = line.split(',')
    strlistlist.append(strlist)
f.close()

for strlist in strlistlist:
    if strlist[0] == 'X':
        continue
    strtemp = [0]*81
    #first
    strtemp[int(strlist[0])-1] = 1
    #second
    strtemp[9+int(strlist[1])-2] = 1
    #third
    month =['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    strtemp[17+month.index(strlist[2])] = 1
    #forth 
    day = ['mon','tue','wed','thu','fri','sat','sun']
    strtemp[29+day.index(strlist[3])] = 1
    #fifth 7.8
    a = int((float(strlist[4])-18.7)/15.6)
    strtemp[36+a] = 1
    #sixth 29.1
    a = int((float(strlist[5])-1.1)/58.2)
    strtemp[41+a] = 1
    #seventh 85.3
    a = int((float(strlist[6])-7.9)/170.6)
    strtemp[46+a] = 1
    #eighth 5.65
    a = int((float(strlist[7])-0)/11.3)
    strtemp[51+a] = 1
    #ninth 3.14
    a = int((float(strlist[8])-2.2)/6.28)
    strtemp[56+a] = 1
    #tenth 3.14
    a = int((float(strlist[9])-15)/17.04)
    strtemp[61+a] = 1
    #11th 3.14
    a = int((float(strlist[10])-0.4)/1.804)
    strtemp[66+a] = 1
    #12th 3.14
    a = int((float(strlist[11])-0.0)/1.2804)
    strtemp[71+a] = 1
    #13th 3.14
    a = int((float(strlist[12])-0.0)/218.18)
    strtemp[76+a] = 1
    
    transaction.append(strtemp)
#把transaction记录输出
output = file('transaction.txt','w')
for record in transaction:
    for item in record:
        output.write(str(item)+' ')
    output.write('\n')
output.close()
    
raw_input()
