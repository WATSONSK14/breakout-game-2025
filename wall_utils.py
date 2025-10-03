from turtle import Turtle

class Wall:
    def __init__(self):
        self.walls = []
        self.blocks = []
        self.create_block()
        self.create_wall()


    def create_wall(self):
        # Sağ duvar
        self.right_wall = Turtle()
        self.right_wall.shape("square")
        self.right_wall.color("white")
        self.right_wall.shapesize(stretch_wid=45, stretch_len=0.8)
        self.right_wall.penup()
        self.right_wall.goto(x=333, y=9)
        self.walls.append(self.right_wall)

        # Sol duvar
        self.left_wall = Turtle()
        self.left_wall.shape("square")
        self.left_wall.color("white")
        self.left_wall.shapesize(stretch_wid=45, stretch_len=0.8)
        self.left_wall.penup()
        self.left_wall.goto(x=-340, y=9)
        self.walls.append(self.left_wall)

        # Üst duvar
        self.top_wall = Turtle()
        self.top_wall.shape("square")
        self.top_wall.color("white")
        self.top_wall.shapesize(stretch_wid=1.2, stretch_len=35)
        self.top_wall.penup()
        self.top_wall.goto(x=0, y=320)
        self.walls.append(self.top_wall)

    def create_block(self):
        colors = [
            ("red", 2),
            ("orange", 2),
            ("green", 2),
            ("yellow", 2)
        ]
        start_x = -307
        start_y = 250

        for color, rows in colors:
            for r in range(rows):
                x = start_x
                y = start_y - (len(self.blocks) // 12) * 15
                for _ in range(12):
                    block = Turtle()
                    block.shape("square")
                    block.color(color)
                    block.shapesize(stretch_wid=0.6, stretch_len=2.5)
                    block.penup()
                    block.goto(x=x, y=y)
                    self.blocks.append(block)
                    x += 55
