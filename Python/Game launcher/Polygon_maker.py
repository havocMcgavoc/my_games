import turtle
tom = turtle.Pen()

def polygon():
    def shape(shape_sides):
        for i in range(shape_sides):
            tom.forward(100)
            tom.left(360/shape_sides)

    while True:
        try:
            shape_sides = int(turtle.textinput("shape", "Enter the number of sides you want your shape to have."))
            while shape_sides <= 2:
                shape_sides = int(turtle.textinput("shape",f"There is no polygon existing with {shape_sides} sides. Choose another number"))

            break
        except ValueError:
            print("Please enter an integer value")
    shape(shape_sides)
    if __name__ == '__main__':
        print("Run the code again to draw another polygon")
    turtle.done()