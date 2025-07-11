from turtle import Turtle
import  random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=-.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x_axis=random.randint(-270,270)
        y_axis=random.randint(-270,270)
        self.goto(x_axis,y_axis)