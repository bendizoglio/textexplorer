import csv

class Inventory(dict):
    def _init_(self):
        self.inventorylist = []
    def add_item(self,item):
        self.inventorylist.append(item)
    def remove_item(self,item):
        self.inventorylist.remove(item)

class Location():
    direction = ['n', 's', 'e', 'w', 'u', 'd','exit', 'look', 'inventory', 'search']
    
    
    def _init_(self,name,desc):
        self.m_locations = {'Town Square':'the center of town','North Wall':'the north wall', 'South Wall':'the south wall'}
        
    def add_exit(self,direction,location):
        self.exits[direction] = location
        
    def leads_to(self,direction):
        return self.exits.get(direction)
    
    def resolve_location(self,choice):
        
        
        new_location = self.location
        
        if new_location:
            self.location = new_location
            print "you enter:", new_location
            
        else:
            print "you can't go that way."
        


class Player():
    def _init_(self, location):
        self.location = location
        self.inventory = Inventory()
        
        
    def add_to_inventory(self, new_inventory):
        self.inventory.add_item(new_inventory)
        
    def display_inventory(self):
        print 'You carry:\n', self.inventory
        
    def look_location(self):
        print "You're in:\n", self.location
        
    

class GamePlay(Location,Inventory):
    game_map = {}
    
    def loadGame(self):
        map_reader = csv.reader(open('resources/map.csv', 'rU'), delimiter=',', quotechar='|') 
        j=0
        index_list = []
        desc_list = []
        
        for row in map_reader:
            if j == 25:
                break
            for i in range(len(row)):
                index_list.append(25*j+i)
                if row[i] == 'null':
                    desc_list.append(row[i])
                else:
                    cell_list = row[i].split(";")
                    desc_list.append(cell_list)
                # print ('%d: %s' % (25*j+i,row[i]))
            j=j+1
        game_map = dict(zip(index_list,desc_list))
        print (game_map)
        
        cell_nav = []
        current_nav = []
        
        for current_index,v in game_map.items():
            print (current_index)
            print (game_map[current_index])
            if (game_map[current_index]) != 'null':     
                if (current_index - 25) >0 and (game_map[current_index - 25]) != 'null':
                    cell_nav.append('n')
                if (current_index + 25) <625 and (game_map[current_index + 25]) != 'null':
                    cell_nav.append('s')
                if current_index <624:
                    if (current_index % 25) != 0 and (game_map[current_index + 1]) != 'null':
                        cell_nav.append('e')
                if (current_index - 1 % 25) >0 and (game_map[current_index - 1]) != 'null':
                    cell_nav.append('w')
                
            current_nav.append(cell_nav)
            cell_nav = []
            
        game_nav = dict(zip(index_list,current_nav))
        print (game_nav)
            

    def play(self):
        self.help()
        self.player.look_location()
    
    def playercommand(self,):
        
        _direction = Location()

        while True:
            commandx = raw_input('\n>')
            try:
                i = _direction.direction.index(commandx)
            except ValueError:
                i = -1

            if i == 6:
                break

            elif i == 7:
                Player.look_location()

            elif i == 8:
                self.player.display_inventory()
            
            """elif i == 9 :
                location.inventorylist"""
                
        return(0)
    

