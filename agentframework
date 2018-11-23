import random


class Agent:
   # carry_on = True   

    def __init__(self, environment, agentlist):
        self.columny = (random.randint(0,99))
        self.columnx = (random.randint(0,99))
        self.environment = environment
        self.agentlist = agentlist
        self.store = 0
       
        
        
    def movement(self):
        '''To ensure agents move randomly and remain within the boundaries'''
        if random.random( ) <0.5:
            self.columny = (self.columny + 1) % 100
        else:
            self.columny = (self.columny - 1) % 100
         
        if random.random( ) <0.5:
            self.columnx = (self.columnx + 1) % 100
        else:
            self.columnx = (self.columnx - 1) % 100
        print ("I'm here:" , self.columny, self.columnx)

    def eat(self):
        '''This eat function ensures that agents only eat up too 100 and no more'''
        if self.environment[self.columny][self.columnx] > 10 and self.store <= 100:
           self.environment[self.columny][self.columnx] -= 10
           self.store += 10

    ''' Here, I'm attempting to calculate the distance between each agent'''
    def distance_between(self, agents):
        a = (((self.columny - agents.columny)**2) + 
                    ((self.columnx - agents.columnx)**2))**0.5
        
        print("We're this far apart:", a)
        return a
       
        
    def share_with_neighbours(self, neighbourhood):
        for i in self.agentlist:
            distance = self.distance_between(i) 
            if distance < neighbourhood:
                sharing = (self.store + i.store) / 2
                self.store = sharing
                i.store = sharing
               # print("sharing " + str(distance) + " " + str(sharing))
