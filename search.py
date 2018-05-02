from operator import add
# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    path=[]
    steps=[]
    steps.append( map(add,init, delta[0]))
    steps.append( map(add,init,delta[1]))
    steps.append( map(add,init,delta[2]))
    steps.append( map(add,init, delta[3]))

    #Remove illegal steps
    #If all steps are illegal, then we've hit a road block
########################################
    illegal_indices=[]
    next_steps=[]
    index=0
    for step in steps:
    #Check that we dont step outside the grid
        if(step[0]<0 or step[0]>len(grid) or step[1]<0 or
            step[1]>len(grid[0])-1):
            print "Illegal step" + str(step)
            index+=1
            continue
#Check that we don't step into a road block
        if(grid[int(step[0]),int(step[1])]==1):
            print "Illegal step" + str(step)
            index+=1
            continue

        index += 1
        next_steps.append(step)


########################################

    print next_steps
    return path

search(grid,init,goal,cost)
