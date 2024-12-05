import pycxsimulator
from pylab import *
import numpy as np
import matplotlib.colors as mcolors

width = 20
height = 20
initProb = 0.2

# Define the custom colormap using the specified colors
colors = ['#000000', '#88CCEE', '#44AA99', '#117733', '#4141FF', '#AA4499',
          '#999933', '#CC6677', '#882255', '#FFFFFF']

# Create a colormap object from the list of colors
cmap = mcolors.ListedColormap(colors)

def initialize():
    global time, config, nextConfig

    time = 0
    
    # Initialize the grid with random values between 0 and 9 (representing the ten possible states)
    config = np.random.randint(0, 10, (height, width))
    
    # Initialize the next configuration grid
    nextConfig = np.zeros([height, width])

def observe():
    cla()

    # Use the custom colormap with values between 0 and 9
    imshow(config, vmin = 0, vmax = 9, cmap = cmap)
    axis('image')
    title('t = ' + str(time))

def update():
    global time, config, nextConfig

    time += 1
########################################################
    q1 = config[:10,:10]
    y = np.random.randint(0, 10)
    x = np.random.randint(0, 10)
    state = q1[y,x]
    next_state = np.random.randint(0,10)
    q1[y,x] = next_state
    
########################################################  
    q2 = config[:10,10:]
    
    y = np.random.randint(0, 10)
    x = np.random.randint(0, 10)
    state = q2[y,x]
    if (y > 3) & (y < 7) & (x > 3) & (x < 7) & (q2[y,x] != 0):
        comparison = np.random.randint(0,10)
        if comparison < 5:
            next_state = q2[y,x]
        if comparison >= 5:
            next_state = np.random.randint(0,10)
        else:
            next_state = 0 
    elif np.random.randint(0, 10) < 6:
        next_state = 0
    else:
        next_state = np.random.randint(0, 10)

    if state==0:
        next_state=0
    q2[y,x] = next_state

###################################################################################
    q3 = config[10:,:10]

    y = np.random.randint(0, 10)
    x = np.random.randint(0, 10)
    next_state = np.random.randint(0, 10)
    if y==0 | y ==10:
        if np.random.randint(0,10) > 5:
            next_state = 4
        else:
            next_state = 3
    q3[y,x] = next_state


###################################################################################

    q4 = config[10:,10:]



    top = np.hstack([q1, q2])  # Combine q1 and q2 horizontally
    bottom = np.hstack([q3, q4])  # Combine q3 and q4 horizontally
    config = np.vstack([top, bottom])

    #rint(config)

    nextConfig = config
    # Simulate the update of each cell
    # for x in range(10,width):
    #     for y in range(0,10):
    #         state = config[y, x]
    #         numberOfAlive = 0
    #         state = 0
    #         nextConfig[y, x] = state
    # for x in range(0,10):
    #     for y in range(0,10):
    #         state = config[y, x]
    #         numberOfAlive = 0
    #         state = state
    #         nextConfig[y, x] = state
    # for x in range(0,10):
    #     for y in range(10,20):
    #         state = config[y, x]
    #         numberOfAlive = 0
    #         state = state
    #         nextConfig[y, x] = state
    # for x in range(10,20):
    #     for y in range(10,20):
    #         state = config[y, x]
    #         numberOfAlive = 0
    #         state = state
    #         nextConfig[y, x] = state


    # Swap configs
    config, nextConfig = nextConfig, config

# Start the simulator
pycxsimulator.GUI().start(func=[initialize, observe, update])
