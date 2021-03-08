import pip
import sys
import turtle
import pyautogui
sys.path
turtle.speed(0)
turtle.bgpic("city.gif")
turtle.hideturtle()
turtle.penup()
turtle.setheading(900)
turtle.forward(400)
turtle.color("white")
turtle.write("Move cursor to top left to stop program", align="left", move=False, font=("Comic Sans MS", 30, "normal"))
turtle.setheading(90)
turtle.forward(100)
turtle.write("A program to stop the library computers logging me out while I buy lunch Made by Mitchell benjamin", align="left", move=False, font=("Comic Sans MS", 10, "normal"))
while True:
    pyautogui.moveTo(200, 100)
    pyautogui.moveTo(100, 100)


