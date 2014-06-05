# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
data_file="final/fedora-haproxy-2"
output = open(data_file, 'w')
output.write("#cpu 1 5 10 20 50 100 200 500\n")
index=[]
value=[]
co=[1,5,10,20,50,100,200,500]
for i in range(1,2):
    if i ==3:
        continue
    raw=open('result/fedora-haproxy-'+str(i)).read()
    p_assert = re.compile('cpu.*')
    p_value=re.compile('cpu.*?upc',re.DOTALL)
    match_assert = p_assert.findall(raw)
    match_value= p_value.findall(raw)
    if len(match_assert)==len(match_value):
        if len(index)==0:
            index=[a.split()[1] for a in match_assert]
        id=0
        for h in [a for a in match_value]:
            p_v=re.compile('Requests.*');
            vs=p_v.findall(h)
            vs=[a.split()[3] for a in vs]
            vs.insert(0,index[id])
            value.append(vs)
            id=id+1
    else:
        print "error"
for v in value:
    for i in v:
        output.write(str(float(i)-500)+' ')
    output.write('\n')
