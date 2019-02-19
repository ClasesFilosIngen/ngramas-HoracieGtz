import numpy as np
import matplotlib.pyplot as plt
import string
import collections
translator = str.maketrans('', '', string.punctuation+"´"+"¡"+"0"+"1"+"2"+"3"+"4"+"5"+"6"+"7"+"8"+"9"+"»"+"•"+"«"+"—"+"¿") 

def ngramas(texto,n):
	ngramas=[]
	for j in texto:							#Recorre lista de palabras
		for i in range((len(j))-(n-1)):		#Itera en el tamaño de la palabra-(n-1)
			ngramas.append(j[i:i+n:])		#Agrega a la lista y avanza en la palabra de i a i+n
	return ngramas


def analizarT(archivo):
	with open(archivo) as f:					#Abre archivo
		data=f.read().replace('\n',' ')			#Quita saltos de linea
		data=data.lower()						#Minusculas
		data=data.translate(translator)			#Elimina caracteres especiales
		pal=data.split( )						#Divide en palabras

	#t= trigrama d=diccionario l=lista  r=repetidos

	t=(ngramas(pal,3))						#Se dividen palabras en trigramas

	dT = collections.Counter(t)				#Se ordenan por los mas repetidos
	tR = dT.most_common(10)					#n ngramas mas comunes
	return tR


def graficas():
	idiomas=["Spanish.txt","English.txt","French.txt"]
	ltR=[]
	for i in range(len(idiomas)):
	    ltR.append(analizarT(idiomas[i]))

	plt.grid(True)
	plt.title("Trigramas mas comunes según idioma")   # Establece el título del gráfico
	plt.xlabel("Trigramas")   # Inserta el título del eje X 
	plt.ylabel("Repeticiones")   # Inserta el título del eje Y
	plt.plot(*zip(*ltR[0]), marker='o', linestyle='None', color='r',label="Español")
	plt.plot(*zip(*ltR[2]), marker='s', linestyle='None', color='b',label="Francés")
	plt.plot(*zip(*ltR[1]), marker='s', linestyle='None', color='g',label="Inglés")
	plt.legend(loc="upper left")
	plt.show()

def lista():
	idiomas=["Spanish.txt","English.txt","French.txt"]
	ltR=[]
	for i in range(len(idiomas)):
	    ltR.append(analizarT(idiomas[i]))

	for i in range(len(ltR)):
		if i==0:
			print("\nEspañol: ")
		if i==1:
			print("\nInglés: ")
		if i==2:
			print("\nFrancés")
		print(ltR[i])

print(lista(),graficas())
