'''
Created on May 18, 2013

@author: rmaharaj
'''
# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
win = 0
loss = 0
A = "0"
B = "0"
C = "0"
D = "0"
started = False
stopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global A, B, C, D
   
    temp = str(t)
    if t < 10:
        D = temp[0]
    elif t < 100:
        C = temp[0]
        D = temp[1]
    elif t < 600:
        B = temp[0]
        C = temp[1]
        D = temp[2]
    elif t < 1000:
        A = str(t // 600)
        B = str((t % 600) // 100)
        C = temp[1]
        D = temp[2]
    else:
        A = str(t // 600)
        B = str((t % 600) // 100)
        C = temp[2]
        D = temp[3]
    return A+":"+B+C+"."+D
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global started, stopped
    timer.start()
    started = True
    stopped = False

def stop_handler():
    global win, loss, started, stopped
    timer.stop()
    if not stopped:
        if time % 10 == 0:
            win += 1
        loss +=1
    started = False
    stopped = True
        

def reset_handler():
    global time, A, B, C, D, win, loss
    time = 0
    A = "0"
    B = "0"
    C = "0"
    D = "0"
    win = 0
    loss = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), (160,200), 48, "Red")
    canvas.draw_text(str(win) + " / " + str(loss), (315,50), 24, "Grey")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 400, 400)


# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
frame.add_button("Start",start_handler,100)
frame.add_button("Stop",stop_handler,100)
frame.add_button("Reset",reset_handler,100)

# start frame
frame.start()

# Please remember to review the grading rubric
