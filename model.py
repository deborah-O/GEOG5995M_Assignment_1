"""
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation


'''I am creating 10 agents, ensuring that the sequence runs once and creating a neighbourhood of 20'''
num_of_agents = 2
neighbourhood = 20

'''Creating empty stores for my agents, neighbourhood and environment'''
agents = []
agentlist = []
environment = []

'''Opening the external file and adding the data to the environment'''   
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:	
    rowlist = []
    for value in row:				
        rowlist.append(value)
    environment.append(rowlist)
    
    			
f.close()


'''This outlines the dimensions of my animation'''
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


'''Creating the agents and adding them to my agents list and environment.'''
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))


#agents[0].distance_between(agents[1])
	
'''Defining the update within my model to include an animation of my agents behaviour'''
def update(frame_number):

    fig.clear()  
   
     
    '''Plot environment'''
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    
    ''' Agents come to life.'''
    for i in range(num_of_agents):
           agents[i].movement()
           agents[i].eat()
           agents[i].share_with_neighbours(neighbourhood)
           agents[i].distance_between(agents[0])
    '''visualising my agents'''
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].columnx, agents[i].columny)

'''This stopping function is set to stop when my agents store is exactly equal to 100'''                 	
def gen_function(b = [0]):
    a = 0
    for i in range(num_of_agents):
           if agents[i].store == 100:
               break
           else:         
               a = a + 1
               yield a			# Returns control and waits next call.
               print ("I'm full!")

'''Creating the animation'''
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

matplotlib.pyplot.show()
