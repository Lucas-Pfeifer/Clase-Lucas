import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0

barra_a = turtle.Turtle()
barra_a.speed(100)
barra_a.shape("square")
barra_a.color("white")
barra_a.shapesize(stretch_wid=5, stretch_len=1)
barra_a.penup()
barra_a.goto(-350, 0)

barra_b = turtle.Turtle()
barra_b.speed(0)
barra_b.shape("square")
barra_b.color("white")
barra_b.shapesize(stretch_wid=5, stretch_len=1)
barra_b.penup()
barra_b.goto(350, 0)

pelota = turtle.Turtle()
pelota.speed(10)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.07
pelota.dy = 0.07

pen = turtle.Turtle()
pen.speed(10)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador A: 0  Player B: 0", align="center", font=("Courier", 20, "normal"))

def barrita_a_arriba():
    y = barra_a.ycor()
    y += 20
    barra_a.sety(y)

def barrita_a_abajo():
    y = barra_a.ycor()
    y -= 20
    barra_a.sety(y)

def barrita_b_arriba():
    y = barra_b.ycor()
    y += 20
    barra_b.sety(y)

def barrita_b_abajo():
    y = barra_b.ycor()
    y -= 20
    barra_b.sety(y)

wn.listen()
wn.onkeypress(barrita_a_arriba, "w")
wn.onkeypress(barrita_a_abajo, "s")
wn.onkeypress(barrita_b_arriba, "Up")
wn.onkeypress(barrita_b_abajo, "Down")      

while True:
    wn.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1
        score_a += 1
        pen.clear()
        pen.write("Jugador A: {}  Player B: {}".format(score_b, score_a), align="center", font=("Courier", 20, "normal"))

    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Jugador A: {}  Player B: {}".format(score_b, score_a), align="center", font=("Courier", 20, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1

    if pelota.xcor() > 340 and pelota.xcor() < 350 and (pelota.ycor() < barra_b.ycor() + 50 and pelota.ycor() > barra_b.ycor() -50):
        pelota.setx(340)
        pelota.dx *= -1

    if pelota.xcor() < -340 and pelota.xcor() > -350 and (pelota.ycor() < barra_a.ycor() + 50 and pelota.ycor() > barra_a.ycor() -50):
        pelota.setx(-340)
        pelota.dx *= -1