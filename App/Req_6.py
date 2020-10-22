from math import acos, cos, sin, radians

def distancia (c1, c2):
    	c1= (radians(c1[0]), radians (c1[1]))
	c2= (radians(c2[0]), radians (c2[1]))
	dist=acos(sin(c1[0])*sin(c2[0])+cos(c1[0])*cos (c2[0])*cos(c1[1]-c2[1]))
	return dist * 6371.01

#Coordenada (latitud, longitud)
la=float(input("Digite la latitud_1: "))
lo=float(input("Digite la longitud_1: "))
c1=(la,lo)
la=float(input("Digite la latitud_2: "))
lo=float(input("Digite la longitud_2: "))
c2=(la,lo)
resp=distancia (c1,c2)
print ("La distancia entrer las dos coordenadas es:" , resp)
