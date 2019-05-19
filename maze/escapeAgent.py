import os
from maze import *
from turtle import *
from datetime import datetime
''' File Name format student#_Name e.g.) 2015123456_John'''

''' Write a function to escape from a maze with searching algorithm'''
''' You are allowed to use 5 functions (Left, Right, Forward, Backward, isSuccess) with agent actions '''
''' Starting point will be given'''
''' Program will be tested with different maze'''

''' Comment is necessary for code description '''
''' Plagiarism prohibited '''

def escape():
    import math
# The best solution in my opinion is to map the maze to a graph and then use DFS or BFS algorithm to search it for escape. The
# problem is that we need to create graph dynamically while moving through maze. If a tricky example is given it is very easy
# to get into a loop while moving through maze. That loop will make graph infinietly big. Avoiding loops seems requires remebering
# visited vertexes and their coordinates. That's what I will do in array "visited"

#class Tile is used to remember neighbours of every point we are in and path we went
    class Tile:
        def __init__(self, fromWhere):
            self.visitedNeighbours = []
            self.visitedNeighbours.append(fromWhere) # Direction from which we come is always first in a list, it allows to go back if there is no other way
        def addNeighbour(self, newNeighbour):
            self.visitedNeighbours.append(newNeighbour)

#This compares points that are of double type
    def areTilesTheSame (x1, y1, x2, y2):
        if abs(x1-x2)<0.2 and abs(y1-y2)<0.2:
            return True
        return False

    class Point:
        def __init__ (self,x,y):
            self.x=x
            self.y=y

    def getRadius(x,y):
        return math.sqrt(x*x+y*y)

# I store the path agent went through, in a list called 'path'. The last Tile in 'path' is the one we are currently in.
    path=[];
# This stores all points we have been to
    visited =[];
    startingTile = Tile("start"); # We start in a tile 'start' so we add it to the list and vector
    path.append(startingTile)
    visited.append(Point(agent.xcor(), agent.ycor()))

    while not isSuccess(): # main loop, stop if we are outside of maze

        shouldContinue=0 #This flag helps to break nested loops
# These 4 ifs are similar, I will describe only first one
        if  "forward" not in path[len(path)-1].visitedNeighbours: # We can move forward if we haven't been there before
            path[len(path)-1].addNeighbour("forward") # We went forward so we add a visited neigbour
            if (Forward(agent)): #If we can got forward we add a new tile to the 'path' and remember we came there from backward
                for point in visited: #we iterate through
                    if  areTilesTheSame(point.x, point.y,agent.xcor(), agent.ycor()): #if we have been there we go back
                        Backward(agent)
                        shouldContinue=1;
                        break;
                if shouldContinue: # Go to while if we have visited that point
                    continue;
                step = Tile("backward") # Make a tile and append it to the list so we will start in it in next iteration
                path.append(step)
                visited.append(Point(agent.xcor(), agent.ycor()))
            continue

        if  "right" not in path[len(path)-1].visitedNeighbours:
            path[len(path)-1].addNeighbour("right")
            if (Right(agent)):
                for point in visited:
                    if  areTilesTheSame(point.x, point.y,agent.xcor(), agent.ycor()):
                        Left(agent)
                        shouldContinue=1;
                        break;
                if shouldContinue:
                    continue;
                step = Tile("left")
                path.append(step)
                visited.append(Point(agent.xcor(), agent.ycor()))
            continue


        if  "left" not in path[len(path)-1].visitedNeighbours:
            path[len(path)-1].addNeighbour("left")
            if (Left(agent)):
                for point in visited:
                    if  areTilesTheSame(point.x, point.y,agent.xcor(), agent.ycor()):
                        Right(agent)
                        shouldContinue=1;
                        break;
                if shouldContinue:
                    continue;
                step = Tile("right")
                path.append(step)
                visited.append(Point(agent.xcor(), agent.ycor()))
            continue


        if  "backward" not in path[len(path)-1].visitedNeighbours and getRadius(agent.xcor(), agent.ycor()) >55: # Here we cannot go backwards if we are the lowest level
            path[len(path)-1].addNeighbour("backward")
            if (Backward(agent)):
                for point in visited:
                    if  areTilesTheSame(point.x, point.y,agent.xcor(), agent.ycor()):
                        Forward(agent)
                        shouldContinue=1
                        break;
                if shouldContinue:
                    continue;
                step = Tile("forward")
                path.append(step)
                visited.append(Point(agent.xcor(), agent.ycor()))
            continue

        #When all neighbours are visited we are in a dead end and have to go back. Direction in visitedNeighbours[0] is from we came from

        if path[len(path)-1].visitedNeighbours[0] == "forward": # If we came from a tile that is forward we go back there and increase level
            Forward(agent)
        elif path[len(path)-1].visitedNeighbours[0] == "left":
            Left(agent)
        elif path[len(path)-1].visitedNeighbours[0] == "right":
            Right(agent)
        elif path[len(path)-1].visitedNeighbours[0] == "backward":
            Backward(agent)
        elif path[len(path)-1].visitedNeighbours[0] == "start": #If we came back to start and visited all neighbours of start then there is no way out of the maze
            print ("\nTHERE IS NO WAY OUT\n")
            break
        path.pop(len(path)-1) # If we go back we need to pop first tile from 'path'



if __name__ == '__main__':
    # Maze
    screen = Screen()
    sampleMaze()

    # Agent Init
    agent = Turtle()
    init_agent(agent)
    start = datetime.now()
    escape()
    finish = datetime.now()

    # Result
    print(os.path.basename(__file__).split('.')[0])
    print('Result   : Pass') if isSuccess() else print('Result   : Fail')
    print('Duration :', finish-start)

    mainloop()
