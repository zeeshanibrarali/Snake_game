from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        n = 0
        for _ in range(3):
            new_turtle = Turtle(shape='square')
            new_turtle.penup()
            new_turtle.color('white')
            new_turtle.goto(x=new_turtle.xcor() - n, y=0)
            n += 20
            self.all_turtles.append(new_turtle)

    def add_segment(self):
        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        new_turtle.color('white')
        new_turtle.goto(x=self.all_turtles[-1].xcor(), y=self.all_turtles[-1].ycor())
        self.all_turtles.append(new_turtle)

    def reset(self):
        for seg in self.all_turtles:
            seg.goto(1000, 1000)
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]

    def extend(self):
        self.add_segment()

    def move(self):
        for turtles in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[turtles - 1].xcor()
            new_y = self.all_turtles[turtles - 1].ycor()
            self.all_turtles[turtles].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
            self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
            self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
            self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.all_turtles[0].setheading(180)
            self.move()
