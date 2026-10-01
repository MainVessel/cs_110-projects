import turtle
my_turtle_obj = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")
my_turtle_obj.shape("turtle")
my_turtle_obj.color("green")
for square in range (4):
    my_turtle_obj.forward(150)
    my_turtle_obj.right(90)
my_turt_obj=turtle.Turtle()
my_turt_obj.shape("turtle")
my_turt_obj.color("blue")
my_turt_obj.up()
my_turt_obj.goto(-100,100)
my_turt_obj.down()
for square in range (4):
    my_turt_obj.forward(150)
    my_turt_obj.right(90)
window.exitonclick()
