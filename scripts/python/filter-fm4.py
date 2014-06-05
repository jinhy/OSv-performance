# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
data_file="final/fedora-memcached-t4"
output = open(data_file, 'w')
output.write("#cpu ops tps net_rate\n")
index=[]
value=[]
for i in range(1,6):
    if i !=4:
        continue
    raw=open('result/fedora-'+str(i)).read()
    p_assert = re.compile('cpu.*')
    p_value=re.compile('Run time.*')
    match_assert = p_assert.findall(raw)
    match_value= p_value.findall(raw)
    if len(match_assert)==len(match_value):
        if len(index)==0:
            index=[a.split()[1] for a in match_assert]
            value.append(index)
        value.append([a.split()[4] for a in match_value])
        value.append([a.split()[6] for a in match_value])
        value.append([a.split()[8][:-3] for a in match_value])
    else:
        print "\n\n\n\n"
for j in range(0,len(value[0])):
    for i in range(0,len(value)):
        output.write(str(value[i][j])+' ')
    output.write('\n')
