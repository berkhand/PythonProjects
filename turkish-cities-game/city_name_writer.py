from turtle import Turtle


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(0, 0, 0)
        self.shape("blank")
        self.penup()

    def write_name(self, name, x, y):
        self.setposition(x, y)
        self.write(name, False, align="center",
                   font=('Arial', 14, 'normal'))
