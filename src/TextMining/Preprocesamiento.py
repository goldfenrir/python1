
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
    #if (campo==""): campo
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
    
def quitarComillasPuestoClase(linea):   
    nLinea=""
    clase=""
    puesto=""
    if (linea[0]=="\""):
        clase=linea[1]  
        linea=linea[4:]
    else:
        clase=linea[0]
        linea=linea[2:]
        
    if (linea[0]=="\""):
        puesto=linea[1:linea.find("\"")]  
        linea=linea[linea.find(",")+1:]
    else:
        puesto=linea[0:linea.find(",")]
        linea=linea[linea.find(",")+1:]
        
    nLinea+=clase
    nLinea+=","
    nLinea+=puesto   
    nLinea+=","
    nLinea+=linea
    return nLinea
    
def limpiarLinea(linea,numeroCampos): #se limpia una linea
    #print linea
    linea=quitar_campo1_2(linea)
    linea=quitarComillasPuestoClase(linea)
    #print linea
    nuevaLinea=""
    nCampos=0
    primero=True
    
    linea=linea.strip() #campo sin espacios
    #linea convertir ,   " ==  ,"
    #linea = linea sin acentos
    
    linea = quitar_puntuacion(linea)
    
    linea=linea.translate(None, '\n')
    
    if(validarComillas(linea)==False):
        
        #print "cayo validarComillas"
        return -1
    i=0
    f=0
    #print len(linea)
    while (f<len(linea)):
        
        
        #print f
        if (linea[f]=="," and ((nCampos==2 and 
        (noComillas(linea[f:] or f+2==len(linea)) )) or linea[f+1]=="\"" or nCampos<2)):
            nCampos+=1
            campo=linea[i:f]
            #print campo
            
            if (quitarComilla(campo)!=-1):
                campo=quitarComilla(campo)
            else:
                #print "callo"
                return -1
            if (primero==False):
                nuevaLinea+=","
                nuevaLinea+=campo
            else:
                nuevaLinea+=campo
                primero=False
            #print campo
            #print nuevaLinea
            i=f+1
        f+=1
    
    f+=1
    nCampos+=1
    campo=linea[i:f]
    #print campo
    if (quitarComilla(campo)!=-1):
        campo=quitarComilla(campo)
    else:
        #print "cayo ultima validacion"
        return -1
    nuevaLinea+=","
    nuevaLinea+=campo
    #print campo
    #print nuevaLinea
    if (nCampos==numeroCampos):
        return nuevaLinea
    else:
        return -1
    return nuevaLinea


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
    linea = oferta[1+oferta.find(','):]
 
    clase = ""
    clase = linea[:linea.find(',')]
    
    linea = linea[1+linea.find(','):]

    linea = linea[1+linea.find(','):]

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
def imprimir_archivo(lineas, nombreArch):
    archEscritura = open(nombreArch, 'w')
    for lin in lineas:
        archEscritura.write(lin)
        archEscritura.write("\n")
    archEscritura.closed
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


#print limpiarLinea("1,1,1231,iop,\"d,e,s,c\",\"re,q,u,i\"",4)


archLectura = open("TA_Registros_etiquetados.csv")
lineas = arreglo_ofertas(archLectura)
#print lineas[0]
#print quitar_campo1_2(lineas[0])
#
#print limpiarLinea(lineas[21],4)
#print quitarComillasPuestoClase

contador=0
contadorEliminados=0
arregloLineas = []
arregloLineasEliminadas = []
for linea in lineas:
    
    if (limpiarLinea(linea,4)!=-1):
        arregloLineas.append(limpiarLinea(linea,4))
        contador+=1
    else:
        arregloLineasEliminadas.append(linea)
        contadorEliminados+=1
        print "Linea eliminada"

print contador
print contadorEliminados
imprimir_archivo(arregloLineas,"limpio.csv")
imprimir_archivo(arregloLineasEliminadas,"eliminados.csv")
"""
#print limpiarLinea("1,iop,\"d,e,s,c\",\"re,q,u,i\"",4)"""