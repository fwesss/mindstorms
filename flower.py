import turtle

DEGREES = 360
PETALS = 36

def draw_petal(my_turtle):
	my_turtle.circle(50)

def draw_flower():
	window = turtle.Screen()

	scooter = turtle.Turtle()
	scooter.color("blue")
	scooter.speed(0)


	petals_drawn = 0
	while petals_drawn < PETALS:
		draw_petal(scooter)
		scooter.right(DEGREES / PETALS)
		petals_drawn = petals_drawn + 1

	scooter.color("green")
	scooter.right(90)
	scooter.forward(350)

	window.exitonclick()

draw_flower()
