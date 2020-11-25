from lode.models.PlanInstance import PlanInstance
#from lode.models.GameInstance import GameInstance

class InstanceManager:

    def __init__(self):
        self.ins = {}

    #Vytváři novou instanci
    def add(self,id):
        self.ins[id] = PlanInstance()

    #Maže instanci po odpojení
    def delete(self,id):
        del self.ins[id]

    
