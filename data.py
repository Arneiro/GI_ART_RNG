import random

art_sub=[
    ['HP_', 209,239,269,299],
    ['HP%', 4.1,4.7,5.3,5.8],
    ['ATK_',14, 16,18,19],
    ['ATK%',4.1,4.7,5.3,5.8],
    ['DEF_',16, 19,21,23],
    ['DEF%',5.1,5.8,6.6,7.3],
    ['EM',  16, 19,21,23],
    ['ER',  4.5,5.2,5.8,6.5],
    ['CR',  2.7,3.1,3.5,3.9],
    ['CD',  5.4,6.2,7.0,7.8]
]

for x in random.sample(art_sub,4):
    z=len(x)-1

    while z < len(x):
        z+=1

        print(x)



