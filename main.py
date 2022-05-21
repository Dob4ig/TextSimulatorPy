import os
from TextGame.Item import Item
from settings import game, player
from work import works
from food import foods

#Точка входа игрока.
print(game.greeting)
while(True):
    print(game.menu)
    #Выбор пункта меню:
    temp = input()
    os.system('cls||clear')
    if temp == "1":
       Item.display(works)
    elif temp == 2:
        pass