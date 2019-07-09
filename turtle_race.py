import os
import random
import subprocess
import turtle
#import pydub
#from playsound import playsound #

#from IPython.display import Audio
#sound_file = 'turtle_welcome.wav'

#Audio('turtle_welcome.wav', autoplay=True)

def get_heading():
    distance = random.randint(1,10)
    heading = random.randint(1,20)
    heading = heading - 10
    return (distance,heading)
def f():
    fd(50)
    lt(60)
race_on = 1
finish = 300

main_screen = turtle.Screen()
main_screen.bgcolor("green")
main_screen.title("turtle race")

#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("brown")
border_pen.penup()
border_pen.setposition((-1*finish),(-1*finish))
border_pen.pensize(5)
border_pen.pendown()
for side in range(4):
    border_pen.fd((2*finish))
    border_pen.lt(90)
border_pen.hideturtle()

result_message = turtle.Turtle()
result_message.shape("circle")
result_message.color("brown")

t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("blue")
t1.speed(2)

t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("pink")
t2.setheading(90)
t2.speed(2)

t3 = turtle.Turtle()
t3.shape("turtle")
t3.color("yellow")
t3.setheading(180)
t3.speed(2)

t4 = turtle.Turtle()
t4.shape("turtle")
t4.color("purple")
t4.setheading(270)
t4.speed(2)
#select turtle
#while (True):
    #screen.onkey(f, "Up")
    #screen.listen()
    #break
#screen.textinput("NIM", "Pick your turtle:")
#os.spawn(playsound('turtle_welcome.mp3'))

#playsound('turtle_welcome.mp3') #annoying that this runs in the forground, I would much rather this run in bg or thread it
#subprocess.playsound('turtle_welcome.mp3')

player_turtle = int(main_screen.numinput("Pick your turtle","1-4", minval=1, maxval=4))
t1place = 4
t2place = 4
t3place = 4
t4place = 4
while race_on < 4:
    #if t1.isdown()
    if (t1.isdown()):
        t1c = get_heading()
        t1h = t1.heading()
        t1h = t1h + t1c[1]
        t1.setheading(t1h)
        t1.fd(t1c[0])
    if (t2.isdown()):
        t2c = get_heading()
        t2h = t2.heading()
        t2h = t2h + t2c[1]
        t2.setheading(t2h)
        t2.fd(t2c[0])
    if (t3.isdown()):
        t3c = get_heading()
        t3h = t3.heading()
        t3h = t3h + t3c[1]
        t3.setheading(t3h)
        t3.fd(t3c[0])
    if (t4.isdown()):
        t4c = get_heading()
        t4h = t4.heading()
        t4h = t4h + t4c[1]
        t4.setheading(t4h)
        t4.fd(t4c[0])
    
    (t1x,t1y) = t1.position()
    if(t1x > finish or -1*t1x > finish):
        if (t1.isdown()):
            #t1.write("turtle finished")
            #t1.write(race_on)
            t1place = race_on
            if (t1place == 1):
                t1.write("     turtle finished first")
            if (t1place == 2):
                t1.write("     turtle finished second")
            if (t1place == 3):
                t1.write("     turtle finished third")
            t1.penup()
            race_on = race_on + 1
        
    if(t1y > finish or -1*t1y > finish):
        if (t1.isdown()):
            t1place = race_on
            if (t1place == 1):
                t1.write("     turtle finished first")
            if (t1place == 2):
                t1.write("    turtle finished second")
            if (t1place == 3):
                t1.write("    turtle finished third")
            t1.penup()
            race_on = race_on + 1
    
    (t2x,t2y) = t2.position()
    if(t2x > finish or -1*t2x > finish):
        if (t2.isdown()):
            
            #t2.write("turtle finished")
            t2place = race_on
            if (t2place == 1):
                t2.write("      turtle finished first")
            if (t2place == 2):
                t2.write("      turtle finished second")
            if (t2place == 3):
                t2.write("     turtle finished third")
            t2.penup()
            race_on = race_on + 1
    if(t2y > finish or -1*t2y > finish):
        if (t2.isdown()):
            t2place = race_on
            if (t2place == 1):
                t2.write("     turtle finished first")
            if (t2place == 2):
                t2.write("     turtle finished second")
            if (t2place == 3):
                t2.write("     turtle finished third")
           
            t2.penup()
            race_on = race_on + 1
    
    (t3x,t3y) = t3.position()
    if(t3x > finish or -1*t3x > finish):
        if (t3.isdown()):
            t3place = race_on
            if (t3place == 1):
                t3.write("     turtle finished first")
            if (t3place == 2):
                t3.write("     turtle finished second")
            if (t3place == 3):
                t3.write("     turtle finished third")
            t3.penup()
            race_on = race_on + 1
    if(t3y > finish or -1*t3y > finish):
        if (t3.isdown()):
            t3place = race_on
            if (t3place == 1):
                t3.write("     turtle finished first")
            if (t3place == 2):
                t3.write("     turtle finished second")
            if (t3place == 3):
                t3.write("     turtle finished third")
            t3.penup()
            race_on = race_on + 1
    
    (t4x,t4y) = t4.position()
    if(t4x > finish or -1*t4x > finish):
        if (t4.isdown()):
            t4place = race_on
            if (t4place == 1):
                t4.write("     turtle finished first")
            if (t4place == 2):
                t4.write("     turtle finished second")
            if (t4place == 3):
                t4.write("     turtle finished third")
            t4.penup()
            race_on = race_on + 1
    if(t4y > finish or -1*t4y > finish):
        if (t4.isdown()):
            t4place = race_on
            if (t4place == 1):
                t4.write("     turtle finished first")
            if (t4place == 2):
                t4.write("     turtle finished second")
            if (t4place == 3):
                t4.write("     turtle finished third")
            t4.penup()
            race_on = race_on + 1
        
    
if (player_turtle == 1 and t1place == 1):
    #win
    win = True
elif (player_turtle == 2 and t2place == 1):
    #win
    win = True
elif (player_turtle == 3 and t3place == 1):
    #win
    win = True
elif (player_turtle == 4 and t4place == 1):
    #win
    win = True
else:
    #lose
    win = False



if (win):
    result_message.pencolor("black")
    result_message.write("      Congratulations, your turtle was lucky and your wish will surely come true")
else:
    result_message.pencolor("black")
    result_message.write("      Sorry, your turtle was unlucky and your wish may not come true for a little while")
        
    #t2c = get_heading()
    #t3c = get_heading()
    #t4c = get_heading()
    
turtle.exitonclick()  
print("Goodbye")
turtle.bye()
