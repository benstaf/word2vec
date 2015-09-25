# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 21:05:18 2014

@author: mostafa
"""

import gensim
import os
import codecs
import io


modeles = gensim.models.Word2Vec.load('modeles300mt11')


modelfr = gensim.models.Word2Vec.load('modelfr300mt11')


#modelfr=modelengmt11


testfr= codecs.open('topfrespanol.csv', 'r', 'utf-8')

import pandas as pd
df = pd.read_csv(testfr)

#dfsmalli=df[:60]


#dfsmall= dfsmalli[[ (' ' in w ) == False for w in dfsmalli['francais'] ]]

#dfsmall= dfsmall.reset_index(drop=True)



for n in range( len(df)):
    if df['francais'][n] not in modelfr.vocab or df['espanol'][n] not in modeles.vocab:
        df=df.drop(n)

df= df.reset_index(drop=True)


df['vectorfr']=[modelfr[df['francais'][n]] for n in range( len(df)  ) ]





#df['vectorfr']=[model[df['francais'][n]] for n in range( len(df['francais']))]

#df['vectores']=[model[df['espanol'][n]] for n in range( len(df['francais']))]

df['vectores']=[modeles[df['espanol'][n]] for n in range( len(df) )]


prelmatfr=df['vectorfr'][:5000]

prelmates=df['vectores'][:5000]

matrainfr= pd.DataFrame(prelmatfr.tolist()).values


matraines = pd.DataFrame(prelmates.tolist()).values


import numpy as np

#matrix W is given in  http://stackoverflow.com/questions/27980159/fit-a-linear-transformation-in-python

W = np.linalg.pinv(matrainfr).dot(matraines).T





def mostsimilarvect(self, vectenter, topn=5):
    self.init_sims()
    dists = np.dot(self.syn0norm, vectenter)
    if not topn:
        return dists
    best = np.argsort(dists)[::-1][:topn ]
        # ignore (don't return) words from the input
    result = [(self.index2word[sim], float(dists[sim])) for sim in best]
    return result[:topn]













def traducwithscofres(w,numb=5):
    return mostsimilarvect(modeles,W.dot(modelfr[w]),numb)


def traduclistfres(w,numb=5):
    return [traducwithscofres(w,numb)[k][0] for k in range(numb)]
    



#for n in range(5000,5100):
#    print df['espanol'][n] in traduclistfres(df['francais'][n] )





traductesttoptenfres=[ df['espanol'][n] in traduclistfres(df['francais'][n] ) for n in range(5000,6000) ]    
    
    

    
sum(traductesttoptenfres)/len(traductesttoptenfres)





traductestfres=[ df['espanol'][n] in traduclistfres(df['francais'][n],1 ) for n in range(5000,6000) ]    
    
    

    
sum(traductestfres)/len(traductesttoptenfres)

