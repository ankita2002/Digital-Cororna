import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('white')
t.pencolor('red')
t.pensize(10)
a = 0
b = 0
t.speed(1)
t.penup()
t.goto(0,200)
t.pendown
#if(ASA()==True):
#    ASA()

def ASA():
    global a,b
    t.forward(a)
    t.right(b)
    a=a+3
    b=b+1

    #if b==210: 
        #break
    t.hideturtle() 

if(ASA()==True):
    ASA

turtle.done()