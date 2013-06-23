'''
Created on May 18, 2013

@author: Keith Noyb
http://www.codeskulptor.org/#user12_cSYTmOBWKU_0.py
'''


import simplegui, math

major_coord_list = {} # this will be a list of 50 coord sets, each set consists of 2 coord pairs (4 coords that define startx, starty, endx and endy for each minor dash)
minor_coord_list = {} # this will be a list of 10 coord pairs in sets of 4 (40 coords in all)

def tick():
    global hand, number_of_ticks
    if clock_is_running == True:
        number_of_ticks += 1
        tenths = number_of_ticks % 10 # calculate tenth of second from number_if ticks
        angle = tenths * math.pi*2/10 # calculate angle based on tenths
        hand = get_coords(angle, -0) # assign four coords that describe out hand position to global hand variable
        

def draw_dots(): # generates coordinates  
    for x in range(50): # for the manor dashes around the outer edge of clockface
        angle = x * math.pi*2 / 50 # calculate angle based on value of x
        minor_coord_list[x] = get_coords(angle, -75) # get set of four coords for current angle and store in list
    
    for x in range(10): 
        angle = x * ((math.pi*2) / 10)
        major_coord_list[x] = get_coords(angle, -70)
       

def get_coords(angle, ydist):
    #global x1, y1, x2, y2
    x = 0 # starting x position for our dashes
    y = -80 # starting y position (from center of clock)
    # starting position at the top of the clock, calc coords based on starting position and angle
    x1 = int(x * math.cos(angle) - y * math.sin(angle))
    y1 = int(x * math.sin(angle) + y * math.cos(angle))
    x2 = int(x * math.cos(angle) - ydist * math.sin(angle))
    y2 = int(x * math.sin(angle) + ydist * math.cos(angle))
    return x1, y1, x2, y2

def start():
    global clock_is_running
    if clock_is_running == False:
        timer.start()
        clock_is_running = True
        
def stop():
    global clock_is_running, hand
    if clock_is_running == True:
        timer.stop()
        clock_is_running = False
        #print second_hand_ticks
        
        
def reset():
    global hand, clock_is_running, number_of_ticks
    hand = 0, 0, 0, -70
    timer.stop()
    clock_is_running = False
    number_of_ticks = 0
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
   
    


    


def draw(canvas):

    canvas.draw_circle((150, 100), 80, 2, "White", "Black") # draw circle
    canvas.draw_line((hand[0] + 150, hand[1] + 100), (hand[2] + 150,hand[3] + 100), 6, "Red") # draw hand
    for x in range(50):
        # draw minor dashes
        canvas.draw_line((minor_coord_list[x][0] + 150, minor_coord_list[x][1] + 100), (minor_coord_list[x][2] + 150,minor_coord_list[x][3] + 100), 1, "White")
    for y in range(10):
        # draw major dashes
        canvas.draw_line((major_coord_list[y][0] + 150,major_coord_list[y][1] + 100), (major_coord_list[y][2] + 150,major_coord_list[y][3] + 100), 4, "White")
    
        
frame = simplegui.create_frame("Testing circle", 300, 300)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_canvas_background("044040")
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)

reset() # init some variables
frame.start() # start our frame
draw_dots() # build list of coords for our clock face dashes