'''
Created on May 17, 2012

@author: Rishi Maharaj
'''
import binascii

def hex2str(a):
    return binascii.unhexlify(a);

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])