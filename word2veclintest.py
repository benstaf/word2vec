# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 21:05:18 2014

@author: mostafa
"""

import gensim
import os
import codecs
import io

#class MySentences(object):
# %   def __init__(self, dirname):
# %       self.dirname = dirname
# %   def __iter__(self):
# %      for fname in os.listdir(self.dirname):
# %         with open(os.path.join(self.dirname,fname)) as opn:
# %            for senten in opn:
# %                yield senten.split()
                                 #   senten= senten.encode('utf-8')
                
                
#            for senten in codecs.open(os.path.join(self.dirname,fname), 'r', 'utf-8'):


#%directory='/home/mostafa/Downloads/wikifr/wikisplitest'

#%directoryeng='/home/mostafa/tomsawyertest'

#%sentences = MySentences(directory)



modelfr = gensim.models.Word2Vec.load('/home/mostafa/Downloads/modelfrmini')



modeleng = gensim.models.Word2Vec.load('/home/mostafa/Downloads/modelengmini')
 # a memory-friendly iterator

#%model = Word2Vec.load(fname)


#%sentenceseng = MySentences(directoryeng)




 # a memory-friendly iterator




testfr= codecs.open('topenfrpr.csv', 'r', 'utf-8')

import pandas as pd
df = pd.read_csv(testfr)

#dfsmalli=df[:60]


#dfsmall= dfsmalli[[ (' ' in w ) == False for w in dfsmalli['francais'] ]]

#dfsmall= dfsmall.reset_index(drop=True)



for n in range( len(df)):
    if df['francais'][n] not in modelfr.vocab or df['english'][n] not in modeleng.vocab:
        df=df.drop(n)

df= df.reset_index(drop=True)


df['vectorfr']=[modelfr[df['francais'][n]] for n in range( len(df)  ) ]





#df['vectorfr']=[model[df['francais'][n]] for n in range( len(df['francais']))]

#df['vectoreng']=[model[df['english'][n]] for n in range( len(df['francais']))]

df['vectoreng']=[modeleng[df['english'][n]] for n in range( len(df) )]


prelmatfr=df['vectorfr'][:50]

prelmateng=df['vectoreng'][:50]

matrainfr= pd.DataFrame(prelmatfr.tolist()).values


matraineng= pd.DataFrame(prelmateng.tolist()).values


#START HERE

W = np.linalg.pinv(matrainfr).dot(matraineng).T




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










def traducwithscofreng(w,numb=10):
    return mostsimilarvect(modeleng,W.dot(modelfr[w]),numb)


def traduclistfreng(w,numb=10):
    return [traducwithscofreng(w,numb)[k][0] for k in range(numb)]
    


traductesttoptenfrengtest=[ df['english'][n] in traduclistfreng(df['francais'][n] ) for n in range(50,55) ]    




traductestfreng=[ df['english'][n] in traduclistfreng(df['francais'][n],1 ) for n in range(50,55) ]    
    
    

    
scorefinalfreng = sum(traductestfreng)/len(traductestfreng)

print scorefinalfreng



traductesttoptenfreng=[ df['english'][n] in traduclistfreng(df['francais'][n] ) for n in range(50,55) ]    
    
    

    
scorefinaltoptenfreng = sum(traductesttoptenfreng)/len(traductesttoptenfreng)

print scorefinaltoptenfreng























#prelmatpredfr= df['vectorfr'][5000:]

#matfrfortest= pd.DataFrame(prelmatpredfr.tolist()).values


#matengtested= clf.predict(matfrfortest)

#from most import mostsimilarvect



































#dictresultest1= { dfsmall['francais'][n+50]: mostsimilarvect(modelfr,matengtested[n],1)[0][0] for n in range(matengtested.shape[0]) }
#utiliser modelfr


#dictresultest5= { dfsmall['francais'][n+50]: [mostsimilarvect(modelfr,matengtested[n],5)[p][0] for p in range(5)] for n in range(matengtested.shape[0]) }



#dictres1= { dfsmal[n]: mostsimilarvect(modelfr,matengtested[n],1)[0][0] for n in range(matengtested.shape[0]) }

#listefrbig=[modelfr[w] for w  in modelfr.vocab ]
 




#dictotalfreng= { w: mostsimilarvect(modeleng,clf.predict(modelfr[w]))   for w in modelfr.vocab}



#import cPickle as pickle

#pickle.dump( dictotalfreng, open( "savefreng.p", "wb" ) )
        


