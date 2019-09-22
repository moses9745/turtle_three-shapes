# CS152 Sept. 2, 2019 Unit 3-2
# David Morris
# Modified program by creating functions to remove repeating code
#   Draws 3 sets of shapes of varying lengths
#   Draw a rectangle
#   Draw a line the length of the rectangle's perimeter
#   Draw a circle with the same area as the rectangle

import turtle
import math

def next_y_position(y,ht):
    """ Returns the next y-position, given current position y and height ht """
    next = y + ht + 30
    return next

def drawRect(t, len, wid):
    """ Draws a rectangle using turtle t with sides len and wid """
    for side in [len, wid, len, wid]:
        t.forward(side)
        t.left(90)
	  
def skipForward(t,len): # New function for 1-2
    ''' Moves the turtle t forward len units without drawing anything'''
    t.penup()
    t.fd(len)
    t.pendown()

def skipTo(t, x, y): # New function for 3
    ''' Moves the turtle t to coordinates (x,y) without drawing anything'''
    t.penup()
    t.goto(x,y)
    t.pendown()

def perimeter(len,wid): # New function for 4
    ''' Returns the perimeter of rectangle with sides len and wid.'''
    perimeter = 2 * (len + wid)
    return perimeter

def cir_rad(len, wid): # New function for 5
    ''' Returns the radius of a circle with an area of len * wid '''
    results = math.sqrt(len*wid/math.pi)
    return results


def main():
    # named constants
    screen_size = 500
    screen_startx = 60 # x coordinate of the left edge of the graphics window

    # Set up the window and its attributes
    wn = turtle.Screen()              
    wn.bgcolor("lightblue")
    wn.setup(screen_size, screen_size, screen_startx, 0)

    alex = turtle.Turtle()

    # Initial turtle position near left edge, toward the bottom
    xpos = -screen_size/2 + 20 
    ypos = -screen_size/2 + 50
    
    skipTo(alex, xpos, ypos)
    #alex.up()
    #alex.goto(xpos,ypos)
    #alex.down()
    
    # y-dimension of each rectangle
    width = 50
    
    # draw three sets of shapes - same width(y-dimension) but different lengths
    for length in [25, 50, 75]:

        # Draw the rectangle
        drawRect(alex, length, width)

        # # Move a little to the right of the rectangle
        # alex.up()
        # alex.forward(length)
        # alex.forward(10)
        # alex.down() 
        #skipForward(alex, 200) # Calling new function
        

        # Draw the line the same length as the perimeter of the rectangle
        # per = 2 * (length + width)
        # alex.forward(per)
        p = perimeter(length,width) # Calling new function 

        # Move a little to the right of the line
        #alex.up()
        #alex.forward(20)
        #alex.down()
        # skipTo(alex, xpos, ypos)
        skipTo(alex, alex.xcor() + 200 , alex.ycor())

        # Draw a circle with the same area as the rectangle
        alex.begin_fill()
        rad = cir_rad(length, width) # Calling new function
        alex.circle(rad)
        alex.end_fill()

        # Next vertical position for a set of shapes
        ypos = next_y_position(ypos, width)
        
        # Put turtle to left side of screen at correct height
        alex.up()
        alex.goto(xpos,ypos)
        alex.down()        
        
    wn.exitonclick()

# Run the main function. This should be the last statement in the file.
main()


