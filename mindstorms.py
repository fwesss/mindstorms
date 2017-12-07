import turtle

DEGREES = 360

def draw_square(turtle_dude):
	lines = 0
	while lines < 4:
		turtle_dude.forward(100)
		turtle_dude.right(90)
		lines = lines + 1

# def draw_circle(turtle_dude):
# 	turtle_dude.circle(100)

# def draw_triangle(turtle_dude):
# 	lines = 0
# 	while lines < 3:
# 		turtle_dude.right(120)
# 		turtle_dude.forward(100)
# 		lines = lines + 1

def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("blue")

	olivar = turtle.Turtle()
	olivar.shape("turtle")
	olivar.color("green")
	olivar.speed(9)

	squares_drawn = 0
	square_desity = 45
	while squares_drawn < square_desity:
		draw_square(olivar)
		olivar.right(DEGREES / square_desity)
		squares_drawn = squares_drawn + 1

	# tuna = turtle.Turtle()
	# tuna.shape("turtle")
	# tuna.color("grey")
	# draw_circle(tuna)

	# scout = turtle.Turtle()
	# scout.shape("arrow")
	# scout.color("red")
	# draw_triangle(scout)

	window.exitonclick()

draw_shapes()
