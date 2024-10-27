import turtle

def draw_tree(branch_length, angle, depth, t):
    if depth == 0:
        return
    t.forward(branch_length)
    t.left(angle)
    draw_tree(branch_length * 0.7, angle, depth - 1, t)
    t.right(2 * angle)
    draw_tree(branch_length * 0.7, angle, depth - 1, t)
    t.left(angle)
    t.backward(branch_length)

t = turtle.Turtle()
screen = turtle.Screen()
t.speed(0)
t.left(90)
t.up()
t.goto(0, -250)
t.down()

draw_tree(branch_length=100, angle=30, depth=5, t=t)
screen.mainloop()
