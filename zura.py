import turtle as t
import colorsys
t.bgcolor('black')
t.speed('fastest')
hue=0.0
for i in range(300):
  col=colorsys.hsv_to_rgb(hue,1,1)
  t.pencolor(col)
  hue += 0.005
  t.forward(i)
  t.left(200)
  t.circle(20)
t.hideturtle()
t.done()
