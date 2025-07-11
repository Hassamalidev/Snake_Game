import  turtle
STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
      def __init__(self):
          self.all_segment=[]
          self.createSnake()
          self.head=self.all_segment[0]
      def createSnake(self):
          for position in STARTING_POSITION:
              self.add(position)

      def add(self, position):
          segment = turtle.Turtle("square")
          segment.penup()
          segment.color("white")
          segment.goto(position)
          self.all_segment.append(segment)

      def extend(self):
          self.add(self.all_segment[-1].position())

      def move(self):
          for seg in range(len(self.all_segment) - 1, 0, -1):
              new_x = self.all_segment[seg - 1].xcor()
              new_y = self.all_segment[seg - 1].ycor()
              self.all_segment[seg].goto(new_x, new_y)
          self.head.forward(MOVE_DISTANCE)

      def move_right(self):
          if self.head.heading()!=LEFT:
             self.head.setheading(RIGHT)
      def move_left(self):
          if self.head.heading() != RIGHT:
             self.head.setheading(LEFT)
      def move_up(self):
          if self.head.heading() != DOWN:
             self.head.setheading(UP)
      def move_down(self):
          if self.head.heading() != UP:
             self.head.setheading(DOWN)

