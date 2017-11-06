def polygon(t,dist,sides):
    angle = 360/sides
    t.begin_fill()
    for times in range(sides):
        t.forward(dist)
        t.left(angle)
    t.end_fill()
                  
def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()


