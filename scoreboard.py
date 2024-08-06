from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, score=0):
        super().__init__()
        self.goto(x=0, y=280)
        self.score = score
        self.penup()
        self.color("white")
        self.hideturtle()
        # It could be a good idea to add the 'align' and 'font' as constants top of the code
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 12, 'normal'))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", move=False, align='center', font=('Arial', 12, 'normal'))


