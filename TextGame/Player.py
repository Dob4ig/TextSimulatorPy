

class Player():

    def __init__(self) -> None:
        self._health_point=None
        self._money=None
        self._stamina=None
    @property
    def health_point(self):
        return self._health_point
    @property
    def money(self):
        return self._money
    @property
    def stamina(self):
        return self._stamina

    @health_point.setter
    def health_point(self,new_health_point):
        self._health_point=new_health_point
    @money.setter
    def money(self,new_money):
        self._money=new_money
    @stamina.setter
    def stamina(self,new_stamina):
        self._stamina=new_stamina

