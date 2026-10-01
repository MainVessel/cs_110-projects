import turtle
def main():
  sides = int(input("How many sides in your shape? "))
  length = float(input("How big is your shape? "))
  turt = turtle.Turtle()
  angle = 360 / sides
  for i in range(sides):
    turt.forward(length)
    turt.right(angle)
  turtle.done()

main()
