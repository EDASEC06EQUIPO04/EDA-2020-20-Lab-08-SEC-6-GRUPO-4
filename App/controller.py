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

import config as cf
from App import model
import datetime
import csv
from DISClib.ADT import list as lt
#from DISClib.Algorithms.Sorting import insertionsortReto1 as ordenar

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion del modelo.
    """
    analyzer=model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, accidentsfile, accidentesArray):
    """
    Carga los datos de los archivos CSV en el modelo
    """
  
    accidentsfile = cf.data_dir + accidentsfile
    input_file = csv.DictReader(open(accidentsfile, encoding="utf-8"),delimiter=",")
    for accident in input_file:
         
        accidente ={

        "ID":accident['ID'],
        "Severity":accident['Severity'],
        "Start_Time":accident['Start_Time'],
        "Start_Lat":accident['Start_Lat'],
        "Start_Lng":accident['Start_Lng'],
        "State":accident['State']}
        
        accidente1=lt.newList('SINGLE_LINKED',compareIds)
        #'ARRAY_LIST' SINGLE_LINKED
        accidente1=accidente
        accidentesArray.append (accidente1)
       
        #model.addAccident(analyzer, accidente1)
       
    for i in range (0,len(accidentesArray)*0+200):    
        print (accidentesArray[i])
    input ("Se imprime Arreglo sin ordenar. Clic continuar.... favor espera mientras se ordena")

    ##### Lineas para ordenar el Arreglo  ######
    criterio='Start_Time'
    lst=accidentesArray
    for index in range(1,len(lst)):
        currentvalue = (lst[index][criterio])
        position = index
        original=lst[index]
        while position>0 and (lst [position-1][criterio])>(currentvalue):
            lst [position]=lst [position-1]
            position = position-1
        lst[position]=original
    accidentesArray = lst

    ###### Aqui finaliza                 #####
       
    for i in range (0,len(accidentesArray)*0+200):    
        print (accidentesArray[i])
    input (" Arreglo ordenado,Clic para continuar ....... ")

    for i in range (0,len(accidentesArray)):    
        model.addAccident(analyzer, accidente1)

    return analyzer



def compareIds (id1,id2):
    
    # compara los crimenes
    if (id1==id2):
        return 0
    elif (id1>id2):
        return 1
    else:
        return -1

def crear_accidente(ID:str,Severity:int,Start_Time:datetime,Start_Lat:None,Start_Lng:None,State:str)-> dict:
    
    Start_Time=datetime.datetime.now()
    Start_Time = datetime.datetime.strftime(Start_Time, '%Y-%m-%d %H:%M:%S')

    #Start_Time = datetime.datetime.strptime(Start_Time, "%a %b %d %H:%M:%S %Y")
    


    return {
    "ID":ID,
    "Severity":Severity,
    "Start_Time":Start_Time,
    "Start_Lat":Start_Lat,
    "Start_Lng":Start_Lng,
    "State":State}



# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def getAccidentsByRange(analyzer, initialDate,finalDate):

    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%d')
    
    return model.getAccidentsByRange(analyzer, initialDate.date(),finalDate.date())




def getAccidentsByState (analyzer, stateInput):

    return model.getAccidentsByState(analyzer, stateInput)


def accidentSize(analyzer):
    """
    Numero de crimenes leidos
    """
    return model.accidentSize(analyzer)

def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)

 
def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)                

def minKey(analyzer):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer)


def maxKey(analyzer):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer)