from turtle import *

# Simple class
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Line:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2

SUCCESS_LEVEL = 110
# Drawing maze
turtle = Turtle()
turtle.shape('circle')
paths = set()
tracer(0,0)

# Intersection
# http://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

# barrier on circle
def circle(r, a):
    a / 22.5
    for _ in enumerate(range(int(a / 22.5))):
        p1 = Point(turtle.pos()[0], turtle.pos()[1])
        turtle.circle(r,22.5)
        p2 = Point(turtle.pos()[0], turtle.pos()[1])
        if turtle.isdown():
            paths.add(Line(p1,p2))

# barrier on line
def line():
    turtle.right(90)
    turtle.pendown()
    turtle.forward(20)
    p1 = Point(turtle.pos()[0], turtle.pos()[1])
    turtle.backward(20)
    p2 = Point(turtle.pos()[0], turtle.pos()[1])
    turtle.left(90)
    paths.add(Line(p1,p2))

# sample maze
def sampleMaze():
    turtle.penup()

    # inner circle
    turtle.right(-90)
    turtle.forward(40)
    turtle.left(90)
    line()
    turtle.pendown()
    #turtle.circle(40,135)
    circle(40,135)
    line()
    turtle.penup()
    circle(40,45)
    line()
    circle(40,90)
    line()
    circle(40,45)
    line()
    circle(40,45)
    turtle.penup()
    turtle.home()



    # 2nd
    turtle.right(-90)
    turtle.forward(80)
    turtle.left(90)
    line()
    turtle.penup()
    circle(80, 45)
    turtle.pendown()
    circle(80, 45+90-22.5)
    turtle.penup()
    circle(80, 22.5)
    line()
    turtle.pendown()
    circle(80, 45)
    turtle.penup()
    circle(80,22.5)
    line()
    turtle.penup()
    circle(80,45)
    line()
    turtle.penup()
    circle(80,22.5)

    turtle.pendown()
    circle(80, 45)
    turtle.penup()
    turtle.home()

    # 3rd
    turtle.right(-90)
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()
    circle(100, 360)
    turtle.penup()
    turtle.home()

# Check if agent_path intersects maze path
def isBlocked(agent_path):
    for path in paths:
        if intersect(agent_path.p1,agent_path.p2, path.p1,path.p2):
            return True
            break
    return False

def init_agent(agent):
    global circle_level
    circle_level = 50
    agent.penup()
    agent.speed(0.5)
    agent.shape('circle')
    agent.color('red')
    agent.shapesize(.5)
    agent.left(180)
    agent.forward(circle_level)
    agent.left(90)
    agent.circle(circle_level,11.5+45)
    agent.pendown()
    tracer(1,1)

def isSuccess():
    # if outer radius 100
    if circle_level == SUCCESS_LEVEL:
        return True
    return False

# Actions
def Forward(agent):
    global circle_level
    if circle_level < SUCCESS_LEVEL:
        circle_level += 20
        p1 = Point(agent.pos()[0], agent.pos()[1])
        agent.right(90)
        agent.forward(20)
        agent.right(-90)
        p2 = Point(agent.pos()[0], agent.pos()[1])
        if isBlocked(Line(p1,p2)):
            circle_level -= 20
            agent.right(90)
            agent.backward(20)
            agent.right(-90)
            print('blocked')
            return False
    return True

def Backward(agent):
    global circle_level
    if circle_level > 50 and circle_level < SUCCESS_LEVEL:
        circle_level -= 20
        p1 = Point(agent.pos()[0], agent.pos()[1])
        agent.right(90)
        agent.backward(20)
        agent.right(-90)
        p2 = Point(agent.pos()[0], agent.pos()[1])
        if isBlocked(Line(p1,p2)):
            print('blocked')
            circle_level += 20
            agent.right(90)
            agent.forward(20)
            agent.right(-90)
            return False
    return True
def Right(agent):
    global circle_level
    if circle_level < SUCCESS_LEVEL:
        turtle.home()
        p1 = Point(agent.pos()[0], agent.pos()[1])
        agent.circle(circle_level,-22.5)
        p2 = Point(agent.pos()[0], agent.pos()[1])
        if isBlocked(Line(p1,p2)):
            print('blocked')
            agent.circle(circle_level,22.5)
            return False
    return True

def Left(agent):
    global circle_level
    if circle_level < SUCCESS_LEVEL:
        p1 = Point(agent.pos()[0], agent.pos()[1])
        agent.circle(circle_level,22.5)
        p2 = Point(agent.pos()[0], agent.pos()[1])
        if isBlocked(Line(p1,p2)):
            print('blocked')
            agent.circle(circle_level,-22.5)
            return False
    return True
