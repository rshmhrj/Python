'''
Created on May 13, 2013

@author: rmaharaj
'''
import maths
import simplegui

maths.mathtest()

def dh(canvas):
    pass

f = simplegui.create_frame("Test",100,100)
f.set_draw_handler(dh)
f.start()