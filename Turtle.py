import turtle
tao = turtle.Pen() #Use the pen
tao.shape('turtle') #Turns into turtle
def Flower():
    for i in range(10):
        tao.circle(50)
        tao.left(36)

def Line():
    tao.penup()
    tao.left(200)
    tao.right(200)
    tao.forward(200)
    tao.pendown()

Flower()
Line()
Flower()
Line()
Flower()
Line()
Flower()
Line()
