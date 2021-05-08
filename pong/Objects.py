import turtle


def Screen(title, width, height):
    Screen = turtle.Screen()
    Screen.title(title)
    Screen.bgcolor("black")
    Screen.setup(width=width, height=height)
    Screen.tracer(0)
    return Screen


class PongObject(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.shape("square")
        self.goto(x, y)
        self.height = self.shapesize()[0] * 10
        self.width = self.shapesize()[1] * 10


class Paddle(PongObject):
    def __init__(self, side, widthScreen, heightScreen, margin, v=20):
        if side == "left":
            x = (widthScreen / -2) + margin
        elif side == "right":
            x = (widthScreen / 2) - margin
        else:
            raise Error("only right or left")
        super().__init__(x, 0)
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.height = self.shapesize()[0] * 10
        self.width = self.shapesize()[1] * 10
        self.v = v
        self.topLimit = heightScreen / 2
        self.bottomLimit = heightScreen / -2

    def up(self):
        if self.ycor() >= self.topLimit:
            pass
        else:
            self.sety(self.ycor() + self.v)

    def down(self):
        if self.ycor() <= self.bottomLimit:
            pass
        else:
            self.sety(self.ycor() - self.v)


class Ball(PongObject):
    def __init__(self, d, x=0, y=0):
        super().__init__(x, y)
        self.dx = d
        self.dy = d

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)


class Score(PongObject):
    def __init(self, x, y):
        super().__init__(x, y)

    def update(self, a, b):
        self.clear()
        self.write("Player A: {}   Player B: {}".format(a, b), align="center", font=("Courier", 24, "normal"))
