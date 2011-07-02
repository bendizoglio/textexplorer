import engine
from engine import Inventory
from engine import Location
from engine import Player
from engine import GamePlay



   
m_player = Player(541)
g_inventory = Inventory()
game_play = GamePlay()

game_play.loadGame()
print (game_play.get_game_map())
m_location = Location(game_play.get_game_map())

while True:
    m_location.display_location(m_player.get_location())
    game_play.display_navigation(m_player.get_location())

    _direction = m_location.direction

    
    commandx = raw_input('\n>')
    try:
        i = _direction.index(commandx)
    except ValueError:
        i = -1
    if commandx == 'n':
        m_player.set_location(m_player.get_location()-25) 
    if commandx == 's':
        m_player.set_location(m_player.get_location()+25)
    if commandx == 'e':
        m_player.set_location(m_player.get_location()+1)
    if commandx == "w":
        m_player.set_location(m_player.get_location()-1)
    if commandx == 'look':
        m_location.look_location(m_player.get_location())
    if commandx == 'help':
        print (
        '''list of commands:
        n = NORTH
        s = SOUTH
        e = EAST
        w = WEST
        look = look around
        search = search for items in the vicinity\n\n''')

        

    


    
