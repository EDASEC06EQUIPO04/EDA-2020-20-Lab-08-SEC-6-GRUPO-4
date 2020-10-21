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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria
"""

# -----------------------------------------------------
# API del TAD Catalogo de accidentes
# -----------------------------------------------------

def newAnalyzer():

    # creo la lista para almacenar todos los accidentes, esto es cada fila del excel con sus 49 campos
    # crea un Cataolo de Analyzer, una lista para los accidentes y una Mapa Ordenado para las fechas
    analyzer={ 'accidents':None,
               'dateIdndex':None
            }
    analyzer['accidents']=lt.newList('SINGLE_LINKED',compareIds)

    #analyzer['dateIndex']=om.newMap(omaptype='BST',comparefunction=compareDates)
    analyzer['dateIndex']=om.newMap(omaptype='RBT',comparefunction=compareDates)
    return analyzer

# Funciones para agregar informacion al catalogo

def addAccident(analyzer, accident):
    """
    """
    # crea solo el mapa 
    lt.addLast(analyzer['accidents'], accident)

    updateDateIndex(analyzer['dateIndex'], accident)
    
    return analyzer

def updateDateIndex(map, accident):
    """
    Se toma la fecha del accident y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de accidentes
    y se actualiza el indice de tipos de accidentes.
    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de accidentes
    """
    occurreddate = accident['Start_Time']

    accident_date = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')   

    entry = om.get(map, accident_date.date())
    if entry is None:
        datentry = newDataEntry(accident)
        om.put(map, accident_date.date(), datentry)
    else:
        datentry = me.getValue(entry)
   # addDateIndex(datentry, accident)
    return map

def addDateIndex(datentry, accident):
    """
    Actualiza un indice de tipo de accidentes.  Este indice tiene una lista
    de accidentes y una tabla de hash cuya llave es el tipo de accidente y
    el valor es una lista con los accidentes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lst_accidents']
    lt.addLast(lst, accident)
    severity = datentry['severity']
    sever = m.get(severity, accident['severity'])
    if (sever is None):
        entry = new_Accident_Entry(accident['severity'], accident)
        lt.addLast(accident['severity'], accident)
        m.put(accidentIndex, accident['severity'], entry)
    else:
        entry = me.getValue(sever)
        lt.addLast(entry['lstOfAccidents'], accident)
    return datentry

def new_Accident_Entry(severity, accident):
    """
    Crea una entrada en el indice por tipo de accident, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'accident1': None, 'lstOfAccidents': None}
    ofentry['accident1'] = severity
    ofentry['lstOfAccidents'] = lt.newList('SINGLELINKED', compareAccidents)
    return ofentry



def newDataEntry(accident):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'severityIndex': None, 'lst_accidents': None}
    entry['severityIndex'] = m.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareSeverity)
    entry['lst_accidents'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry


# ==============================
# Funciones de consulta
# ==============================
def getAccidentsByRange(analyzer, initialDate,finalDate):
    """
    Retorna el numero de crimenes en un rago de fechas.
    """
    lst = om.values(analyzer['dateIndex'], initialDate,finalDate)
    """accidentDate=om.get(analyzer['dateIndex'], initialDate)
    
    if accidentDate['key'] is not None:
        offensemap = me.getValue(accidentDate)['severityIndex']
        numoffenses = m.get(offensemap, offensecode)
        if numoffenses is not None:
            return m.size(me.getValue(numoffenses)['lst_accidents'])
        return 0
    """
    return lst


def getAccidentsByState(analyzer, stateInput):
    lst= om.values(analyzer, [''])



def accidentSize(analyzer):
    """
    Número de accidentes en el catago
    """
    return lt.size(analyzer['accidents'])


def indexHeight(analyzer):
    """Numero de accidentes leido
    """
    return om.height(analyzer['dateIndex'])

def indexSize(analyzer):
    """Numero de autores leido
    """
    return om.size(analyzer['dateIndex'])

def minKey(analyzer):
    """Numero de autores leido
    """
    return om.minKey(analyzer['dateIndex'])


def maxKey(analyzer):
    """Numero de autores leido
    """
    return om.maxKey(analyzer['dateIndex'])


# ==============================
# Funciones de Comparacion
# ==============================
def compareIds (id1,id2):

    # compara los crimenes
    if (id1==id2):
        return 0
    elif (id1>id2):
        return 1
    else:
        return -1

def compareDates (date1,date2):
    
    # compara los crimenes
    if (date1==date2):
        return 0
    elif (date1>date2):
        return 1
    else:
        return -1

def compareAccidents(accidente1, accidente2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    acci = me.getKey(accidente2)
    if (accidente1 == acci):
        return 0
    elif (accidente1 > acci):
        return 1
    else:
        return -1

def compareSeverity(severity1, severity2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    sever = me.getKey(severity2)
    if (severity1 == sever):
        return 0
    elif (severity1 > sever):
        return 1
    else:
        return -1