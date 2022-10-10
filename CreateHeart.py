# Importing turtle package
import turtle

pen = turtle.Turtle()
  
# Defining the curves
def curve():
    for i in range(200):
  
        # Defining pointer motion
        pen.right(1)
        pen.forward(1)
  
# Defining the method to draw a full heart
def heart():
  
    # Setting color
    pen.fillcolor('red')
    
    pen.begin_fill()
  
    # Draw the left line
    pen.left(140)
    pen.forward(113)
  
    # Draw the left curve
    curve()
    pen.left(120)
  
    # Draw the right curve
    curve()
  
    # Draw the right line
    pen.forward(112)
  
    # Ending the filling of the color
    pen.end_fill()
  

# Draw the heart
heart()
  
# To hide turtle
pen.ht()