import random
import numpy as np

def list():
    Sub=[['HP_', [209,239,269,299]],['HP%', [4.1,4.7,5.3,5.8]],['ATK_', [14, 16,18,19]],['ATK%', [4.1,4.7,5.3,5.8]],['DEF_', [16, 19,21,23]],['DEF%', [5.1,5.8,6.6,7.3]],['EM', [16, 19,21,23]],['ER%', [4.5,5.2,5.8,6.5]],['CR%', [2.7,3.1,3.5,3.9]],['CD%', [5.4,6.2,7.0,7.8]]]
    return Sub

new=random.sample(list(),4)
new.sort()
# add the first roll in each
for a in new:
    a[1].clear()
for x in new:
    for q in list():
        if np.array_equal(x[0],q[0]) == True:
            x[1].append(q[1][3])
# add five roll randomly
c=0
while c<5:
    b=new[random.randint(0,3)]
    for z in list():
        if np.array_equal(b[0],z[0]) == True:
            b[1].append(z[1][random.randrange(4)])
            c+=1

print(new)
