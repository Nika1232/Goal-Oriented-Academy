import turtle
import random
def draw_rotated_text(text, x, y, angle, color):
    t = turtle.Turtle()
    t.penup()
    t.goto(x, y)  # Move to the specified coordinates
    t.color(color)
    t.setheading(angle)
    for char in text:
        t.write(char, font=("Arial", 12, "normal"))  # You can adjust the font as needed
        t.forward(10)  # Adjust spacing between characters
    t.hideturtle()
def print_coordinates(x, y):
    print("Clicked at coordinates:", x, y)
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")
screen.onclick(print_coordinates)
t = turtle.Turtle()
t.speed(0)  
def draw_triangle(base, height, color):
    t.begin_fill()
    t.color(color)
    t.left(60)
    t.forward(base / 2)
    t.right(120)
    t.forward(base)
    t.right(120)
    t.forward(base)
    t.right(120)
    t.forward(base / 2)
    t.end_fill()
def draw_rectangle(width, height, color):
    t.begin_fill()
    t.color(color)
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
#+1.5 , +10

def bow_down():
    t.penup()
    #t.goto(-90, 0)  # Position the flag
    t.setheading(45)  # change flag angle
    t.pendown()

def zeda_koshki():
    # Draw the flagpole
    bow_down()
    t.penup()
    t.goto(288, 278)
    t.pendown()
    draw_rectangle(7, 100, "brown")
    t.penup()
    t.home()
    #draw castle
    t.goto(350, 260)
    t.pendown()
    draw_rectangle(30,200,"gray")
    t.penup()
    t.goto(351.5, 270)
    draw_triangle(50,200,"gray")
    t.home()
    # Draw the flag
    bow_down()
    t.penup()
    t.goto(250, 244)
    t.pendown()
    draw_rectangle(60, 23, "red")
    draw_rotated_text("G O A", 260, 236, 45, "blue")

def polygon(a_turtle, num_side, side_length):
    '''
    The function draws a regular ploygon with the given number of sides, each
    side of the given length.

    a_turtle (turtle) - The turtle that is drawing.
    num_side (int) - Number of sides of the polygon.
    side_lenth (int) - Length of each side of the the polygon.
    '''
    
    for i in range(num_side):
        a_turtle.forward(side_length)
        a_turtle.left(360/num_side)

def house(a_turtle, size):
    '''
    Draw a simple house of the given size.
    
    a_turtle (turtle) - The turtle that is drawing.
    size (int) - Length of each side of the the polygon.
    '''
    polygon(a_turtle, 4, size)
    a_turtle.left(90)
    a_turtle.forward(size)
    a_turtle.right(90)
    polygon(a_turtle, 3,size)
    a_turtle.left(90)
    a_turtle.backward(size)
    a_turtle.right(90)
    return None

def castle(a_turtle, size):
    '''
    Draw a simple castle of the given size.

    a_turtle (turtle) - The turtle that is drawing.
    size (int) - Length of each side of the the polygon.
    '''
    polygon(a_turtle, 4, size)
    a_turtle.penup()
    a_turtle.backward(size * 0.25)
    a_turtle.left(90)
    a_turtle.forward(size)
    a_turtle.right(90)
    a_turtle.pendown()
    house(a_turtle, size * 0.5)
    a_turtle.forward(size * 0.5)
    house(a_turtle, size * 0.5)
    a_turtle.forward(size * 0.5)
    house(a_turtle, size * 0.5)
    a_turtle.penup()
    a_turtle.backward(size * 0.75)
    a_turtle.left(90)
    a_turtle.backward(size)
    a_turtle.right(90)
    a_turtle.pendown()
    return None

#==============================================
def main():
    '''Draw a castle.'''
    yertle = turtle.Turtle()
    yertle.speed(0)
    yertle.penup()
    yertle.goto(-200, -100)
    yertle.backward(100)
    yertle.pendown()
    yertle.pencolor('dark slate grey') #color
    yertle.pensize(5)

    for i in range(4):
       castle(yertle, 100)
       yertle.forward(100)

def draw_stickman(x, y, color):
    turtle.penup()
    turtle.goto(x, y-20)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(3)
    turtle.speed(0)

    # Head
    turtle.circle(10)

    # Body
    turtle.penup()
    turtle.goto(x, y-20)
    turtle.pendown()
    turtle.goto(x, y-50)

    # Arms
    turtle.penup()
    turtle.goto(x, y-30)
    turtle.pendown()
    turtle.goto(x+20, y-40)
    turtle.penup()
    turtle.goto(x, y-30)
    turtle.pendown()
    turtle.goto(x-20, y-40)

    # Legs
    turtle.penup()
    turtle.goto(x, y-50)
    turtle.pendown()
    turtle.goto(x+10, y-70)
    turtle.penup()
    turtle.goto(x, y-50)
    turtle.pendown()
    turtle.goto(x-10, y-70)

# Function to draw a crown
def draw_crown(x, y, color, scale=1):
    scaled_x = x * scale
    scaled_y = y * scale
    turtle.penup()
    turtle.goto(scaled_x - 20 * scale, scaled_y + 10 * scale)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()

    # Crown base
    turtle.goto(scaled_x + 20 * scale, scaled_y + 10 * scale)
    turtle.goto(scaled_x + 10 * scale, scaled_y + 30 * scale)
    turtle.goto(scaled_x, scaled_y + 20 * scale)
    turtle.goto(scaled_x - 10 * scale, scaled_y + 30 * scale)
    turtle.goto(scaled_x - 20 * scale, scaled_y + 10 * scale)

    turtle.end_fill()

# Create a function to draw a rect
def draw_rect(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# Create a function to draw a tri
def draw_tri(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(width)
        turtle.left(120)
    turtle.end_fill()

# Draw the castle base
def draw_castle(x, y, base_width, base_height, tower_width, tower_height, roof_height, color_base, color_roof):
    # Draw the castle base
    draw_rect(265 - base_width / 2, y - 70 / 2, base_width, base_height, color_base)

    # Draw the castle towers
    draw_rect(x - tower_width / 2, y + base_height / 2, tower_width, tower_height, color_base)
    draw_rect(x + base_width / 2 - tower_width / 2, y + base_height / 2, tower_width, tower_height, color_base)

    # Draw the castle roof
    draw_tri(217, -75 + base_height / tower_height, base_width, roof_height, color_roof)

fla_turtle = turtle.Turtle()
fla_turtle.speed(0)  # Set the fastest drawing speed

# TVINI ********* so ill just do this 
def draw_rotated_tex(text, x, y, angle, color, font_size):
    # Create a turtle for drawing text
    text_turtle = turtle.Turtle()
    text_turtle.speed(0)  # Set the fastest drawing speed
    text_turtle.penup()
    text_turtle.goto(x, y)
    text_turtle.color(color)
    text_turtle.write(text, align="center", font=("Arial", font_size, "normal"))
    text_turtle.hideturtle()
# Function to draw a filled rectangle representing the fla
fla_x = -20  # Move flag 10 units to the right
fla_y = 203   # Move flag 60 units up
def draw_fla():
    fla_turtle.penup()
    fla_turtle.goto(fla_x, fla_y)  # Move to the new flag position
    fla_turtle.pendown()
    fla_turtle.begin_fill()
    fla_turtle.color("red")
    for _ in range(2):
        fla_turtle.forward(200)
        fla_turtle.right(90)
        fla_turtle.forward(100)
        fla_turtle.right(90)
    fla_turtle.end_fill()
    draw_rotated_tex("G O A", 75, 120, 360, "blue", font_size=50) #write G O A on flag 
    draw_rotated_tex("G O A", 270, -73, 360, "blue", font_size=20) # write G O A on right bottom side castle roof


# Function to draw the flapole and set the fla on it
def draw_flapole():
    # Draw flapole
    flapole = turtle.Turtle()
    flapole.color("black")
    flapole.width(5)
    flapole.penup()
    flapole.goto(-20, 50)  # Adjust position so the fla hangs from the top
    flapole.pendown()
    flapole.goto(-20, 200)

    # Draw fla on top of the flapole
    fla_turtle.penup()
    fla_turtle.goto(-20, 50)  # Adjust position to place fla on top of the flapole
    fla_turtle.pendown()
    draw_fla()

def car():
    car = turtle.Turtle()
    car.speed(0)
    # Draw the windows
    car.penup()
    car.goto(0, -200)
    car.pendown()
    car.setheading(90)
    car.color("black")
    car.forward(50)
    car.left(90)
    car.forward(50)
    car.left(90)
    car.forward(50)

    # Draw the wheels
    car.penup()
    car.goto(-150, -250)
    car.pendown()
    car.color("black")
    car.begin_fill()
    car.circle(20)
    car.end_fill()

    car.penup()
    car.goto(-25, -250)
    car.pendown()
    car.begin_fill()
    car.circle(20)
    car.end_fill()
    car.penup()
    car.home()
# Draw the car body
    car.penup()
    car.goto(-165, -250)
    car.pendown()
    car.color("red")
    car.begin_fill()
    car.forward(200)
    car.left(90)
    car.forward(50)
    car.left(90)
    car.forward(200)
    car.left(90)
    car.forward(50)
    car.end_fill()
    draw_rotated_tex("""ჯადოსნური მფრინავი
     მანქანა BY: G O A """, -66, -245, 360, "blue", font_size=13) # different message

def field():

    field = turtle.Turtle()
    field.speed(0)  # Set the speed of the turtle

    # Draw the field
    field.penup()
    field.goto(-400, -103)
    field.pendown()
    field.color("green")
    field.setheading(0)
    field.forward(800)

    # draw another field
    field.penup()
    field.goto(250, 60)
    field.pendown()
    field.color("green")
    field.setheading(0)
    field.forward(800)
    # and again
    field.penup()
    field.goto(-400, -270)
    field.pendown()
    field.color("green")
    field.setheading(0)
    field.forward(1000)
    #one more
    field.penup()
    field.goto(-400, 100)
    field.pendown()
    field.color("green")
    field.setheading(0)
    field.forward(100)

def energy_core():

    # Create a turtle object
    vibrating_turtle = turtle.Turtle()
    vibrating_turtle.speed(0)  # Set the fastest drawing speed
    # Function to draw a vibrating circle
    def draw_vibrating_circle(radius, num_iterations, move_distance):
        for _ in range(num_iterations):
            vibrating_turtle.penup()
            vibrating_turtle.goto(-320, 230)  # Move
            vibrating_turtle.pendown()
            vibrating_turtle.circle(20)
            # Move the turtle slightly for the next iteration
            vibrating_turtle.penup()
            vibrating_turtle.setheading(vibrating_turtle.heading() + move_distance)
            vibrating_turtle.forward(10)

    # Set parameters for the vibrating circle
    radius = 100
    num_iterations = 36  # Number of vibrations
    move_distance = 10  # Distance to move for each vibration

    # Call the function to draw the vibrating circle
    draw_vibrating_circle(radius, num_iterations, move_distance)
    draw_rotated_text("GOA'S ENERGY CORE", -395, 270, 360, "red")

# Function to draw a core_rectangle
def core_rectangle(width, height):
    rectangle_turtle = turtle.Turtle()
    rectangle_turtle.speed(0)  # Set the drawing speed
    rectangle_turtle.home()
    rectangle_turtle.penup()
    rectangle_turtle.goto(-330, 100) # move
    rectangle_turtle.pendown()
    rectangle_turtle.begin_fill()  # Begin filling the shape
    rectangle_turtle.color("black")
    for _ in range(2):  # Repeat twice to draw the sides of the rectangle
        rectangle_turtle.forward(width)
        rectangle_turtle.left(90)
        rectangle_turtle.forward(height)
        rectangle_turtle.left(90)
    rectangle_turtle.end_fill()  # End filling the shape

# Function to draw a sun with vibrating rays
def draw_vibrating_sun(t, num_rays, size, amplitude, x, y):
    t.penup()
    t.goto(x, y)  # Set the coordinates where the sun will be drawn
    t.pendown()
    t.color("yellow")

    # Draw sun rays
    for _ in range(num_rays):
        t.penup()
        t.goto(x, y)  # Move to the specified coordinates for each ray
        t.pendown()
        t.setheading(random.randint(0, 360))  # Randomize angle for each ray
        for _ in range(2):
            t.forward(size + random.randint(-amplitude, amplitude))
            t.right(90)
            t.forward(10)
            t.right(90)
def sun():
    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.hideturtle()

    num_rays = 12
    size = 100
    amplitude = 10
    x = -130  # Change x-coordinate
    y = 200    # Change y-coordinate

    while True:
        t.clear()  # Clear previous drawings
        draw_vibrating_sun(t, num_rays, size, amplitude, x, y)
        amplitude += random.randint(-5, 5)  # Change the amplitude randomly
        if amplitude < 5:
            amplitude = 5
        elif amplitude > 20:
            amplitude = 20

    window.mainloop()

zeda_koshki()
main()
field()
draw_stickman(-342.0, -215, "blue")
draw_crown(-682, -440, "gold", scale=0.5)
draw_stickman(-300, -215, "red")
draw_crown(-600, -440, "gold", scale=0.5)
draw_castle(241.0, -150, 100, 150, 10, 150, 100, "gray", "red")
draw_flapole()
car()
# Set parameters for the core_rectangle
width = 20
height = 100
# Call the function to draw the core_rectangle
core_rectangle(width, height)
#call energy core after calling core rectangle
energy_core()
sun()

# Hide the turtle and display the result
t.hideturtle()
screen.mainloop()
x, y = t.pos()
print("Current position:", x, y)