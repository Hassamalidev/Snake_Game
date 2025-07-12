from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", 20, "normal")
class ScoreBoard(Turtle):
       def __init__(self):
           super().__init__()
           self.score = 0
           self.highest_score=0
           self.color("white")
           self.penup()
           self.goto(0, 265)
           self.hideturtle()
           self.update_score()
       def update_score(self):
           self.clear()
           self.write(f"Score: {self.score} High Score: {self.highest_score}", align=ALIGNMENT, font=FONT)
       # def game_over(self):
       #     self.goto(0,0)
       #     self.write("Game Over",  align=ALIGNMENT, font=FONT)

       def reset(self):
            if self.score>self.highest_score:
                self.highest_score=self.score
            self.score=0
            self.update_score()

       def score_count(self):
           self.score+=1
           self.update_score()

