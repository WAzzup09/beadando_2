import turtle

def haromszog():
    turtle.Screen().clear()
    t = turtle.Turtle()
    for _ in range(3):
        t.forward(100)
        t.left(120)

def negyszog():
    turtle.Screen().clear()
    t = turtle.Turtle()
    for _ in range(4):
        t.forward(100)
        t.left(90)

def kor():
    turtle.Screen().clear()
    t = turtle.Turtle()
    for _ in range(360):
        t.forward(1)
        t.left(1)

def csillag():
    t = turtle.Turtle()
    for _ in range(5):
        t.forward(100)
        t.right(144)

def koch(lengthSide, levels):
    if levels == 0: 
        turtle.forward(lengthSide) 
        return
    lengthSide /= 3.0
    koch(lengthSide, levels-1) 
    turtle.left(60) 
    koch(lengthSide, levels-1) 
    turtle.right(120) 
    koch(lengthSide, levels-1) 
    turtle.left(60) 
    koch(lengthSide, levels-1) 
  
def indito():
    turtle.speed(0)                    
    length = 300.0   
          
    turtle.penup()                      
    
    turtle.backward(length/2.0) 
    
                
    turtle.pendown()  

    for i in range(3):     
        koch(length, 4) 
        turtle.right(120) 