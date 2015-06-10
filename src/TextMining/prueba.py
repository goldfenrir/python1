#!/usr/bin/python -i
"""Para ejecutar el programa por terminal
https://pypi.python.org/pypi/nltk
"""
from nltk.stem.snowball import SnowballStemmer
from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords
 	

import math
import string
#definiciones

def quitarComilla(campo):  #quitar comas dentro de un campo con comillas
    flagComilla=0
    campoS=campo.strip() #campo sin espacios
    if (campoS[0]=="\"" and campoS[len(campoS)-1]=="\""):
        campoS=campoS[1:-1]
        campoS = campoS.translate(None, ',\"')        
        return campoS
    else:
        return -1
    return -1

def limpiarLinea(linea): #se limpia una linea
    nCampos=0
    linea=linea.strip() #campo sin espacios
    #linea = linea sin acentos
    #linea = linea sin puntuacino menos comillas y comas \n
    
    for x in range(0,len(linea)-1):
        if (linea[x]=="," and linea[x+1]!="\""):
            nCampos=1
    
    if (nCampos==6):
        return linea
    else:
        return -1
    return linea


def arreglo_ofertas(archEscritura):
	lineas = archLectura.readlines()
	nuevaLinea = ""
	nuevaLinea += lineas[0]
	arregloLineas = []
	count = 1
	while count < len(lineas):
		puesto = lineas[count].split(',')
		#if puesto[0].isdigit() and puesto[1].isdigit() and puesto[2].isdigit():
		if puesto[0].isdigit():
			arregloLineas.append(nuevaLinea)
			nuevaLinea = ""
		nuevaLinea += lineas[count]
		count += 1
	arregloLineas.append(nuevaLinea)
	return arregloLineas


#Lectura y limpieza
#Quitamos todos los caracteres de puntuacion


#fin lectura y limpieza









"""
archLectura=open('TA_Registros_etiquetados1.csv','r')#Leer archivo

#archBag=open('Bag of words.txt','w')#Archivo de salida
#archRepBin=open('Representacion binaria.txt','w')
#archFreq=open('Frecuencia.txt','w')
#archTF_IDF=open('TF_IDF.txt','w')
#archDoc=open('Documentos.txt','w')

lineas=archLectura.readlines()
#print "Read Line: %s" % (lineas)

lineaTotal=""
for linea in lineas:
    lineaTotal+=linea
blob=TextBlob(lineaTotal.decode('utf-8'))



#separamos en palabras
words=blob.words
#print words
#quitamos los stop words
#hacemos un stemming snowball
comentarios=[]
stemmer = SnowballStemmer("spanish")
for word in words:    
    if word not in (stopwords.words('spanish')):#Elimnimar Stop words
        w=Word(word)        
        comentarios.append(stemmer.stem(w.lower()))


print "Nuevo: %s " % (comentarios)

#print stopwords.words('spanish')
"""
