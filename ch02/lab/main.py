import turtle  # 1. import modules
import random
def main():
    # Part A
    window = turtle.Screen()  # 2.  Create a screen
    window.bgcolor("lightblue")

    michelangelo = turtle.Turtle()  # 3.  Create two turtles
    leonardo = turtle.Turtle()
    michelangelo.color("orange")
    leonardo.color("blue")
    michelangelo.shape("turtle")
    leonardo.shape("turtle")

    michelangelo.up()  # 4. Pick up the pen so we don’t get lines
    leonardo.up()
    michelangelo.goto(-100, 20)
    leonardo.goto(-100, -20)

    ## 5. Your PART A code goes here
    
    # Race 1
    michelangelo.goto(-100, 20)
    leonardo.goto(-100, -20)

    michelangelo.forward(random.randrange(1, 101))
    leonardo.forward(random.randrange(1, 101))

    michelangelo.goto(-100, 20)
    leonardo.goto(-100, -20)

    # Race 2
    for count in range(10):
        michelangelo.forward(random.randrange(1, 11))
        leonardo.forward(random.randrange(1, 11))
    
    michelangelo.goto(-100, 20)
    leonardo.goto(-100, -20)


    # PART B - complete part B here
    number_of_sides = 0
    turning_angle = 0
    side_length = 0

    # Triangle
    michelangelo.down()
    number_of_sides = 3
    side_length = 50
    for x in range(number_of_sides):
        michelangelo.forward(side_length)
        michelangelo.left(360/3)
    michelangelo.clear()

     # Square
    michelangelo.down()
    number_of_sides = 4
    side_length = 50
    for x in range(number_of_sides):
         michelangelo.forward(side_length)
         michelangelo.left(360/number_of_sides)
    michelangelo.clear()

    # Hexagon
    michelangelo.down()
    number_of_sides = 6
    side_length = 50
    for x in range(number_of_sides):
        michelangelo.forward(side_length)
        michelangelo.left(360/number_of_sides)
    michelangelo.clear()

    # Icosagon
    michelangelo.down()
    number_of_sides = 20
    side_length = 50
    for x in range(number_of_sides):
            michelangelo.forward(side_length)
            michelangelo.left(360/number_of_sides)
    michelangelo.clear()

    # Hectogon
    michelangelo.down()
    number_of_sides = 100
    side_length = 5
    for x in range(number_of_sides):
            michelangelo.forward(side_length)
            michelangelo.left(360/number_of_sides)
    michelangelo.clear()

    # "Circle"
    michelangelo.down()
    number_of_sides = 1000
    side_length = 5
    for x in range(number_of_sides):
          michelangelo.forward(side_length)
          michelangelo.left(360/number_of_sides)
    michelangelo.clear()





    
    
    






    window.exitonclick()

main()