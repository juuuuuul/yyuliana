from turtle import *
speed(0)
def smth(size, levels, angle):
    if levels == 0:
        return
    forward(size)
    left(angle)
    smth(size*0.6, levels-1, angle)
    left(angle)
    smth(size*0.6, levels-1, angle)
    left(angle)
    backward(size)
smth(300, 7, 90)
mainloop()
