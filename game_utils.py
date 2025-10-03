from turtle import Turtle
from paddle import Paddle
from wall_utils import Wall
from ball import Ball
import pygame
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class GameUtils:
    def __init__(self, screen):
        self.screen = screen
        self.placeholder()
        self.scoreboard()
        self.heart()
        self.paddle = Paddle()
        self.ball = Ball()
        self.wall = Wall()
        pygame.mixer.init()
        self.block_sound = pygame.mixer.Sound(resource_path("sound/block.mp3"))
        self.paddle_sound = pygame.mixer.Sound(resource_path("sound/paddle.mp3"))
        self.heart_sound = pygame.mixer.Sound(resource_path("sound/heart.mp3"))
        self.game_over_sound = pygame.mixer.Sound(resource_path("sound/game_over.mp3"))
        self.win_sound = pygame.mixer.Sound(resource_path("sound/win.mp3"))

    def placeholder(self):
        self.score = 0
        self.lost_life = False
        self.hearts = []
        self.game = False
        self.over = False

    def paddle_ball(self):
        paddle_width = self.paddle.shapesize()[1] * 20
        paddle_half_width = paddle_width / 2

        paddle_left = self.paddle.xcor() - paddle_half_width
        paddle_right = self.paddle.xcor() + paddle_half_width
        paddle_top = self.paddle.ycor() + 10
        paddle_bottom = self.paddle.ycor() - 10

        ball_x_in_range = paddle_left <= self.ball.xcor() <= paddle_right
        ball_y_in_range = paddle_bottom <= self.ball.ycor() <= paddle_top

        if ball_x_in_range and ball_y_in_range:
            self.paddle_sound.play()
            self.ball.goto(self.ball.xcor(), self.paddle.ycor() + 10)
            x_diff = self.ball.xcor() - self.paddle.xcor()
            if x_diff > 0:
                self.ball.x_move = abs(self.ball.x_move)
            else:
                self.ball.x_move = -abs(self.ball.x_move)
            self.ball.bounce_y()


    def wall_ball(self):
        if self.ball.xcor() > 320 or self.ball.xcor() < -320:
            self.ball.bounce_x()
        if self.ball.ycor() > 300:
            self.ball.bounce_y()

    def block_wall(self):
        for block in self.wall.blocks:
            block_left = block.xcor() - 25
            block_right = block.xcor() + 25
            block_top = block.ycor() + 6
            block_bottom = block.ycor() - 6

            ball_in_x_range = block_left <= self.ball.xcor() <= block_right
            ball_in_y_range = block_bottom <= self.ball.ycor() <= block_top

            if ball_in_x_range and ball_in_y_range:
                self.ball.goto(self.ball.xcor(), block.ycor() + 10)

                x_diff = self.ball.xcor() - block.xcor()
                if x_diff > 0:
                    self.ball.x_move = abs(self.ball.x_move)
                else:
                    self.ball.x_move = -abs(self.ball.x_move)
                self.ball.bounce_y()

                block.hideturtle()
                self.wall.blocks.remove(block)

                if block.color()[0] == "red":
                    self.shrink_paddle()
                    self.score += 7
                elif block.color()[0] == "orange":
                    self.score += 5
                elif block.color()[0] == "yellow":
                    self.score += 3
                elif block.color()[0] == "green":
                    self.score += 3

                self.score_turtle.clear()
                self.score_turtle.write(f"{str(self.score).zfill(3)}", font=("Arial", 60, "bold"))
                if self.ball.y_move < 10:
                    self.ball.y_move += 0.15
                    self.ball.x_move += 0.15
                self.block_sound.play()
                break

            if not self.wall.blocks:
                self.game_over()

    def heart(self, size=0.1):
        x = 290
        y = 360
        for i in range(3):
            pen = Turtle()
            pen.color("red")
            pen.pensize(2)
            pen.speed(1)

            pen.penup()
            pen.goto(x, y)
            pen.pendown()

            pen.begin_fill()
            pen.left(140)
            pen.forward(180 * size)
            pen.circle(-90 * size, 200)
            pen.left(120)
            pen.circle(-90 * size, 200)
            pen.forward(180 * size)
            pen.end_fill()
            pen.hideturtle()
            self.hearts.append(pen)
            x -= 40

    def shrink_paddle(self):
        current_size = self.paddle.shapesize()[1]
        new_size = max(2.5, current_size / 2)
        self.paddle.shapesize(stretch_wid=1, stretch_len=new_size)

    def scoreboard(self):
        self.score_turtle = Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.penup()
        self.score_turtle.goto(-290,330)
        self.score_turtle.color("white")
        self.score_turtle.write(f"{str(self.score).zfill(3)}", font=("retro", 60, "bold"))

    def heart_break(self):
        if self.ball.ycor() < -470:
            if self.hearts and not self.lost_life:
                if len(self.hearts) > 1:
                    i = self.hearts.pop(0)
                    i.clear()
                    i.hideturtle()
                    self.lost_life = True
                    self.heart_sound.play()
                    self.screen.ontimer(self.reset_ball, 1800)
                else:
                    self.game_over()


    def reset_ball(self):
        self.ball.goto(0, 25)
        self.ball.y_move = -3
        self.ball.x_move = 3
        self.lost_life = False


    def game_over(self):
        self.game = False
        i = self.hearts.pop(0)
        i.clear()
        i.hideturtle()
        self.over = True
        self.game_turtle = Turtle()
        self.game_turtle.hideturtle()
        self.game_turtle.penup()

        if not self.wall.blocks:
            self.game_turtle.goto(-180, -50)
            self.game_turtle.color("white")
            self.game_turtle.write("YOU WIN", font=("Arial", 60, "bold"))
            self.win_sound.play()

        else:
            self.game_turtle.goto(-250, -50)
            self.game_turtle.color("white")
            self.game_turtle.write("GAME OVER", font=("Arial", 60, "bold"))
            self.game_over_sound.play()