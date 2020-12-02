from random import shuffle, randint
from lode.models.Ship import Ship
from lode.models.DraftTable import DraftTable

#Data potřebné k vytvoření lodí
bluePrints = [
    'Letadlová loď,default,5,1,11111',
    'Bitevní loď,default,4,1,1111',
    'Křižník,default,3,1,111',
    'Ponorka,default,3,1,111',
    'Torpédoborec,default,2,1,11'
]

#Generuje grid bez mezery mezi loděmí
def randomGrid():
    table = DraftTable(10)
    #Indexy dat s loděmi
    vals = [0,1,2,3,4]

    #Zamíchání indexů s loděmi, změní pořadí pokladání lodí
    shuffle(vals)

    #Místo kde se nachází pokladač
    cur = [0,0]

    for i in vals:
        #Vytváří objekt pokládané lodě
        ship = Ship().parseSaveData(bluePrints[i])
        #Náhodná hodnota jako mezera mezi loděmi
        dis = randint(1, 3)
        #Náhodná hodnota pro otočení lodě
        rot = randint(0, 1)
        #Přidává rozestup
        cur[1] += dis
        #Kontroluje konec řádku
        if ship.width > (9 - cur[1]):
            #Jde na nový řádek
            cur[0] += 1
            cur[1] = cur[1] % 10

        #Kontroluje jestli je možné položit loď
        plan = True
        while plan:
            plan = False

            #Kontrola místa pro loď při položení horizontálně
            if ship.width > (9 - cur[1]) and rot == 0:
                cur[0] += 1
                cur[1] = 0
                plan = True
                continue

            #Kontrola místa pro loď při položení vertikálně
            if ship.width > (9 - cur[0]) and rot == 1:
                rot = 0
                plan = True
                continue

            #Kontrola kolize lodě při položení horizontálně
            if rot == 0:
                try:
                    for size in range(0,ship.width):
                        if table.grid[cur[0]][cur[1] + size] > 0:
                            cur[1] += 1
                            plan = True
                except:
                    print('SHIP-AI: CHYBA: DOŠLO MÍSTO')
                    print(cur)
                    print(ship.width)

            #Kontrola kolize lodě při položení vertikálně
            else:
                if table.grid[cur[0]][cur[1]] > 0:
                    cur[1] += 1
                    plan = True
        else:
            #Otáčí loď
            if rot == 1:
                ship.rotate()
            #Pokládá loď
            table.placeShip(ship,cur[1],cur[0])

    #Převrací náhodně celou tabulku
    flip = randint(0, 2)
    for i in range(flip):
        table.rotate()

    return table


def randomHit(empty):
    key = randint(0,len(empty)-1)
    x = empty[key] % self.player.size
    y = empty[key] // self.player.size
    return [x,y]
















#END
