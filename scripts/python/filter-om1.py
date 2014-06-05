# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
data_file="final/osv-memcached-1"
output = open(data_file, 'w')
output.write("#cpu ops tps net_rate\n")
index=[1,2,4,6,8,10,12,14,16]
value=[]
for i in range(1,6):
    raw=open('result/memcached-osv-t1-'+str(i)).read()
    p_value=re.compile('Run time.*')
    match_value= p_value.findall(raw)
    if len(match_value)>0:
        if len(value)==0:
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
