import sys
import turtle

def border(t, screen_x, screen_y):
    # Bir border oluşturmak için kullanılan fonksiyon
    # t.penup()
    # t.home()

    # t.forward(screen_x / 8)
    # t.right(90)
    # t.forward(screen_y /8)
    # t.setheading(45)

    # t.pencolor('SkyBlue')
    # t.pendown()
    # t.pensize(4)
    # for distance in (screen_x, screen_y, screen_x, screen_y):
    #     t.forward(distance)
    #     t.right(90)
    # buraya kadar commentlarsak border oluşumu gözlemlemeyiz
    t.penup()
    t.home()

def sekil(t,size,color):

    t.pencolor(color)
    t.pendown()
    for _ in range(3):
        # range'e verilen değer kaç kere etrafını döneceğiyle ilgilidir
        t.forward(size)
        t.right(120)
        # buradaki t.right fonksiyonuna değerler vererek şekilin nasıl değiştiğini gözlemleyebiliriz

def main():
    
    screen = turtle.Screen()
    screen.title('Vektörel çizdirme uygulaması v1')
    screen_x, screen_y = screen.screensize()
    t = turtle.Turtle()


    border(t, screen_x, screen_y)
    # t.speen() çizimin yapılacağı hızdır
    t.speed(30)
    # renk sayısını arttırarak şekil miktarını arttırabiliriz
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', "black", "red"]
    t.pensize(3)
    for i, color in enumerate(colors):
        sekil(t, (screen_y / 2) / 10 * (i+1), color)

    print('bir Tuşa bas')
    dummy = input()

if __name__ == "__main__":
    main()
