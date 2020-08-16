import sys
import turtle

def border (fon, x_acisi, y_acisi):
    fon.penup()
    fon.home()
    
    fon.forward(x_acisi / 2)
    fon.right(90)
    fon.forward(y_acisi / 2)
    fon.setheading(180)
    
    fon.pencolor('SkyBlue')

    fon.pendown()
    fon.pensize(4)
    for mesafe in (x_acisi, y_acisi, x_acisi, y_acisi):
        fon.forward(mesafe)
        fon.right(180)

    fon.penup()
    fon.home()
def sekil (fon,buyukluk,renk):

    fon.pencolor(renk)
    fon.penup()
    for _ in range(4):
        fon.forward(buyukluk)
        fon.right(90)

def main():
    ekran = turtle.Screen()
    ekran.title('Vektörel çizdirme uygulaması v2')
    x_acisi, y_acisi = ekran.screensize()

    fon = turtle.Turtle()

    fon.speed(15)

    border(fon, x_acisi, y_acisi)

    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', "black", "red"]

    fon.pensize(3)

    for i, color in enumerate(colors):
        sekil(fon, (y_acisi / 2) / 10 * (i+1), color)

    


if __name__ == "__main__":
    main()
