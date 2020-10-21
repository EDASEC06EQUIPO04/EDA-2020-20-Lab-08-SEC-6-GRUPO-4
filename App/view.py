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




def printAccident(info, lista):

        accidentCounter=0

        accidentRead=lt.getElement(info['accidents'],0) 
        print (accidentRead['Severity'])
        print (lt.getElement(lista,0))
        numAccidentes=controller.accidentSize(info)
        #for k in range (0, lt.size(lista)):
            #print (lt.getElement(lst,k))                  #Aqui se imprimen los valores del mapa
        dateCom=lt.getElement(lista,0)
            
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
                if str(dateCom)==str(oneDate1):     
                    print (dateCom, "--> ID: ", accidentRead['ID']," ", "Severidad: ",accidentRead['Severity'])
                    accidentCounter = accidentCounter+1
        
        print ("se encontraron ", accidentCounter ," accidentes en la fecha especificada")
      
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

def printAccidentRange(info, lista):
    
        accidentCounter=0
        accidentRead=lt.getElement(info['accidents'],0) 
        print (accidentRead['Severity'])
        print (lt.getElement(lista,0))
        numAccidentes=controller.accidentSize(info)
        for k in range (1, lt.size(lista)+1):
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
                if str(dateCom)==str(oneDate1):     
                    print (dateCom, "--> ID: ", accidentRead['ID']," ", "Severidad: ",accidentRead['Severity'])
                    accidentCounter = accidentCounter+1
        accidentCounter = accidentCounter
        print ("se encontraron ", accidentCounter ," accidentes antes de la fecha especificada")     
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
        #lt.addLast(cont['accidents'],"Dato de prueba de de la lista.. OKKKK")
        #dato=lt.getElement(cont['accidents'],0) 

        print (cont['accidents'])
        #print (dato)

        input("Ahora la mapa ordenado dateIndex")
        print (cont['dateIndex'])
        print ("")
        input("Se acaba de crear el Catalogo Analyzer con su respectiva lista y un mapa ordenado tipo RBT")
        # cont es el controlador que se usará de acá en adelante
       

    elif int(inputs[0]) == 2:

        t1_start = process_time()

        print("\n Cargando información de accidentes ....\n")

        controller.loadData(cont, accidentFile)
        #print (lt.getElement(cont['accidents'],0))
        #print (lt.getElement(cont['accidents'],controller.accidentSize(cont)))
        #for i  in range (0,controller.accidentSize(cont)):
        #   print (lt.getElement(cont['accidents'],i))
        print ("")
        print('Accidentes cargados: ' + str(controller.accidentSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))
        print("")

        #accidentRead=lt.getElement(cont['accidents'],0) 
        #print (accidentRead['Severity'])
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
        input("Clic para continuar")
       

    elif int(inputs[0]) == 3:
        print("\nIngrese una fecha para buscar accidentes: ")
        
        initialDate="2000-00-00"
        #finalDate= "2000-00-00"
        initialDate = input("Fecha Busqueda (YYYY-MM-DD): ")       
        #finalDate = input("Rango Final (YYYY-MM-DD): ")
        lst = controller.getAccidentsByRange(cont, initialDate, initialDate) 
        
        #print (lst)
        print("\nTotal de llaves en el rango: " + str(lt.size(lst)))
        print (initialDate)

        #for k,v in lst.items():
           #print (lt.getElement(lst,0))
        #   print (v)

              
        printAccident(cont,lst)

        """tamLista= lt.size(lst)   
        for i in range (1, tamLista):
               print (lt.getElement(lst,i))
        
      
        """
        input("Clic para continuar")

    elif int(inputs[0]) == 4:
        print("\nIngrese una fecha para buscar accidentes antes de esta: ")
        
        initialDate="2000-00-00"
        #finalDate= "2000-00-00"
        initialDate = input("Fecha Busqueda (YYYY-MM-DD): ")       
        #finalDate = input("Rango Final (YYYY-MM-DD): ")
        lst = controller.getAccidentsByRange(cont, initialDate, initialDate) 
        
        #print (lst)
        print("\nTotal de llaves en el rango: " + str(lt.size(lst)))
        print (initialDate)

        #for k,v in lst.items():
           #print (lt.getElement(lst,0))
        #   print (v)
        
        printAccidentAntesDe(cont,lst)

        """tamLista= lt.size(lst)   
        for i in range (1, tamLista):
               print (lt.getElement(lst,i))
        
      
        """
        input("Clic para continuar")

    elif int(inputs[0]) == 5:
        print("\nIngrese una fecha para buscar accidentes antes de esta: ")
        
        initialDate="2000-00-00"
        finalDate= "2000-00-00"
        initialDate = input("Fecha Inicial (YYYY-MM-DD): ")       
        finalDate = input("Rango Final (YYYY-MM-DD): ")
        lst = controller.getAccidentsByRange(cont, initialDate, finalDate) 
        
        print (lst)
        input (":::: Acabo de imprimir el rango de fechas que se consultaron del del mapa ::::")
        print("\nTotal de llaves en el rango: " + str(lt.size(lst)))
        print ("Rango desde: [ ",initialDate, " ] a [ ", finalDate," ]")

        #for k,v in lst.items():
           #print (lt.getElement(lst,0))
        #   print (v)
        
        printAccidentRange(cont,lst)
        
        """tamLista= lt.size(lst)   
        for i in range (1, tamLista):
        print (lt.getElement(lst,i))
        
    
        """
        input("Clic para continuar")


    elif int(inputs[0]) == 6:
        print("\nRequerimiento No 4 del reto 3: ")

#input fecha inicial
#input fecha final


        print("\nBuscando accidentes en un estado: ")
        
        
        #use OH to test
        #stateSearched= "OH"
        stateSearched = input("Estado a buscar: ")    
        
        resultLocation = controller.getAccidentsByState(cont, stateSearched)
        #print (lst)
        print("\nTotal de llaves en el rango: " + str(lt.size(lst)))
        print (initialDate,finalDate)

    else:
        sys.exit(0)
sys.exit(0)