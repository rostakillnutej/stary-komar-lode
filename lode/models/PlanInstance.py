from lode.models.DraftTable import DraftTable
from lode.models.Ship import Ship

class PlanInstance:

    def __init__(self,preCreated = False,table = 0):
        if preCreated:
            self.dock = []
            self.table = table
        else:
            self.dock = [
                Ship().parseSaveData('Letadlová loď,default,5,1,11111'),
                Ship().parseSaveData('Bitevní loď,default,4,1,1111'),
                Ship().parseSaveData('Křižník,default,3,1,111'),
                Ship().parseSaveData('Ponorka,default,3,1,111'),
                Ship().parseSaveData('Torpédoborec,default,2,1,11')
            ]
            self.table = DraftTable(10)

    #Validuje idečko loďe, i jestli je v docku nebo položená
    def validId(self,num,placed = False):
        if not(isinstance(num, int)):
            return False

        #Kontrola jestli validujeme id položené loďe
        if placed:
            #Idečko položené lodě hledá v tabulce v proměné která drží položené lodě
            return num in self.table.ships
        else:
            #Idečko nepoložené lodi musí být větší než nula ale menší než delka listu
            return num >= 0 and num < len(self.dock)

    #Pokládá loď, vrací id položené lodě
    def handlePlace(self,index,x,y):
        if not(self.validId(index)):
            return [False]
        ship = self.dock[index]
        #Kontroluje jestli se položení povedlo
        placedId = self.table.placeShip(ship,x,y)
        if placedId:
            #Maže loď z doku
            self.dock.pop(index)
            return [placedId,x,y]
        return [False]

    #Maže loď z tabulky, vrací bolean jako výsledek
    def handleRemove(self,shipId):
        if not(self.validId(shipId,True)):
            return [False]
        data = self.table.removeShip(shipId)
        self.dock.append(data[0])
        return data

    #Rotuje loď v doku, vrací bolean jako výsledek
    def handleShipRotate(self,index):
        if not(self.validId(index)):
            return False
        self.dock[index].rotate()
        return True

    def getDocks(self):
        ships = []
        for i in range(len(self.dock)):
            ships.append(self.dock[i].getSaveData())
        return ships
















#
