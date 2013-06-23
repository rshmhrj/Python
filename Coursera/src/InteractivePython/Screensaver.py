'''
Created on May 14, 2013

@author: rmaharaj
'''
import simplegui
import random

# globals
message = "Nishu & Ranveer!"
position = [100, 100]
width = 600
height = 400
interval = 1000
colors = ["Red","Orange","Yellow","Green","Blue","Pink","Violet"]
currentColor = 0

# helper functions

# classes

# event handlers
def tick():
    global currentColor
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    z = random.randrange(0, 7)
    
    position[0] = x
    position[1] = y
    currentColor = z
    

def draw(canvas):
    canvas.draw_text(message, position, 24, colors[currentColor])

def update(text):
    global message
    message = text

# create frame
# frame = simplegui.create_frame("Screensaver by Rishi", width, height)
# 
# 
# # register handlers
# frame.set_draw_handler(draw)
# frame.add_input("Enter message:", update, 200)
# timer = simplegui.create_timer(interval, tick)
# 
# # start frame/timers
# frame.start()
# timer.start()