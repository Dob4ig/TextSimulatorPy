from TextGame.Game import Game
from TextGame.Player import Player


game=Game()
game.greeting="Добро пожаловать в симулятор человека!\n$help для помощи!"
game._win_msg="Вы выиграли!"
game.loose_msg="Вы проиграли!"
game.help_msg="Ваша цель продержаться 100 дней!"#Редактировать в процессе!


player=Player()
player.health_point=100
player.money=10
player.stamina=3
