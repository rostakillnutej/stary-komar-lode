from lode.models.GameTable import GameTable
from lode.models.ShipAi import randomGrid,randomHit
from random import randint

class GameInstance:

    def __init__(self,table):
        self.returnData = table.getSaveData()
        self.player = GameTable(table)
        self.ai = GameTable(randomGrid())
        self.turn = 1 #randint(0,1)
        self.winner = False
        self.changed = False

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
                if self.ai.sunkIds == 5:
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
