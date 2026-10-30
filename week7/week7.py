import turtle
import math
# def sumTo(n):
#     result = n*(n+1)/2
#     return result
#
# print(sumTo(10))
#
#
# def drawStar (t, n , size):
#
#     angle = 180 - 180/n
#     for i in range(n):
#         t.forward(size)
#         t.left(angle)
#
wn = turtle.Screen()
tess = turtle.Turtle()
tess.color("hotpink")
tess.fillcolor("red")

# drawStar(tess,9,200)


# def sumTo(n):
#     countr = 0
#     for i in range(n + 1):
#          counter += 1
#
#     return counter
#
# print(sumTo(10))



# def sprite( t , leg , length  ):
#     angle = 360 / leg
#     for i in range (leg):
#         t.forward(length)
#         t.backward(length)
#         t.left(angle)
#
# def Square( t , size):
#     for i in range(4):
#         sprite(t, 15 , 20)
#         t.forward(size)
#         t.left(90)
#
#
# Square(tess,150)













# def checkSign ( n) :
#     if n > 0 :
#         return "positive"
#     elif n < 0 :
#         return "negative"
#     else :
#         return "zero"
#
#
# num = [-7 , 5 , 0 ]
# for n in num :
#     print(checkSign(n))





def drawBar( t , h , gap):
    t.begin_fill()
    t.left(90)
    t.forward (h + gap)
    t.write(str(h))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(h + gap)
    t.left(90)
    t.end_fill()


x = [ 33,45,66,77,89,100,150,200]
maxh = max(x)
num = len(x)
b = 20
wn.setworldcoordinates(0-b , 0-b ,40*num + b , maxh + b )

for i in x :
    drawBar(tess,i,10)

wn.exitonclick()
