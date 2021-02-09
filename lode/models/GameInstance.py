from lode.models.GameTable import GameTable
from lode.models.ShipAi import randomGrid,randomGridHard,randomHit
from flask_socketio import send, emit
from random import shuffle,randint


class GameInstance:

    def __init__(self,table,dif):
        self.returnData = table.getSaveData()
        self.player = GameTable(table)
        if(dif == 1):
            self.ai = GameTable(randomGrid())
        else:
            self.ai = GameTable(randomGridHard(dif == 3))

        if(dif == 1):
            limit = 80
        elif(dif == 2):
            limit = 65
        else:
            limit = 40

        newArr = []
        shuffle(self.player.empty)
        for i in self.player.empty:
            x = i % self.player.size
            y = i // self.player.size
            if self.player.grid[y][x]:
                newArr.append(i)
                continue
            if limit > 0:
                newArr.append(i)
                limit -= 1
        self.player.empty = newArr

        self.turn = 1
        self.winner = False
        self.changed = False
        self.dif = dif

    def aiHit(self):
        self.turn = not(self.turn)
        pos = randomHit(self.player.empty,self.player.size)
        self.player.placeShot(pos[0],pos[1])
        if not(self.player.state):
            self.winner = 'ai'

        return [pos,self.player.shipHit]


    def handleHit(self,x,y):
        self.changed = False
        if self.turn:
            result = self.ai.placeShot(x,y)
            if result:
                self.turn = not(self.turn)
                if len(self.ai.sunkIds) > 4:
                    self.winner = 'player'
                    return [result,self.ai.shipHit]
                else:
                    self.changed = self.aiHit()
                    return [result,self.ai.shipHit]

            else:
                #Položení zásahu se nepovedlo
                return [False]
        else:
            #Zahraje AIČKO kvůli bugu třeba
            self.changed = self.aiHit()
            return [False]







#player.sunkIds
#player.empty
#player.state
#player.shipHit











#
