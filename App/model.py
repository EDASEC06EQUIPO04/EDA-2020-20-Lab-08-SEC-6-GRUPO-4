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
from DISClib.DataStructures import listiterator as it
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
               'dateIndex':None
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
    occurreddate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, occurreddate.date())
    if entry is None:
        datentry = newDataEntry(accident)
        om.put(map, occurreddate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, accident)
    return map

def addDateIndex(datentry, accident):
    """
    Actualiza un indice de tipo de accidentes.  Este indice tiene una lista
    de accidentes y una tabla de hash cuya llave es el tipo de accidente y
    el valor es una lista con los accidentes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstaccidents']
    lt.addLast(lst, accident)
    severity = datentry['SeverityIndex']
    state = datentry['StateIndex']
    sever = m.get(severity, accident['Severity'])
    stateToAdd = m.get(state,accident['State'])
    if (sever is None):
        entry = newSeverityEntry(accident["Severity"], accident)
        lt.addLast(entry['lstseverity'], accident)
        m.put(severity, accident['Severity'], entry)
    else:
        entry = me.getValue(sever)
        lt.addLast(entry['lstseverity'], accident)

    if(stateToAdd is None):
        entry= newStateEntry(accident['State'], accident)
        lt.addLast(entry['lststate'], accident)
        m.put(state, accident['State'], entry)
    else:
        entry = me.getValue(stateToAdd)
        lt.addLast(entry['lststate'], accident)
    return datentry




def newDataEntry(accident):
    """
    Crea una entrada en el indice por tipo de accident, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'SeverityIndex': None, 'lstaccidents': None}
    ofentry['SeverityIndex'] = m.newMap(numelements=0,
                                    maptype='PROBING',
                                    comparefunction=compareSeverity)
    ofentry ['StateIndex'] = m.newMap(numelements=10, maptype= 'PROBING', comparefunction= compareStates)
    ofentry['lstaccidents'] = lt.newList('SINGLELINKED', compareDates)
    return ofentry


def newSeverityEntry(AccSeverity, accident):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """

    entry = {'severityIndex': None, 'lstseverity': None}
    entry['severityIndex'] = AccSeverity
    entry['lstseverity'] = lt.newList('SINGLE_LINKED', compareSeverity)
    return entry


def newStateEntry(AccState, accident):
    entry = {'sateIndex': None, 'lststate': None}
    entry['statetyIndex'] = AccState
    entry['lststate'] = lt.newList('SINGLE_LINKED', compareStates)
    return entry




# ==============================
# Funciones de consulta
# ==============================
def getAccidentsByRange(analyzer, initialDate,finalDate):
    
    lst = om.values(analyzer['dateIndex'], initialDate,finalDate)
    
    lstiterator = it.newIterator(lst)
    totalAccidents = 0
    while (it.hasNext(lstiterator)):
        lstdate = it.next(lstiterator)
        totalAccidents += lt.size(lstdate['lstaccidents'])
    return totalAccidents
    
    return lst


def getAccidentsByRange2(analyzer, initialDate,finalDate):
    
    lst = om.values(analyzer['dateIndex'], initialDate,finalDate)
    
    return lst

#this is the laziest way of solving this, but if it works it aint stupid
def getAccidentsOnDate (analyzer, dateinput):
    lst = om.values(analyzer['dateIndex'], dateinput, dateinput)
    lstiterator = it.newIterator(lst)
    totalAccidents = 0
    while (it.hasNext(lstiterator)):
        lstdate = it.next(lstiterator)
        totalAccidents += lt.size(lstdate['lstaccidents'])
    return totalAccidents
#---------------------------------------------------------------------------
#REQ 1
def getAccidentsDateSeverity (analyzer, initialDate, severity):
    accdate = om.get(analyzer['dateIndex'], initialDate)
    if accdate['key'] is not None:
        severitymap = me.getValue(accdate)['SeverityIndex']
        numtotal = m.get(severitymap, severity)

        if numtotal is not None:
            return m.size(me.getValue(numtotal)['lstseverity'])
        return 0

#---------------------------------------------------------------------------
#REQ2
def getAccidentsBeforeDate (analyzer, dateinput):
    dateinputformatted = datetime.datetime.strptime(dateinput, '%Y-%m-%d')
    earliestDate =str(minKey(analyzer))
    dateformatted = datetime.datetime.strptime(earliestDate, '%Y-%m-%d')
    result = getAccidentsByRange(analyzer, dateformatted.date(), dateinputformatted.date())
    worstDayEver =dateMostAccidents(analyzer, dateformatted, dateinputformatted)
    accidentsWorstDay = getAccidentsOnDate (analyzer, worstDayEver.date())
    print ("\nRango desde: [ ",earliestDate, " ] a [ ", dateinput," ]")
    print("\nTotal de accidentes en el rango de fechas: " + str(result)+ "\n")
    print("\nla fecha con mas accidentes fue:  " + str(worstDayEver))
    print("\ntotal de accidentes en " + str(worstDayEver) +  " :  " + str(accidentsWorstDay))


def dateMostAccidents(analyzer, initialDate, finalDate):
    currentdate = initialDate
    mostAccidents=0
    resultDate= None

    while currentdate < finalDate :
        currentaccidents = getAccidentsOnDate(analyzer, currentdate.date())
        if currentaccidents > mostAccidents:
            mostAccidents= currentaccidents
            resultDate= currentdate
        currentdate = currentdate + datetime.timedelta(days=1) 
    return resultDate

#---------------------------------------------------------------------------
#REQ3
#todo lo demas que requiere este ya esta en el req 1 y en la funcion general de find in range
def getAccidentsRangeSeverity(analyzer, initialdate, finaldate):
    currentdate = initialdate
    accidentsCat2=0
    accidentsCat3=0
    accidentsCat4=0

    while currentdate < finaldate :
        #only 3 possible categories exist, as the possible iterators are of such a  small size explicitly stating them as a str facilitates readability of the code
        accidentsCat2 = accidentsCat2 + getAccidentsDateSeverity(analyzer, currentdate, "2")
        accidentsCat3 = accidentsCat3 + getAccidentsDateSeverity(analyzer, currentdate, "3")
        accidentsCat4 = accidentsCat4 + getAccidentsDateSeverity(analyzer, currentdate, "4")

        currentdate = currentdate + datetime.timedelta(days=1)  
    accidentHighestCat(accidentsCat2, accidentsCat3, accidentsCat4)



def accidentHighestCat(cat1, cat2, cat3):
    largest = max(cat1, cat2, cat3)
    if largest == cat1 :
        print("la categoria con mas accidentes es la severidad 2")
        print("la categoria tiene " + str(cat1)+ " accidentes")
    elif largest == cat2:
        print("la categoria con mas accidentes es la severidad 2")
        print("la categoria tiene " + str(cat2)+ " accidentes")
    else :
        print("la categoria con mas accidentes es la severidad 2")
        print("la categoria tiene " + str(cat3)+ " accidentes")

#---------------------------------------------------------------------------
#req 4
def getAccidentsDateState (analyzer, initialDate, stateinpt):
    accdate = om.get(analyzer['dateIndex'], initialDate)
    if accdate['key'] is not None:
        statemap = me.getValue(accdate)['StateIndex']
        numtotal = m.get(statemap, stateinpt)
        if numtotal is not None:
            return m.size(me.getValue(numtotal)['lststate'])
        return 0


def getAccidentsRangeState (analyzer, initialdate, finaldate):
    highesState=0
    currentdate = initialdate

    while currentdate < finaldate :
        highesState = highesState + getAccidentsDateState(analyzer, currentdate, "OH")
        currentdate = currentdate + datetime.timedelta(days=1) 
    print(highesState)

#---------------------------------------------------------------------------------------
def getAccidentsHourRange (analyzer, initialtime, finaltime, lowrange, highrange):
    print("rango de tiempo:")
    print(initialtime.strftime('%H:%M:%S'))
    print(finaltime.strftime('%H:%M:%S'))

    print("rango de fechas:")
    print(lowrange)
    print(highrange)
    
    #resultlistcat2 =lt.newList(datastructure= 'SINGLE_LINKED')
    resultlistcat2 =0
    resultlistcat3 =lt.newList(datastructure= 'SINGLE_LINKED')
    resultlistcat4 =lt.newList(datastructure= 'SINGLE_LINKED')
    currentdate = lowrange

    severity = "2"
    while currentdate < highrange:
        temptotal = int(dateSeverity(analyzer, currentdate, severity))
        resultlistcat2 = resultlistcat2 + temptotal
    print (resultlistcat2)




def getAccidentsByRangeHour(analyzer, initialDate,finalDate, initialtime, finaltime):
    
    lst = om.values(analyzer['dateIndex'], initialDate,finalDate)
    lstiterator = it.newIterator(lst)
    totalAccidents = 0
    while (it.hasNext(lstiterator)):
        lstdate = it.next(lstiterator)
        totalAccidents += lt.size(lstdate['lstaccidents'])
    return totalAccidents



def dateSeverity(analyzer, initialDate, severity):
    accdate = om.get(analyzer['dateIndex'], initialDate)
    if accdate['key'] is not None:
        severitymap = me.getValue(accdate)['SeverityIndex']
        numtotal = m.get(severitymap, severity)
        if numtotal is not None:
            return m.size(me.getValue(numtotal)['lstseverity'])
        return 0



    # this is a variation of the get accidents date severity




def accidentSize(analyzer):
    """
    Número de accidentes en el catalogo
    """
    return lt.size(analyzer['accidents'])


def indexHeight(analyzer):
    return om.height(analyzer['dateIndex'])

def indexSize(analyzer):
    return om.size(analyzer['dateIndex'])

def minKey(analyzer):
    return om.minKey(analyzer['dateIndex'])


def maxKey(analyzer):
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

def compareStates ( state1, state2):
    sever = me.getKey(state2)
    if (state1 == sever):
        return 0
    elif (state1 > sever):
        return 1
    else:
        return -1
