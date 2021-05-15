import turtle


#Window Setup
win = turtle.Screen()
win.title("BLASTEROIDS 3: PHANTOM GENESIS")
win.bgcolor('#808080')
win.setup(width=800, height=600) #Note: (0,0) is at the Centers
win.tracer(0)


#Game Elements

# Score
score_a = 0
score_b = 0

# Speed Values
playerspeed = 0.2
ballspeed   = 0.1
expfactor   = 0.02

# Paddle A
paddle_a = turtle.Turtle() #default size is 20x20 px
paddle_a.speed(0) #Max Speed
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #turtles draw lines when they're moving. this lifts the pen up
paddle_a.goto(-350, 0)
paddle_a.dx = 0
paddle_a.dy = 0



# Paddle B
paddle_b = turtle.Turtle() #default size is 20x20 px
paddle_b.speed(0) #Max Speed
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #turtles draw lines when they're moving. this lifts the pen up
paddle_b.goto(350, 0)
paddle_b.dx = 0
paddle_b.dy = 0

# Ball
ball = turtle.Turtle() #default size is 20x20 px
ball.speed(0) #Max Speed
ball.shape("square")
ball.color("#00FF00")
#paddle_b.shapesize(stretch_wid=5, stretch_len=1)
ball.penup() #turtles draw lines when they're moving. this lifts the pen up
ball.goto(0, 0)
ball.dx = ballspeed
ball.dy = ballspeed

# Pen - Makes Text
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0      Player 2: 0", align="center", font=("Centaur", 24, "normal"))



# Movement Functions.mew
def paddle_a_up():
    paddle_a.dy = playerspeed

def paddle_a_down():
    paddle_a.dy = -playerspeed

def paddle_b_up():
    paddle_b.dy = playerspeed

def paddle_b_down():
    paddle_b.dy = -playerspeed

def paddle_a_stop():
    paddle_a.dy = 0

def paddle_b_stop():
    paddle_b.dy = 0

"""
# Movement Functions.old
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
"""

# Object Collision
if (((ball.xcor() > 340) and (ball.xcor() < 350)) and ((ball.ycor() > (paddle_b.ycor()-50)) or (ball.ycor() < (paddle_b.ycor()+50)))):
    ball.goto(0,0)


# Keyboard Input
win.listen()
win.onkeypress(paddle_a_up,      "w") #called function, input trigger
win.onkeypress(paddle_a_down,    "s")
win.onkeypress(paddle_b_up,      "Up")
win.onkeypress(paddle_b_down,    "Down")
# New

win.onkeyrelease(paddle_a_stop,      "w")
win.onkeyrelease(paddle_a_stop,    "s")
win.onkeyrelease(paddle_b_stop,      "Up")
win.onkeyrelease(paddle_b_stop,    "Down")

#Main Game Loop
while True:
    win.update() #Main


    #Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Move Paddles
    paddle_a.sety(paddle_a.ycor() + paddle_a.dy)
    paddle_b.sety(paddle_b.ycor() + paddle_b.dy)


    #Border Logic
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #Score Logic
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write("Player 1: {}      Player 2: {}".format(score_a, score_b), align="center", font=("Centaur", 24, "normal"))
        # Exponential Speed Gain
        playerspeed *= (1+expfactor)**(score_b + score_a)
        #ballspeed *= (1+expfactor)**(score_b + score_a)


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write("Player 1: {}      Player 2: {}".format(score_a, score_b), align="center", font=("Centaur", 24, "normal"))
        # Exponential Speed Gain
        playerspeed *= (1+expfactor)**(score_b + score_a)
        #ballspeed *= (1+expfactor)**(score_b + score_a)

    # Score Update


    # Object Collision

    #Paddle B hit
    if (((ball.xcor() > 340) and (ball.xcor() < 350)) and ((ball.ycor() > (paddle_b.ycor()-50)) and (ball.ycor() < (paddle_b.ycor()+50)))):
        ball.dx *= -1

    #Paddle A hit
    if (((ball.xcor() < -340) and (ball.xcor() > -350)) and ((ball.ycor() > (paddle_a.ycor()-50)) and (ball.ycor() < (paddle_a.ycor()+50)))):
        ball.dx *= -1

    