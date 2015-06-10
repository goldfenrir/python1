# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from nltk.stem.snowball import SnowballStemmer
from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords


import math
import string
import unicodedata


archLectura= open('vect.txt', 'r')
lineas=archLectura.readlines()
i=0
lineaTotal=""
for linea in lineas:
    lineaTotal+=linea
blob=TextBlob(lineaTotal.decode('utf-8'))
words=blob.words
dict = dict.fromkeys(words)
dictList=sorted(dict.keys())
bag=[]
for word in dict:
    bag.append(word)

#seq = ('name', 'age', 'sex','name')
archLectura.close()
archLectura= open('vect.txt', 'r')
archVect= open('Vectores.txt', 'w')
lineas=archLectura.readlines()

for linea in lineas:
    for word in bag:
        oracion= TextBlob(linea)
        dict[word]=oracion.word_counts[word]
    archVect.write(str(dict))
archVect.close()
archLectura.close()
#dictList=sorted(dict.keys())
#print dictList
#__author__ = "alulab14"
#__date__ = "$09/06/2015 07:16:30 PM$"
#
#if __name__ == "__main__":
#    print "Hello World"