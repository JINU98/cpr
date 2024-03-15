#test_point = "i have been there and got nothing same as my life.i have a gun.im not on a ledge or something but i have a gun on my lap."
test_point = "i feel backed into a corner mostly.and im tired of being tired of everything.if that makes sense.thank you i understand its a sad thing.but I also want people to realize that there can be humor in anything and its the best way to deal with this."  

from PKiL import ProKnow

pk1 = ProKnow()
pk1.process_knowledge('cssrs.txt','cssrs_annotate.txt')

#test_point = input("Enter test point: ")

label = pk1.evaluate_pk(test_point,explanation=True)
