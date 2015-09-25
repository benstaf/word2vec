# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 14:49:04 2014

@author: mostafa
"""

import numpy as np

def load_word2vec(file):
    
    word2vec = {} #skip information on first line
    fin= open(file)    
    for line in fin:
				items = line.replace('\r','').replace('\n','').split(' ')
				if len(items) < 10: continue
				word = items[0]
				vect = np.array([float(i) for i in items[1:] if len(i) > 1])
				word2vec[word] = vect
		
		
    return word2vec


print 'Loading vectors obtained with GloVe'
word2vec = load_word2vec('/home/mostafa/Downloads/vectors.6B.50d.txt')

print 'Analogy game: type a word:'
	#while (True):
word1 = raw_input('->').lower() 
print 'is to'
word2= raw_input('->').lower()
print 'as'
word3= raw_input('->').lower()
print 'is to...(GloVe is computing...)'

v1=word2vec[word1]
v2=word2vec[word2]
v3=word2vec[word3]

analogvect= v1/np.linalg.norm(v1) - v2/np.linalg.norm(v2) + v3/np.linalg.norm(v3)
cosi={}
for k, v in word2vec.items():
    if len(v)==len(analogvect):
        cosi[k]=1-((np.dot(v,analogvect))/(np.linalg.norm(v) * np.linalg.norm(analogvect)))
    
    
#vectsoustractnorm= {k: np.linalg.norm(v) for k, v in vectsoustract.items()}
cosi.pop(word3,None)
cosi.pop(word1,None)

#cosi=sorted(cosi)
        
answer = min(cosi,key=cosi.get)

#answer= cosi[:10]

print answer

#    word4