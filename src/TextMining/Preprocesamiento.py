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
    nCampos=0
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
    if (nCampos==numeroCampos):
        return nuevaLinea
    else:
        return -1
    return nuevaLinea


print limpiarLinea("1,iop,\"d,e,s,c\",\"re,q,u,i\"",4)