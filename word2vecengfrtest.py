# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 21:05:18 2014

@author: mostafa
"""

import gensim
import os
import codecs
import io


modelfr = gensim.models.Word2Vec.load('/home/mostafa/Downloads/wikifr/modelfr')



modeleng = gensim.models.Word2Vec.load('/home/mostafa/Downloads/wikifr/modeleng')



import codecs

testfr= codecs.open('/home/mostafa/topenfrpr.csv', 'r', 'utf-8')

import pandas as pd
df = pd.read_csv(testfr)




for n in range( len(df)):
    if df['francais'][n] not in modelfr.vocab or df['english'][n] not in modeleng.vocab:
        df=df.drop(n)

df= df.reset_index(drop=True)



df['vectorfr']=[modelfr[df['francais'][n]] for n in range( len(df)  ) ]





df['vectoreng']=[modeleng[df['english'][n]] for n in range( len(df) )]


prelmatfr=df['vectorfr'][:10]

prelmateng=df['vectoreng'][:10]

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





def traducwithproxengfr(w,numb=10):
    return mostsimilarvect(modelfr,clf.predict(modeleng[w]),numb)
    
def traduclistfr(w,numb=10):
    return [traducwithproxengfr(w)[k][0] for k in range(numb)]
    


traductestfr=[ df['francais'][n] in traduclistfr(df['english'][n] ) for n in range(15)   ]    
    
    

    
scorefinalengfr = sum(traductestfr)/len(traductestfr)

print scorefinalengfr

#dictresultest1= { dfsmall['francais'][n+50]: mostsimilarvect(modelfr,matengtested[n],1)[0][0] for n in range(matengtested.shape[0]) }
#utiliser modelfr


#dictresultest5= { dfsmall['francais'][n+50]: [mostsimilarvect(modelfr,matengtested[n],5)[p][0] for p in range(5)] for n in range(matengtested.shape[0]) }



#dictres1= { dfsmal[n]: mostsimilarvect(modelfr,matengtested[n],1)[0][0] for n in range(matengtested.shape[0]) }

#listefrbig=[modelfr[w] for w  in modelfr.vocab ]
 
        
