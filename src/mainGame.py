import engine
from engine import Inventory
from engine import Location
from engine import Player
from engine import GamePlay


        
   
Location()
m_player = Player()
g_inventory = Inventory()
game_play = GamePlay()

game_play.loadGame()

runGame = 1
while runGame == 1:
    runGame = game_play.playercommand()
    
    


    
