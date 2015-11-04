import turtle
import time
'''
numbers=[1,2,3]
calculate=0
for i in numbers:
	print i
	print i*2
	calculate+=i
print calculate
'''
speed=1
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.width(5)
turtle.ht()
colors=['blue','red','green','yellow','pink','brown','purple']
for color in colors:
	speed+=1
	turtle.speed(speed)		
	turtle.begin_fill()
	turtle.color(color)
	'''
	sturtle.goto(0,100)
	turtle.goto(100,100)
	turtle.goto(100,0)
	turtle.goto(0,0)
	'''
	turtle.circle(100)
	turtle.end_fill()
	time.sleep(0.3)