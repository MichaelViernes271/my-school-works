"""
Refereence: Tech with Time. (). "Learn Python by Building Five Games - Full Course." freecodecamp.org. Retrieved April 30, 2022 from <https://www.youtube.com/watch?v=XGf2GcyHPhc&list=PLzKXyiTy2_I5m97uDH6N6bhszsOAbYnwV>
Author: Viernes, Michael
Date: April 30, 2022
Objective: Create a pong game.

Sidenote:
 Here are the suggested improvements from the author.
  1. Add a launch button to start the game.
  2. Set the limit to end the game.
  3. A background music will always be welcome.
  4. By making a menu screen likewise a complete game set, it allows replayability.
  5. Adding other kinds of gimmicks (e.g. cute animations, icons, improved ui) might help but this is a simple pong game with the usual setup.
 If you did enjoy the game or were inspired of it, you may share it with your friends and family. Thank you for your appreciation!
"""


import turtle

window = turtle.Screen()
window.title("Michael's Pong")
window.bgcolor("grey")
window.setup(width=800, height=600)
window.tracer(0)

# Scoring 
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1 )
paddle_a.penup()
paddle_a.goto(-350,0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1 )
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
# ball movements
ball.dx = .75
ball.dy = .75


# Pen writing the score.
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 \t Player B: 0", align="center", font=("Courier", 24, "normal"))


# A function for moving the paddles a and b.
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
# Keyboard binding (event calling) - listens for keyboard input of players.
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")



# Main game loop.
while True:
    window.update()
    
    # Move the ball.
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Checking the borders.
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} \t Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} \t Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        
    # The paddle and ball collisions.
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1    
          