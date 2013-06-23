'''
Created on May 18, 2013

@author: rmaharaj
'''

# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

# Ball Variables
ball_pos = [WIDTH / 2, HEIGHT /2]
ball_vel = [0, 0]
right = True

# Paddle Variables
paddle_speed_constant = 10
paddle1_pos = [4, HEIGHT / 2]
paddle1_top = [paddle1_pos[0], paddle1_pos[1] - (PAD_HEIGHT / 2)]
paddle1_bot = [paddle1_pos[0], paddle1_pos[1] + (PAD_HEIGHT / 2)]
paddle1_vel = [0, 0]

paddle2_pos = [WIDTH - 4, HEIGHT / 2]
paddle2_vel = [0, 0]
paddle2_top = [paddle2_pos[0], paddle2_pos[1] - (PAD_HEIGHT / 2)]
paddle2_bot = [paddle2_pos[0], paddle2_pos[1] + (PAD_HEIGHT / 2)]

# Score Tracker Variables
score1 = 0
score1_pos = [(WIDTH / 2) - 35, 40]
score2 = 0
score2_pos = [(WIDTH / 2) + 20, 40]

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT /2]
    
    # NOTE: I thought the suggested ranges were too fast to be playable
    h_vel = random.randrange(3, 10)#random.randrange(120, 240)
    v_vel = random.randrange(1, 10)#random.randrange(60, 180)
    
    if not right:
        h_vel *= -1
    
    ball_vel = [h_vel, v_vel]

# helper function that checks if a paddle hits the ball or not
def isHit(paddle):
    if paddle == 1:
        if (ball_pos[1] >= paddle1_top[1]) and (ball_pos[1] <= paddle1_bot[1]):
            return True
        else:
            return False
    else:
        if (ball_pos[1] >= paddle2_top[1]) and (ball_pos[1] <= paddle2_bot[1]):
            return True
        else:
            return False

# define event handlers

def new_game():
    # NOTE: I chose not to reset the paddles, only the scores and ball
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    ball_init(random.choice([True, False]))
    score1 = 0
    score2 = 0

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_top, paddle1_bot, paddle2_top, paddle2_bot
    global pad1_up, pad1_down, pad2_up, pad2_down
 
    # update paddle's vertical position, keep paddle on the screen
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    paddle1_pos[0] += paddle1_vel[0]
    paddle1_pos[1] += paddle1_vel[1]


    paddle2_pos[0] += paddle2_vel[0]
    paddle2_pos[1] += paddle2_vel[1]
    paddle2_top = [paddle2_pos[0], paddle2_pos[1] - (PAD_HEIGHT / 2)]
    paddle2_bot = [paddle2_pos[0], paddle2_pos[1] + (PAD_HEIGHT / 2)]
    
    # Paddle Collision Rules
    if (paddle1_pos[1] <= (PAD_HEIGHT/2)):
        paddle1_top = [paddle1_pos[0], 0]
        paddle1_bot = [paddle1_pos[0], PAD_HEIGHT]
    elif (paddle1_pos[1] >= (HEIGHT - 1 - (PAD_HEIGHT/2))):
        paddle1_top = [paddle1_pos[0], HEIGHT - PAD_HEIGHT]
        paddle1_bot = [paddle1_pos[0], HEIGHT - 1]
    else:
        paddle1_top = [paddle1_pos[0], paddle1_pos[1] - (PAD_HEIGHT / 2)]
        paddle1_bot = [paddle1_pos[0], paddle1_pos[1] + (PAD_HEIGHT / 2)]

    if (paddle2_pos[1] <= (PAD_HEIGHT/2)):
        paddle2_top = [paddle2_pos[0], 0]
        paddle2_bot = [paddle2_pos[0], PAD_HEIGHT]
    elif (paddle2_pos[1] >= (HEIGHT - 1 - (PAD_HEIGHT/2))):
        paddle2_top = [paddle2_pos[0], HEIGHT - PAD_HEIGHT]
        paddle2_bot = [paddle2_pos[0], HEIGHT - 1]
    else:
        paddle2_top = [paddle2_pos[0], paddle2_pos[1] - (PAD_HEIGHT / 2)]
        paddle2_bot = [paddle2_pos[0], paddle2_pos[1] + (PAD_HEIGHT / 2)]
    
    c.draw_line(paddle1_top, paddle1_bot, PAD_WIDTH, "White")
    c.draw_line(paddle2_top, paddle2_bot, PAD_WIDTH, "White")
     
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
   # Ball Collision Rules
        # NOTE: I thought that the 10% ball velocity increase was
        # too easy, so made it increase by 20% instead
    # Horizontal
        #Left Edge
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if isHit(1):
            ball_vel[0] = -ball_vel[0]*1.2
        else:
            score2 += 1
            ball_init(True)
        #Right Edge
    if ball_pos[0] >= (WIDTH - 1) - BALL_RADIUS - PAD_WIDTH:
        if isHit(2):
            ball_vel[0] = -ball_vel[0]*1.2
        else:
            score1 += 1
            ball_init(False)
    # Vertical
        #Upper Edge
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        #Lower Edge
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    c.draw_text(str(score1), score1_pos, 30, "White")
    c.draw_text(str(score2), score2_pos, 30, "White")
        
        
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["W"]:
        if (paddle1_pos[1] < (PAD_HEIGHT/2)):
            paddle1_vel[1] = 0
        else:
            paddle1_vel[1] -= 1*paddle_speed_constant
        print 'pos =',paddle1_pos,'vel =',paddle1_vel
        
    if key == simplegui.KEY_MAP["S"]:
        if (paddle1_pos[1] > (HEIGHT - PAD_HEIGHT/2 - 1)):
            paddle1_vel[1] = 0
        else:
            paddle1_vel[1] += 1*paddle_speed_constant
        print 'pos =',paddle1_pos,'vel =',paddle1_vel
        
    if key == simplegui.KEY_MAP["up"]:
        if (paddle2_pos[1] < (PAD_HEIGHT/2)):
            paddle2_vel[1] = 0
        else:
            paddle2_vel[1] -= 1*paddle_speed_constant
        print 'pos =',paddle2_pos,'vel =',paddle2_vel
        
    if key == simplegui.KEY_MAP["down"]:
        if (paddle2_pos[1] > (HEIGHT - PAD_HEIGHT/2 - 1)):
            paddle2_vel[1] = 0
        else:
            paddle2_vel[1] += 1*paddle_speed_constant
        print 'pos =',paddle2_pos,'vel =',paddle2_vel
   
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["W"]:
        if (paddle1_pos[1] < (PAD_HEIGHT/2)):
            paddle1_vel[1] = 0
        else:
            paddle1_vel[1] += 1*paddle_speed_constant
        print 'pos =',paddle1_pos,'vel =',paddle1_vel
        
    if key == simplegui.KEY_MAP["S"]:
        if (paddle1_pos[1] > (HEIGHT - PAD_HEIGHT/2 - 1)):
            paddle1_vel[1] = 0
        else:
            paddle1_vel[1] -= 1*paddle_speed_constant
        print 'pos =',paddle1_pos,'vel =',paddle1_vel
        
    if key == simplegui.KEY_MAP["up"]:
        if (paddle2_pos[1] < (PAD_HEIGHT/2)):
            paddle2_vel[1] = 0
        else:
            paddle2_vel[1] += 1*paddle_speed_constant
        print 'pos =',paddle2_pos,'vel =',paddle2_vel
        
    if key == simplegui.KEY_MAP["down"]:
        if (paddle2_pos[1] > (HEIGHT - PAD_HEIGHT/2 - 1)):
            paddle2_vel[1] = 0
        else:
            paddle2_vel[1] -= 1*paddle_speed_constant
        print 'pos =',paddle2_pos,'vel =',paddle2_vel
   
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
reset_button = frame.add_button("Reset Game", new_game, 100)


# start frame
frame.start()
new_game()
