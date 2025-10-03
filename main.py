from turtle import Screen, Turtle
import time
from game_utils import GameUtils

class Game:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Brekout Game 2025")
        self.screen.setup(width=700, height=900, startx=600, starty=50)
        self.screen.bgcolor("#1f2024")
        self.screen.tracer(0)
        self.game_utils = GameUtils(self.screen)
        self.screen.listen()
        self.screen.onkeypress(self.game_utils.paddle.go_left, "Left")
        self.screen.onkeypress(self.game_utils.paddle.go_right, "Right")
        self.screen.onkeypress(self.restart_game, "space")
        self.screen.onclick(self.start_game)

        self.screen.mainloop()

    def start_game(self, x, y):
        if not self.game_utils.game and not self.game_utils.over:
            self.game_utils.game = True
            self.game_loop()

    def restart_game(self):
        if self.game_utils.over:
            for heart in self.game_utils.hearts:
                heart.clear()
                heart.hideturtle()
            self.game_utils.hearts.clear()
            self.game_utils.heart()

            self.game_utils.game_turtle.clear()
            self.game_utils.score_turtle.clear()
            self.game_utils.score = 0
            self.game_utils.score_turtle.write(f"{str(self.game_utils.score).zfill(3)}", font=("retro", 60, "bold"))

            for block in self.game_utils.wall.blocks:
                block.hideturtle()

            self.game_utils.wall.blocks = []
            self.game_utils.wall.create_block()


            self.game_utils.ball.goto(0, 25)
            self.game_utils.ball.y_move = -3
            self.game_utils.ball.x_move = 3

            self.game_utils.paddle.goto(0, -350)
            self.game_utils.paddle.shapesize(stretch_wid=1, stretch_len=5)
            self.game_utils.game = True
            self.game_utils.over = False

            self.game_loop()

    def game_loop(self):
        while self.game_utils.game:
            time.sleep(0.008)
            self.screen.update()
            self.game_utils.ball.move()
            self.game_utils.wall_ball()
            self.game_utils.paddle_ball()
            self.game_utils.block_wall()
            self.game_utils.heart_break()
Game()

