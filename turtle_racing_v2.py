import turtle
import random
turtle.speed(10)
turtle.penup()
turtle.goto(-140,140)
donus = 0
for step in range(15):
    turtle.write(step ,align="center")
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(150)
    turtle.penup()
    turtle.backward(160)
    turtle.left(90)
    turtle.forward(20)

while donus < 100:
    ada = turtle.Turtle()
    ada.color("red")
    ada.shape("turtle")
    ada.penup()
    ada.goto(-160, 100)
    ada.pendown()

    bob= turtle.Turtle()
    bob.color("blue")
    bob.shape("turtle")
    bob.penup()
    bob.goto(-160, 70)
    bob.pendown()

    ken = turtle.Turtle()
    ken.color("black")
    ken.shape("turtle")
    ken.penup()
    ken.goto(-160, 40)
    ken.pendown()

    for turn in range(100):
        ada.forward(random.randint(1,5))
        bob.forward(random.randint(1,5))
        ken.forward(random.randint(1,5))
        print(turn)
        if turn == 99:
            donus += 1

print("Bir tuşa basınız")

dummy = input()