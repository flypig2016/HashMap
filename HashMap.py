#!/usr/bin/env python2

d = {}

#empty dectionary or d = {} 

#key value pairs: list of keys:  hashmap => effcient fast and uses the memory. implmemtation of hashmap is the dictionary.
#key must be hashable and unique
#dictonary/hashmap is not gurenteed to be in the order. unless a list.list is always in order.


d = {"1":1, "2":1, "3":2, "4":2, "5":1}

#print d["1"]
d.keys()
#print d.keys()

e = {"6":1}
d.update(e) #for merging.
#print d.keys()

d.items() # gives me back the list of Tuple -> can not change things or add things. it's fixed/
d.values() # give me back all the values 


x = d.keys()
y = d.values()
f = zip(x,y)
f=dict(zip(x,y))



#literating on a dcitionary.

for k , v in d.iteritems():  #most efficenl way to iterate the dictionary, does not use much memory.  
	#print "key " + str(k)
	#print "value" + v 
	pass


#take a dictionary and invert it.
newd ={}
for k , v in d.iteritems(): 
	if v in newd.keys():
		newd[v].append(k)
	else:
		newd[v] = [k]

print newd