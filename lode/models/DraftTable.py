import json
from lode.models.Ship import Ship

class DraftTable:

    def __init__(self,size = 10):
        self.size = size
        self.ships = {}
        self.locs = {}
        self.grid = []
        for y in range(size):
            fr = []
            for x in range(size):
                fr.append(0)
            self.grid.append(fr)

    def newId(self):
        #Generuje nový identifikator lodě
        keys = [*self.ships]
        #Kontroluje klíče po vymazaných lodích
        i = 1
        for key in keys:
            if(key != i):
                return i
            i += 1
        return i

    def placeShip(self,ship,posX,posY,id=0):
        #Pokládá loď
        if(not(id)):
            id = self.newId()

        #Kontroluje jestli je místo na loď
        for y in range(ship.height):
            for x in range(ship.width):
                if(ship.grid[y][x]):
                    if(self.grid[posY + y][posX + x]):
                        return False
        #Pokládá loď
        for y in range(ship.height):
            for x in range(ship.width):
                self.grid[posY + y][posX + x] = id
        #Přidává umísténí lodě a samotnou loď
        self.ships[id] = ship
        self.locs[id] = [posX,posY]
        return id

    def removeShip(self,id):
        #Maže loď z pole
        posX = self.locs[id][0]
        posY = self.locs[id][1]
        for y in range(self.ships[id].height):
            for x in range(self.ships[id].width):
                #Zjištujě tvar lodě
                if(self.ships[id].grid[y][x]):
                    #Maže loď
                    self.grid[posY + y][posX + x] = 0

        #Maže pozici lodě a loď samotnou
        del self.locs[id]
        del self.ships[id]

    def rotate(self):
        #Převrací pole
        newGrid = []
        for x in range(self.size):
            fr = []
            for y in range(self.size - 1,-1,-1):
                fr.append(self.grid[y][x])
            newGrid.append(fr)
        self.grid = newGrid


    def getSaveData(self):
        #Vrací data tabulky s loděmi v kompatnější formě
        shipsData = {}
        for i in self.ships:
            shipsData[i] = self.ships[i].getSaveData()

        #vrací: String - velikost mřížky # pozice loďí v JSON # data lodí v JSON
        return '{}#{}#{}'.format(self.size,json.dumps(self.locs),json.dumps(shipsData))

    #argument: String - velikost mřížky # pozice loďí v JSON # data lodí v JSON
    def parseSaveData(self,data):
        #Vytváři z kompaktnějších dat objekt tabulky
        arr = data.split('#')
        self.size = int(arr[0])
        #Získává pozice lodí a lodě v JSON
        locs = json.loads(arr[1])
        shipsData = json.loads(arr[2])
        ships = {}
        for i in shipsData:
            #Vytváři z kompatnějších dat lodí objekty lodí
            shipObj = Ship()
            shipObj.parseSaveData(shipsData[i])
            #Pokládá lodě podle pozic do mřížky
            self.placeShip(shipObj,locs[i][0],locs[i][1])



    #TESTOVACÍ
    def getGridString(self):
        out = []
        for line in self.grid:
            out.append(' '.join([str(letter) for letter in line]))
            out.append('\n')
        return ''.join(out)
