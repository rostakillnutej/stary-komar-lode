from lode.models.PlanInstance import PlanInstance
from lode.models.DraftTable import DraftTable
#from lode.models.GameInstance import GameInstance

class InstanceManager:

    def __init__(self):
        self.ins = {}

    #Vytváři novou instanci
    def add(self,id,user):
        if user and user.currentTable != '':
            table = DraftTable()
            table.parseSaveData(user.currentTable)
            self.ins[id] = PlanInstance(True,table)
        else:
            self.ins[id] = PlanInstance()

    #Maže instanci po odpojení
    def delete(self,id):
        if id in self.ins:
            del self.ins[id]

    #Vrací instanci podle idečka
    def getIns(self,id):
        if id in self.ins:
            return self.ins[id]
        return False
