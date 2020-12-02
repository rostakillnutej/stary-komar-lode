class GameTable:

    def __init__(self,draft):
        #TESTOVACÍ
        self.getGridString = draft.getGridString
        #Získává údaje z navrhové tabulky
        self.size = draft.size
        self.grid = draft.grid
        #self.locs = draft.locs
        self.ships = draft.ships
        #Stav pole, false - všechny lodě zničeny, true - hraje se
        self.state = True
        #Vytvaří pole s místy na které ještě nebylo stříleno
        self.empty = [*range(0,self.size ** 2,1)]
        #Idečko lodi která byla trefena nebo 0 když neblo trefeno nic
        self.shipHit = 0
        #Ídečka potopených lodí
        self.sunkIds = []
        #Drží počet zásahů do lodí
        self.hitCounter = {}

    #Pokládá střelu do mřížky
    def placeShot(self,posX,posY):
        pos = posY * self.size + posX
        #Zjištuje validní souřadnie a jestli na místě už neni střela, a jestli probíhá hra
        if posX >= self.size or posY >= self.size or not(pos in self.empty) or not(self.state):
            return False

        #Získává hodnotu z mřížky
        id = self.grid[posY][posX]
        #Když je hodnota větší než 0 byla trefena loď
        if id:
            #Když už byla loď trefena preď tím do přičte se k id lodě 1
            if id in self.hitCounter:
                self.hitCounter[id] += 1
                #Kontrola jestli nebyla trefená poslední část lodě
                if self.hitCounter[id] == self.ships[id].getShipParts():
                    self.sunkIds.append(id)
                    #Kontroluje jestli nejsou zničeny všechny lodě
                    if len(self.ships) == len(self.sunkIds):
                        self.state = False
            #Když jestě loď nebyla trefena vytvoří se klíč - id a hodnota - 1
            else:
                self.hitCounter[id] = 1

        self.shipHit = id
        #Maže místo kde bylo střeleno
        self.empty.remove(pos)
        return True
