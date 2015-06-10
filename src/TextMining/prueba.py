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


def arreglo_ofertas(archLectura):
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

def quitar_campo1_2(oferta):
    linea = ""
    linea = oferta[oferta.find(','):]
    clase = ""
    clase = linea[:linea.find(',')]
    linea = linea[linea.find(','):]
    linea = linea[linea.find(','):]
    nLinea = ""
    nLinea += clase
    nLinea +=","
    nLinea += linea
    return nLinea
#Lectura y limpieza
#Quitamos todos los caracteres de puntuacion

def strip_accents(s): 
    res = s.decode('utf-8')
    linea = ''.join(c for c in unicodedata.normalize('NFD', res) 
        if unicodedata.category(c) != 'Mn')
    nlinea = linea.encode('ascii', 'ignore')
    nlinea = str(nlinea)
    return nlinea
#fin lectura y limpieza

def quitar_puntuacion(linea):
    exclude1 = set(string.punctuation)
    exclude = set()
    while len(exclude1) > 0:
        i = exclude1.pop()
        if not i == ',':
            if not i == '"':
                exclude.add(i)
    word = ''.join(ch for ch in linea if ch not in exclude)
    return word

def imprimir_archivo(lineas, nombreArch):
    archEscritura = open(nombreArch, 'w')
    for lin in lineas:
        archEscritura.write(lin)
        archEscritura.write("\n")
    archEscritura.closed




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
