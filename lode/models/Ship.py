class Ship:

    def __init__(self,name='none',type='default'):
        self.name = name
        self.type = type
        self.width = 0
        self.heght = 0
        self.grid = []

    def preCreate(self,width,height):
        #Vytváří prázdnou mřížku
        self.width = width
        self.height = height
        for y in range(height):
            fr = []
            for x in range(width):
                fr.append(0)
            self.grid.append(fr)

    def rotate(self):
        #Převrací tabulku lodě po směru hodin
        newGrid = []
        for x in range(self.width):
            fr = []
            for y in range(self.height - 1,-1,-1):
                fr.append(self.grid[y][x])
            newGrid.append(fr)
        #vyměnuje výšku a šířku lodě
        self.grid = newGrid
        mem = self.width
        self.width = self.height
        self.height = mem

    def fill(self,fromX,fromY,toX,toY,val = 1):
        #Funkce na vytváření části loďe
        #Vylní čtverec podle zadaných souřadnic
        for y in range(fromY,toY):
            for x in range(fromX,toX):
                self.grid[y][x] = val

    def getSaveData(self):
        #Vrací data lodé v kompaktnějším formátu
        large = []
        for line in self.grid:
            large.append(''.join([str(letter) for letter in line]))
        #vrací: String - naźev loďe,typ lodě,velikost x,velikost y,grid
        return '{},{},{},{},{}'.format(self.name,self.type,self.width,self.height,''.join(large))

    #argument: String - nazév loďe,typ lodě,velikost x,velikost y,grid
    def parseSaveData(self,data):
        #Přemění data lodě na objekt lodě
        arr = data.split(',')
        self.name = arr[0]
        self.type = arr[1]
        self.width = int(arr[2])
        self.height = int(arr[3])
        index = 0;
        for y in range(self.height):
            fr = []
            for x in range(self.width):
                fr.append(arr[4][index])
                index += 1
            self.grid.append(fr)
        return self



    #TESTOVACÍ
    def getGridString(self):
        out = []
        for line in self.grid:
            out.append(' '.join([str(letter) for letter in line]))
            out.append('\n')
        return ''.join(out)
