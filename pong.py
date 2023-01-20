import turtle

""" Global turtle and window variables """
window = turtle.Screen()
start = turtle.Turtle()
congrats = turtle.Turtle()
p1 = turtle.Turtle()
p2 = turtle.Turtle()
ball = turtle.Turtle()
pen = turtle.Turtle()

def init_game():
    """ Initializes turtle window and turtle components for game """
    turtle.setup(800, 600, None, None)
    window.title('Pong')
    window.bgcolor('Black')
    window.setup(width=800, height=600)
    window.tracer(1)
    # start setup
    start.color('white')
    start.ht()
    start.penup()
    start.goto(-100, 30)
    start.pendown()
    start.write('Game starting soon, get ready :D')
    # congrats setup
    congrats.ht()
    congrats.color('black', 'black')
    congrats.goto(-400, -300)
    congrats.begin_fill()
    congrats.goto(400, -300)
    congrats.goto(400, 300)
    congrats.goto(-400, 300)
    congrats.goto(-400, -300)
    congrats.end_fill()
    congrats.penup()
    # Paddle 1 setup
    p1.speed(0)
    p1.shape('square')
    p1.color('white')
    p1.shapesize(stretch_wid=5, stretch_len=1)
    p1.penup()
    p1.showturtle()
    p1.goto(-350, 0)
    # Paddle 2 setup
    p2.speed(0)
    p2.shape('square')
    p2.color('white')
    p2.shapesize(stretch_wid=5, stretch_len=1)
    p2.penup()
    p2.showturtle()
    p2.goto(350, 0)
    # Ball setup
    ball.speed(0)
    ball.shape('square')
    ball.color('white')
    ball.penup()
    ball.showturtle()
    ball.goto(0, 0)
    # Pen setup
    pen.speed(0)
    pen.color('white')
    pen.penup()
    pen.ht()
    window.listen()
    window.onkeypress(p1_up, 'w')
    window.onkeypress(p1_down, 's')
    window.onkeypress(p2_up, 'Up')
    window.onkeypress(p2_down, 'Down')

def pen_helper(a, b):
    """ Draws scoreboard in game window """
    pen.goto(-30, 280)
    pen.write('Player 1: ' + str(a) + '  Player 2: ' + str(b))

def pen_clear():
    """ Helper """
    pen.color('white', 'black')
    pen.goto(-100, 240)
    pen.begin_fill()
    pen.goto(100, 240)
    pen.goto(100, 300)
    pen.goto(-100, 300)
    pen.goto(-100, 240)
    pen.end_fill()

def p1_up():
    """ Specifies up movement of the player1 paddle """
    y = p1.ycor()
    y += 30
    p1.sety(y)
    if y > 250:
        p1.sety(250)

def p1_down():
    """ Specifies down movement of the player1 paddle """
    y = p1.ycor()
    y -= 30
    p1.sety(y)
    if y < -250:
        p1.sety(-250)

def p2_up():
    """ Specifies up movement of the player2 paddle """
    y = p2.ycor()
    y += 30
    p2.sety(y)
    if y > 250:
        p2.sety(250)

def p2_down():
    """ Specifies down movement of the player2 paddle """
    y = p2.ycor()
    y -= 30
    p2.sety(y)
    if y < -250:
        p2.sety(-250)

def no():
    """ Closes turtle if user does not want another game """
    congrats.penup()
    congrats.goto(-50, -100)
    congrats.pendown()
    congrats.write('Okay, cya :)')
    turtle.bye()

def endgame_routine(w):
    """
    Prints congrats message for winning player and prompts user to play another match or close
    :param w: 1 or 2 - the winner of the match
    """
    ball.ht()
    p1.ht()
    p2.ht()
    window.onkeypress(run_game, 'y')
    window.onkeypress(no, 'n')
    congrats.color('white')
    congrats.goto(-50, 0)
    congrats.pendown()
    congrats.write('Congrats Player ' + str(w) + '! You win!')
    congrats.penup()
    congrats.goto(-50, -50)
    congrats.pendown()
    congrats.write('Hit y to play again or n to stop the program')
    turtle.done()

def main_loop():
    """ Main pong loop - controls ball movement, scoring, calls endgame_routine when
     game is over """
    # Moving the ball
    ball.x = 10
    ball.y = -6
    player_one = 0
    player_two = 0
    pen_helper(player_one, player_two)
    # Main loop
    while True:
        window.update()
        ball.setx(ball.xcor() + ball.x)
        ball.sety(ball.ycor() + ball.y)
        # Y Boundaries
        if ball.ycor() > 290:
            ball.sety(290)
            ball.y *= -1
            ball.sety(ball.ycor() + ball.y)
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.y *= -1
            ball.sety(ball.ycor() + ball.y)
        # X Boundaries
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.x *= -1
            player_one += 1
            pen_clear()
            if ball.x > 0:
                ball.x += 1
                if ball.y > 0:
                    ball.y += 0.5
                else:
                    ball.y -= 0.5
            else:
                ball.x -= 1
                if ball.y > 0:
                    ball.y += 0.5
                else:
                    ball.y -= 0.5
            pen_helper(player_one, player_two)
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.x *= -1
            player_two += 1
            pen_clear()
            pen_helper(player_one, player_two)
        # Paddle Collisions
        if ball.xcor() > 340 and p2.ycor() + 50 > ball.ycor() > p2.ycor() - 50:
            ball.x *= -1
        if ball.xcor() < -340 and p1.ycor() + 50 > ball.ycor() > p1.ycor() - 50:
            ball.x *= -1
        if player_one > 9:
            winner = 1
            break
        if player_two > 9:
            winner = 2
            break
    endgame_routine(winner)

def run_game():
    """ Initializes game and begins main loop """
    init_game()
    main_loop()

run_game()
