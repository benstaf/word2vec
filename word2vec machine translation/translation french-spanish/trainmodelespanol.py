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

os.system("taskset -p 0xff %d" % os.getpid())

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            with open(os.path.join(self.dirname,fname)) as opn:
                for senten in opn:
                    yield senten.split()
                                 #   senten= senten.encode('utf-8')
                
                
#            for senten in codecs.open(os.path.join(self.dirname,fname), 'r', 'utf-8'):



directory='wikisplites'

#wikipedia spanish: https://dumps.wikimedia.org/eswiki/20150105/eswiki-20150105-pages-articles-multistream.xml.bz2 

#MT11 data set : http://www.statmt.org/wmt11/training-monolingual.tgz

sentences = MySentences(directory)


modeles = gensim.models.Word2Vec(sentences, size=300, window=10, min_count=5, workers=36)


modeles.init_sims(replace=True)


modeles.save('modeles300')

