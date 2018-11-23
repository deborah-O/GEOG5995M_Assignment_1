"""
import pytest
import agentframework
import csv

''' Creating agent and environment store which are empty at the moment'''
agents = []
environment = []

'''Creating a single agent to use to test each function'''
num_of_agents = 2

'''This function adds the single agent to the empty agent store created above'''
for i in range(num_of_agents):
        agents.append(agentframework.Agent(environment, agents))

'''Importing the environment from external txt file and adding it to the empty environment store created above'''
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:	
    rowlist = []
    for value in row:				
        rowlist.append(value)
    environment.append(rowlist)
    
    			
f.close()

'''Defening a class to test the eat function'''    
def test_eat():
    '''The agent created above somewhere in the environment that has 100 units of food'''
    agents[0].environment[agents[0].columny][agents[0].columnx] = 100
    '''The agents current store is 0'''
    agents[0].store = 0
    '''This makes the agent eat'''
    agents[0].eat()
    
    '''Based on my original eat function, if the environment has more than 10  units of food, it should decrease by 10
       and add 10 to the agents store. There the environment should now have 90 units of food and the store should have 10.'''
    assert agents[0].environment[agents[0].columny][agents[0].columnx] == 90
    assert agents[0].store == 10
    '''If the test passes then the eat function works'''
    
    '''This tests if the environment works correctly, if the test passes then the function works'''
    agents[0].environment[agents[0].columny][agents[0].columnx] = 10
    agents[0].eat()

    assert agents[0].environment[agents[0].columny][agents[0].columnx] == 10

def test_distance_be():
    '''Setting the agents co-ordinates to 0 and 5'''
    agents[0].columny = 0 
    agents[0].columnx = 0
    
    agents[1].columny = 0 
    agents[1].columnx = 5
    '''This test would pass as the distance is 5'''
    assert agents[0].distance_between(agents[1]) == 5
    '''Changing the co-ordinate to 0'''
    agents[1].columnx = 0
    '''This test would pass as the distance has changed to 0'''
    assert agents[0].distance_between(agents[1]) == 0

def test_move():
     '''Agent 0 is at (0,0)'''
     agents[0].columny = 0 
     agents[0].columnx = 0
     '''Agent moves according to condition in framework'''
     agents[0].movement()
     '''Agent could only ever land on (1,99)(99,1), therefore test passes'''
     assert agents[0].columny == 1 or agents[0].columny == 99
     assert agents[0].columnx == 1 or agents[0].columnx == 99
     
     
def test_share():
    '''setting neighbourhood to 5000, something larger than distance condition from agent framework'''
    neighbourhood = 5000
    '''setting agents stores'''
    agents[0].store = 500    
    agents[1].store = 0
    '''Agent 0 should share with neighbours in the neighbourhood''' 
    agents[0].share_with_neighbours(neighbourhood)
    '''The test passes because both agents have 250 in their stores'''
    assert agents[1].store == 250 and agents[0].store == 250
    
    '''setting the neighbourhood to something less than distance'''
    neighbourhood = 0
    '''changing stores'''
    agents[1].store = 10
    '''Agent 0 instructed to share again''' 
    agents[0].share_with_neighbours(neighbourhood)
    '''Test passes if Agent 0 cannot share with neighbour Agent 1'''
    assert agents[1].store == 10 and agents[0].store == 250

pytest.main()
