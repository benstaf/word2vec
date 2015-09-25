# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 21:05:18 2014

@author: mostafa
"""

import gensim
import os
import codecs
import io


modelfr = gensim.models.Word2Vec.load('modelfr800')



modeleng = gensim.models.Word2Vec.load_word2vec_format('eng300.bin', binary=True)
 # a memory-friendly iterator



import codecs

testfr= codecs.open('topenfrpr.csv', 'r', 'utf-8')

import pandas as pd
df = pd.read_csv(testfr)




for n in range( len(df)):
    if df['francais'][n] not in modelfr.vocab or df['english'][n] not in modeleng.vocab:
        df=df.drop(n)

df= df.reset_index(drop=True)



df['vectorfr']=[modelfr[df['francais'][n]] for n in range( len(df)  ) ]





df['vectoreng']=[modeleng[df['english'][n]] for n in range( len(df) )]


prelmatfr=df['vectorfr'][:5000]

prelmateng=df['vectoreng'][:5000]

matrainfr= pd.DataFrame(prelmatfr.tolist()).values


matraineng= pd.DataFrame(prelmateng.tolist()).values


from sklearn import linear_model
clf = linear_model.LinearRegression()

clf.fit(matraineng,matrainfr)


#prelmatpredfr= df['vectorfr'][5000:]

#matfrfortest= pd.DataFrame(prelmatpredfr.tolist()).values


#matengtested= clf.predict(matfrfortest)

#from most import mostsimilarvect


import numpy as np

def mostsimilarvect(self, vectenter, topn=10):
    self.init_sims()
    vectunit = gensim.matutils.unitvec(vectenter)
    dists = np.dot(self.syn0norm, vectunit)
    if not topn:
        return dists
    best = np.argsort(dists)[::-1][:topn ]
        # ignore (don't return) words from the input
    result = [(self.index2word[sim], float(dists[sim])) for sim in best]
    return result[:topn]




def traducwithscoengfr(w,numb=10):
    return mostsimilarvect(modelfr,clf.predict(modeleng[w]),numb)


def traduclistengfr(w,numb=10):
    return [traducwithscoengfr(w,numb)[k][0] for k in range(numb)]
    




traductestengfr=[ df['francais'][n] in traduclistengfr(df['english'][n],1 ) for n in range(5000,6000) ]    
    
    

    
scorefinalengfr = sum(traductestengfr)/len(traductestengfr)

print scorefinalengfr



traductesttoptenengfr=[ df['francais'][n] in traduclistengfr(df['english'][n] ) for n in range(5000,6000) ]    
    
    

    
scorefinaltoptenengfr = sum(traductesttoptenengfr)/len(traductesttoptenengfr)

print scorefinaltoptenengfr


#dictresultest1= { dfsmall['francais'][n+50]: mostsimilarvect(modelfr,matengtested[n],1)[0][0] for n in range(matengtested.shape[0]) }
#utiliser modelfr


#dictresultest5= { dfsmall['francais'][n+50]: [mostsimilarvect(modelfr,matengtested[n],5)[p][0] for p in range(5)] for n in range(matengtested.shape[0]) }



#dictres1= { dfsmal[n]: mostsimilarvect(modelfr,matengtested[n],1)[0][0] for n in range(matengtested.shape[0]) }

#listefrbig=[modelfr[w] for w  in modelfr.vocab ]
 
        
