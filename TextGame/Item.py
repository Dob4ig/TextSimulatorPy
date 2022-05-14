
class Item():

    def __init__(self,name:str=None,cost:int=0,effect:int=0) -> None:
        self._name=name
        self._cost=cost
        self._effect=effect


    @property
    def name(self):
        return self._name
    @property
    def cost(self):
        return self._cost
    @property
    def effect(self):
        return self._effect

    @name.setter
    def name(self,new_name):
        self._name=new_name
    @cost.setter
    def cost(self,new_cost):
        self._cost=new_cost
    @effect.setter
    def effect(self,new_effect):
        self._effect=new_effect
