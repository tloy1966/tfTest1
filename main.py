from sqlTest import *
from regTest import *
#s = sqlTest();
#testSql();
data = getDate();
y = [];
x = [];
for i in data:
    ty = [None]*1
    ty[0] = i[0];
    y.append(ty);
    tx = [None]*2;
    tx[0] = i[0] *0.001;
    tx[1] = i[0]+1*10;
    #t.append(i[6]);
    x.append(tx);

t2 = anaData(x,y);
