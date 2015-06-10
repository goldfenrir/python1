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
def noComillas(campo):    
    for c in campo:
        if (c=="\""):
            return False
    return True
def quitarComilla(campo):  #quitar comas dentro de un campo con comillas
    if (noComillas(campo)):
        return campo
    flagComilla=0
    campoS=campo.strip() #campo sin espacios
    if (campoS[0]=="\"" and campoS[len(campoS)-1]=="\""):
        campoS=campoS[1:-1]
        campoS = campoS.translate(None, ',\"')        
        return campoS
    else:
        return -1
    return -1
def validarComillas(linea):
    nComillas=0
    comillasPares=True
    #omillasValidas=True
    for c in linea:
        if (c=="\""):
            nComillas+=1
        
    if ((nComillas%2)==0): comillasPares=True
    else: comillasPares=False
    return  (comillasPares)
    
        
def limpiarLinea(linea,numeroCampos): #se limpia una linea
    print linea
    nuevaLinea=""
    nCampos=1
    primero=True
    linea=linea.strip() #campo sin espacios
    #linea convertir ,   " ==  ,"
    #linea = linea sin acentos
    #linea = linea sin puntuacino menos comillas y comas \n
    if(validarComillas(linea)==False):
        print "cayo validarComillas"
        return -1
    i=0
    f=0
    
    while (f<len(linea)-1):
        
        print ("f: ",f)
        
        if (linea[f]=="," and linea[f+1]=="\""):
            nCampos+=1
            campo=linea[i:f]
            print campo
            if (quitarComilla(campo)!=-1):
                campo=quitarComilla(campo)
            else:
                
                return -1
            if (primero==False):
                nuevaLinea+=","
                nuevaLinea+=campo
            else:
                nuevaLinea+=campo
                primero=False
            print campo
            print nuevaLinea
            i=f+1
        f+=1
    
    f+=1
    nCampos+=1
    campo=linea[i:f]
    print campo
    if (quitarComilla(campo)!=-1):
        campo=quitarComilla(campo)
    else:
        print "cayo ultima validacion"
        return -1
    nuevaLinea+=","
    nuevaLinea+=campo
    print campo
    print nuevaLinea
    print nCampos
    if (nCampos==numeroCampos):
        return nuevaLinea
    else:
       
        return -1
    return nuevaLinea


print limpiarLinea("1,iop,\"d,e,s,c\",\"re,q,u,i\"",4)
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
