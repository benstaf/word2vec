# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 21:05:18 2014

@author: mostafa
"""



import numpy
import gensim
import os
import codecs
import io



sentences = 'textwikieng' 


 # a memory-friendly iterator

modeleng = gensim.models.Word2Vec(sentences, size=300, window=10, min_count=5, workers=36)


modeleng.init_sims(replace=True)


modeleng.save('modeleng300')

