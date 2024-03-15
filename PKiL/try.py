from random import random,choice
from Utils import Utils
from PKiL import ProKnow
from tqdm import tqdm

#N = 500
#x = 'have you  wished you could go to sleep and never wake up.have you thought about doing something to suicide.have you thought about how you would suicide.do you think you would really suicide.have you thought about how and when you would suicide.'
#pk1.evaluate_pk(x)
'''
x = 0
while True:
    point  = ''
    for item in pk:
        if random() <= 0.9:
            point += choice(pk[item])+'.'
    f.write(point+'\n')
    x += 1
    if x == N:
        break
f.close()
'''
#test_point = "i have been there and got nothing same as my life.i have a gun.im not on a ledge or something but i have a gun on my lap."

pk1 = ProKnow()
pk1.process_knowledge('cssrs.txt','cssrs_annotate.txt')
#print (pk1.pk)
#exit()
#print (pk1.annotate_rules)
#exit()
train_data = Utils.read_file('train.txt')[:1]

pk_train_data = {}
clf_train_data = {}
n = len(train_data)

for i in tqdm(range(n)):
    item = train_data[i]
    label = pk1.evaluate_pk(item)
    pk_train_data[item] = label
    clf_label = pk1.evaluate_pk(item,pk=False)
    clf_train_data[item] = clf_label

#print (pk_train_data)
#exit()
#print (clf_train_data)

pk1.train(train_data = pk_train_data)



#pk1.evaluate_pk(test_point)
#exit()
#pk1.evaluate_pk(train_data[0])

        
        

