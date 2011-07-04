import csv

class Inventory(dict):
    def __init__(self,inventorylist):
        self.inventorylist = inventorylist
    def add_item(self,item):
        self.inventorylist.append(item)
    def remove_item(self,item):
        self.inventorylist.remove(item)

class Location():
    direction = ['n', 's', 'e', 'w', 'u', 'd','exit', 'look', 'inventory', 'search']
    
    def __init__(self,game_map):
        self.game_map = game_map
        #print (self.game_map)
        
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
        
    def display_location(self,index):
        print 'You find yourself',((self.game_map[index])[0])
    
    def look_location(self,index):
        print ((self.game_map[index])[1])

class Player:
    def __init__(self, location):
        self.location = location
        self.inventory = Inventory(['copper sword',])
        
        
    def add_to_inventory(self, new_inventory):
        self.inventory.add_item(new_inventory)
        
    def display_inventory(self):
        print 'You carry:\n', self.inventory
        
        
    def get_location(self):
        return (self.location)
        
    def set_location(self,location):
        self.location = location
    

class GamePlay():
    def __init__(self):
        self.game_map = {}
        self.game_nav = {}
        self.inv_list = []
    
    def get_game_map(self):
        #print self.game_map
        return (self.game_map)
        
    def loadGame(self):
        map_reader = csv.reader(open('../resources/map.txt', 'rU'), delimiter='\t', quotechar='|') 
        j=0
        index_list = []
        desc_list = []
        
        
        for row in map_reader:        
            if j < 25:
            #print (len(row))
                for i in range(len(row)):
                    index_list.append(25*j+i)
                    if row[i] == 'null':
                        desc_list.append(row[i])
                    else:
                        cell_list = row[i].split(";")
                        desc_list.append(cell_list)
                # print ('%d: %s' % (25*j+i,row[i]))
            if j >= 26:
                for i in range(len(row)):
                    if row[i] != 'null':
                        l_list = row[i].split("\t")
                        self.inv_list.append(l_list[0])
            j=j+1
            
        print (self.inv_list)
        #print (len(desc_list))
        self.game_map = dict(zip(index_list,desc_list))
        #print (self.game_map)
        
        cell_nav = []
        current_nav = []
        
        for current_index,v in self.game_map.items():
            #print (current_index)
            #print (game_map[current_index])
            if (self.game_map[current_index]) != 'null':     
                if (current_index - 25) >= 0 and (self.game_map[current_index - 25]) != 'null':
                    cell_nav.append('n')
                if (current_index + 25) < 625 and (self.game_map[current_index + 25]) != 'null':
                    cell_nav.append('s')
                if current_index < 624:
                    if ((current_index % 24) != 0 or (current_index == 0)) and (self.game_map[current_index + 1]) != 'null':
                        cell_nav.append('e')
                if ((current_index) % 24) >0 and (self.game_map[current_index - 1]) != 'null':
                    cell_nav.append('w')
            
            cell_nav.append('look')
            cell_nav.append('search')
            cell_nav.append('inventory')
            cell_nav.append('help')
            current_nav.append(cell_nav)
            cell_nav = []
            
        self.game_nav = dict(zip(index_list,current_nav))
        cell_inv = []
        current_inv = []
        for current_index,v in self.game_map.items():
            if len(self.game_map[current_index]) > 2 and self.game_map[current_index] != 'null':     
                cell_inv = self.game_map[current_index]
                
            current_inv.append(cell_inv[2::])
            cell_inv = []
           
        self.game_inv = dict(zip(index_list,current_inv))
        
    def display_cell_inv(self,index):
        if len(self.game_inv[index]) >0:
            display_list = []
            print (self.game_inv[index][0])
            for i in range(len(self.game_inv[index])):
                print (self.game_inv[index][i])
                display_list.append(self.inv_list[int(self.game_inv[index][i])])
            print 'This area contains:', display_list
            print 'What would you like to pick up? <none>'
            
            while True:
                commandx = raw_input('\n>')
                try:
                    print commandx
                    print self.game_inv[index]
                    i = self.inv_list.index(commandx)
                    self.game_inv[index].remove(self.inv_list[i])
                except ValueError:
                    i = -1
                if i == -1:
                    break
                
    def display_navigation(self,index):
        print 'Your possible commands are:',(self.game_nav[index])
        
    def is_nav_valid(self,index,commandx):
        try:
            self.game_nav[index].index(commandx)
            return True
        except ValueError:
            return False

