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

    #Generuje nový identifikator lodě
    def newId(self):
        keys = [*self.ships]
        #Kontroluje klíče po vymazaných lodích

        i = 1
        for key in keys:

            if( key != i and not(i in keys) ):
                return i
            i += 1
        return i

    #Pokládá loď
    def placeShip(self,ship,posX,posY,id=0):
        #Kotnrola místa na loď
        if(posX + ship.width) > self.size or (posY + ship.height) > self.size:
            return False
        #Kontroluje jestli by loď nezasahovala do jiné lodi
        for y in range(ship.height):
            for x in range(ship.width):
                if(ship.grid[y][x]):
                    if(self.grid[posY + y][posX + x]):
                        return False

        if(not(id)):
            id = self.newId()
        #Pokládá loď
        for y in range(ship.height):
            for x in range(ship.width):
                self.grid[posY + y][posX + x] = id
        #Přidává umísténí lodě a samotnou loď
        self.ships[id] = ship
        self.locs[id] = [posX,posY]
        return id

    #Maže loď z pole
    def removeShip(self,id):
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
        deletedShip = self.ships[id]
        del self.ships[id]
        return [deletedShip,posX,posY]

    #Převrací pole
    def rotate(self):
        newGrid = []
        for x in range(self.size):
            fr = []
            for y in range(self.size - 1,-1,-1):
                fr.append(self.grid[y][x])
            newGrid.append(fr)
        self.grid = newGrid

    #Vrací data tabulky s loděmi v kompatnější formě
    def getSaveData(self):
        shipsData = {}
        for i in self.ships:
            shipsData[i] = self.ships[i].getSaveData()

        #vrací: String - velikost mřížky # pozice loďí v JSON # data lodí v JSON
        return '{}#{}#{}'.format(self.size,json.dumps(self.locs),json.dumps(shipsData))

    #argument: String - velikost mřížky # pozice loďí v JSON # data lodí v JSON
    #Vytváři z kompaktnějších dat objekt tabulky
    def parseSaveData(self,data):
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
