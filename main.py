from TextGame.Game import Game
from TextGame.Player import Player
from TextGame.Item import Item

game=Game()
game.greeting="Добро пожаловать в симулятор человека!\n$help для помощи!"
game._win_msg="Вы выиграли!"
game.loose_msg="Вы проиграли!"
game.help_msg="Ваша цель продержаться 100 дней!"#Редактировать в процессе!


player=Player()



#Точка входа игрока.
print(game.greeting)
while(True):
    pass