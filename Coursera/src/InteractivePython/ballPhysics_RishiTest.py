'''
Created on May 18, 2013

@author: rmaharaj
'''
import simplegui, math, random

# globals
WIDTH = 600
HEIGHT = 400

ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [(random.randrange(1,7)*random.choice([-1,1])),(random.randrange(1,7)*random.choice([-1,1]))]
ball_radius = 20
colors = ["White","Red","Orange","Yellow","Green","Blue"]
ball_color = colors[0]

speed_constant = 2

# helpers

# classes

# handlers
def draw(canvas):
    global ball_color
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[0] <= ball_radius:
        ball_vel[0] = -ball_vel[0]# * random.choice([.50, 1.2])
        ball_color = colors[random.randrange(0,6)]
    if ball_pos[0] >= WIDTH - ball_radius - 1:
        ball_vel[0] = -ball_vel[0]# * random.choice([1.50, .2])
        ball_color = colors[random.randrange(0,6)]
    if ball_pos[1] <= ball_radius:
        ball_vel[1] = -ball_vel[1]# * random.choice([.50, .2])
        ball_color = colors[random.randrange(0,6)]
    if ball_pos[1] >= HEIGHT - ball_radius - 1:
        ball_vel[1] = -ball_vel[1]# * random.choice([.50, 1.2])
        ball_color = colors[random.randrange(0,6)]
    
    canvas.draw_circle(ball_pos, ball_radius, 12, ball_color, ball_color)

def keydown(key):
    if key == simplegui.KEY_MAP["left"]:
        ball_vel[0] -= 1*speed_constant
    if key == simplegui.KEY_MAP["right"]:
        ball_vel[0] += 1*speed_constant
    if key == simplegui.KEY_MAP["up"]:
        ball_vel[1] -= 1*speed_constant
    if key == simplegui.KEY_MAP["down"]:
        ball_vel[1] += 1*speed_constant

def keyup(key):
    if key == simplegui.KEY_MAP["left"]:
        ball_vel[0] += 1*speed_constant
    if key == simplegui.KEY_MAP["right"]:
        ball_vel[0] -= 1*speed_constant
    if key == simplegui.KEY_MAP["up"]:
        ball_vel[1] += 1*speed_constant
    if key == simplegui.KEY_MAP["down"]:
        ball_vel[1] -= 1*speed_constant
    else:
        ball_vel[0] = 0
        ball_vel[1] = 0

def timer_handler():
    global ball_vel, ball_color
    ball_vel[random.randrange(0,2)] = random.randrange(0,11)
    ball_color = colors[random.randrange(0,6)]

def reset():
    global ball_pos, ball_vel, ball_color
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [(random.randrange(1,7)*random.choice([-1,1])),(random.randrange(1,7)*random.choice([-1,1]))]
    ball_color = colors[0]
    
def vel_up():
    global ball_vel
    ball_vel[0] = ball_vel[0] * 1.2
    ball_vel[1] = ball_vel[1] * 1.2
    
def vel_down():
    global ball_vel
    ball_vel[0] = ball_vel[0] * .8
    ball_vel[1] = ball_vel[1] * .8

def vel_change():
    global ball_vel
    ball_vel = [random.randrange(1,7),random.randrange(1,7)]

# frame
frame = simplegui.create_frame("Test", WIDTH, HEIGHT)

# register handlers
reset = frame.add_button("Reset", reset, 100)
vel_up = frame.add_button("Velocity Up", vel_up, 100)
vel_down = frame.add_button("Velocity Down", vel_down, 100)
vel_change = frame.add_button("Change Direction", vel_change, 100)

frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(1000,timer_handler)

# start
frame.start()
#timer.start()