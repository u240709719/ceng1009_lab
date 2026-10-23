import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
wn.bgcolor("lightgreen")
alex.color("blue")
alex.pensize(1)
def drawPoly(t,side,size):
    angle = 360/side
    for i in range (side):
        alex.forward(size)
        alex.left(angle)

#drawPoly(alex,8,50)


#for i in range (20):
    #drawPoly(alex,4,50)
    #alex.left(18)

def drawSpirals(t,angle):
    lenght = 2
    for i in range (84):
        alex.right(angle)
        alex.forward(lenght)
        lenght += 2
#drawSpirals(alex,90)
#drawSpirals(alex,89)

def drawEquitriangle(t,size):
    drawPoly(t,3,size)


#drawEquitriangle(alex,100)


def drawStar (t,size):
    for i in range (5):
        alex.forward(size)
        alex.left(216)

# for i in range (5):
#     drawStar(alex,100)
#     alex.penup()
#     alex.forward(350)
#     alex.left(216)
#     alex.pendown()

def drawSprite(t,leg , length):
    angle = 360/leg
    for i in range (leg):
        alex.forward(length)
        alex.backward(length)
        alex.left(angle)

drawSprite(alex , 15 , 120)
wn.exitonclick()
