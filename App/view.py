"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
import datetime
assert config
from time import process_time 
from math import acos, cos, sin, radians

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


#accidentFile='us_accidents_small.csv'
accidentFile='us_accidents_dis_2016.csv'
#accidentFile='US_Accidents_Dec19.csv'

#-------------------------------
#inicializando cont en none
cont=None
#--------------------------------

def compareIds (id1,id2):
    
    # compara los crimenes
    if (id1==id2):
        return 0
    elif (id1>id2):
        return 1
    else:
        return -1


def printAccidentAntesDe(info, lista):
    
        accidentCounter=0

        accidentRead=lt.getElement(info['accidents'],0) 
        print (accidentRead['Severity'])
        print (lt.getElement(lista,0))
        numAccidentes=controller.accidentSize(info)
        for k in range (0, lt.size(lista)):
            #print (lt.getElement(lst,k))                  #Aqui se imprimen los valores del mapa
            dateCom=lt.getElement(lista,k)
            
            for i in range (0,numAccidentes):
            #for i in range (0,10):    
                accidentRead=lt.getElement(info['accidents'],i) 
                #oneDate = datetime.datetime.strptime(accidentRead['Start_Time'], '%Y-%m-%d')
                oneDate = accidentRead['Start_Time']
                oneDate = datetime.datetime.strptime(oneDate, '%Y-%m-%d %H:%M:%S')
                oneDate1 = datetime.datetime.strftime(oneDate,'%Y-%m-%d')
                
                #print (oneDate1)
                #oneDate = datetime.fromisoformat(oneDate)
                #oneDate = datetime._parse_isoformat_date(oneDate)
                #print ("  k: ", k, "   v:", v, "  ", i, ": " , accidentRead['ID']," ", accidentRead['Severity']," ",oneDate1)
                #print (dateCom, "-->",oneDate1)
                #input("")
                if str(dateCom)>=str(oneDate1):     
                    print (dateCom, "-->", i, ": " , "ID: ", accidentRead['ID']," ", "Severidad: ",accidentRead['Severity'])
                    accidentCounter = accidentCounter+1
        accidentCounter = accidentCounter-1
        print ("se encontraron ", accidentCounter ," accidentes antes de la fecha especificada")        


def distancia (c1, c2):
    c1= (radians(c1[0]), radians (c1[1]))
    c2= (radians(c2[0]), radians (c2[1]))
    dist=acos(sin(c1[0])*sin(c2[0])+cos(c1[0])*cos (c2[0])*cos(c1[1]-c2[1]))
    return dist * 6371.01



def printAccidentGeo(info, lista):
    
        #Coordenada (latitud, longitud)
        la1=float(input("Digite la latitud_1: "))
        lo1=float(input("Digite la longitud_1: "))
        c1=(la1,lo1)
        radio=float(input("Digite el numero de kilometros a la redonda para verificar: "))
        #la=float(input("Digite la latitud_2: "))
        #lo=float(input("Digite la longitud_2: "))
        #c2=(la,lo)
        #resp=distancia (c1,c2)
        #print ("La distancia entrer las dos coordenadas es:" , resp)
        accidentCounter=0

        accidentRead=lt.getElement(info['accidents'],0) 
        print (accidentRead['Start_Lat'], accidentRead['Start_Lng'])
        
        numAccidentes=controller.accidentSize(info)    
        for i in range (0,numAccidentes):
            accidentRead=lt.getElement(info['accidents'],i) 
            la2=accidentRead['Start_Lat']
            lo2=accidentRead['Start_Lng']
            c2=(float(la2),float(lo2))
            resp=distancia (c1,c2)
            #print ("La distancia entrer las dos coordenadas es:" , resp)
        
            if resp<=50:     
                accidentCounter = accidentCounter+1
        
        print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")   
        print ("")
        print ("se encontraron ", accidentCounter ," accidentes en el radio dado")
        input ("Clic para continuar")
        

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@") 
    print("@@@@@@@@@                         RETO 3. Seguridad en las vias                @@@@@@@@@@@")   
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@") 
    print("[1] Inicializar Analizador")
    print("[2] Cargar información de accidentes")
    print("[3] Requerimento 1: Conocer los accidentes en una fecha")
    print("[4] Requerimento 2: Conocer los accidentes anteriores a una fecha")
    print("[5] Requerimento 3: Conocer los accidentesen un rango de fechas")
    print("[6] Requerimento 4: Conocer el estado con mas accidentes")
    print("[7] Requerimento 5: Conocer los accidentes por rango de horas")
    print("[8] Requerimento 6: Conocer las zona geografica mas accidentada")
    print("[9] Requerimento 7: Usar el conjunto completo de datos")
    print("[0]- Salir")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@") 


"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar >> ')

    if int(inputs[0]) == 1:

        print("\nInicializando lista Analyzer y mapa ordenado dateIndex....")
        cont = controller.init()
        # cont es el controlador que se usará de acá en adelante
        print (cont['accidents'])
        print (cont['dateIndex'])
        print ("Se acaba de crear el Catalogo Analyzer con su respectiva lista y un mapa ordenado tipo BST")
        #-------------------------------------------------------------------------------------------------------
        #este fragmento es exactamente igual al input 2, lo combine para agilizar pruebas
        t1_start = process_time()
        print("\n Cargando información de accidentes ....\n")

        cont=controller.loadData(cont, accidentFile)
        print ("")
        print('Accidentes cargados: ' + str(controller.accidentSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))
        print("")
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
        #-------------------------------------------------------------------------------------------------------
    elif int(inputs[0]) == 2:

        t1_start = process_time()
        print("\n Cargando información de accidentes ....\n")

        cont=controller.loadData(cont, accidentFile)
        print ("")
        print('Accidentes cargados: ' + str(controller.accidentSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))
        print("")
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")





    elif int(inputs[0]) == 3:
        #REQUERIMIENTO 1
        #input: fecha especifica
        #output:cantidad de accidentes por severidad (range from 2-4)
        print("\nIngrese una fecha para buscar accidentes: ")

        #initialDate = input("Fecha Busqueda (YYYY-MM-DD): ") 
        initialDate="2016-08-09"
        initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d') 

        accidentsseverity2 = controller.getAccidentsDateSeverity(cont, initialDate, "2") 
        print("\nTotal de accidentes tipo 2: " + str(accidentsseverity2))
        accidentsseverity3 = controller.getAccidentsDateSeverity(cont, initialDate, "3") 
        print("\nTotal de accidentes tipo 3: " + str(accidentsseverity3))
        accidentsseverity4 = controller.getAccidentsDateSeverity(cont, initialDate, "4") 
        print("\nTotal de accidentes tipo 4: " + str(accidentsseverity4))

        input("oprima tecla para continuar")



    elif int(inputs[0]) == 4:
        #REQUERIMIENTO 2
        #input: fecha
        #output: total de accidentes antes de la fecha
        #output fecha con mas accidentes

        #print("\nIngrese una fecha: ")
        #initialDate = input("Fecha Busqueda (YYYY-MM-DD): ")      
        initialDate="2016-08-09" 
        result = controller.getAccidentsBeforeDate(cont, initialDate) 
        input("oprima tecla para continuar")

    elif int(inputs[0]) == 5:
        #REQUERIMIENTO 3
        #input: fecha inicial
        #input: fecha final
        #output: total de accidentes en rango
        #output categoria de accidentes mas reportada

        print("\nIngrese un rango para buscar accidentes: ")
        initialDate="2016-08-09"
        finalDate= "2016-09-15"
        #initialDate = input("Fecha Inicial (YYYY-MM-DD): ")       
        #finalDate = input("Rango Final (YYYY-MM-DD): ")
        total = controller.getAccidentsByRange(cont, initialDate, finalDate) 

        print ("\nRango desde: [ ",initialDate, " ] a [ ", finalDate," ]")
        print("\nTotal de accidentes en el rango de fechas: " + str(total) + "\n")
        controller.getAccidentsRangeSeverity(cont, initialDate, finalDate) 

        input("\noprima tecla para continuar")


    elif int(inputs[0]) == 6:
        #REQUERIMIENTO 4
        #input: fecha inicial
        #input: fecha final
        #output: estado con mas accidentes en rango
        #output: fecha con mas accidentes en rango

        print("\nBuscando accidentes en un estado: ")

        initialDate="2016-08-09"
        finalDate= "2016-09-15"
        #initialDate = input("Fecha Inicial (YYYY-MM-DD): ")       
        #finalDate = input("Rango Final (YYYY-MM-DD): ")
        total = controller.getAccidentsByRange(cont, initialDate, finalDate) 
        print ("\nRango desde: [ ",initialDate, " ] a [ ", finalDate," ]")
        print("\nTotal de accidentes en el rango de fechas: " + str(total) + "\n")
        controller.getAccidentsRangeState(cont, initialDate, finalDate) 






    elif int(inputs[0]) == 7:
        #REQUERIMIENTO 5
        #input: hora inicial
        #input: hora final
        #output: total accidentes agrupados severidad.  agrupar inputs de hora en clusters de 30 min
        #output: porcentaje de esta severidad en relacion al total
        initialDate="2016-08-09"
        finalDate= "2016-09-15"
        #initialDate = input("Fecha Inicial (YYYY-MM-DD): ")       
        #finalDate = input("Rango Final (YYYY-MM-DD): ")

        pass

    elif int(inputs[0]) == 8:
        #REQUERIMIENTO 6
        #input: longitud
        #input: latitud
        #input: radio busqueda 
        #output: total accidentes
        #output: total accidentes agruapdos por dia de la semana

        #use OH to test
        pass

    elif int(inputs[0]) == 9:
        #same shit done in 1 to 6 but use the large dataset

        pass


    else:
        sys.exit(0)
sys.exit(0)