'''
Created on May 13, 2013

@author: Rishi Maharaj
'''
from compiler.ast import For
import math

def mathtest():
    print "this is a test!"
    
def decimal_to_binary(n):
    p = 0
    num = n
    result = ""
    found = False
    
    if n == 0:
        result += "0"
        found = True
    else:
        # find largest p where 2 ** p <= n
#         while (not found):
#             if (2 ** (p + 1)) > n:
#                 result += "1"
#                 found = True
#             else:
#                 p +=1
        p = math.log(n,2)
        n -= 2 ** p
        p -= 1
        
        result += "1"
        
        # reduce n by this amount
        if p > 0:
            n -= 2 ** p
            p -= 1
        
            while (p >= 0):
                if (2 ** p) > n:
                    result += "0"
                    p -= 1
                else:
                    result += "1"
                    n -= 2 ** p
                    p -= 1
        
    print "The decimal number", num, "equals the binary number", result
    return result

def binary_to_decimal(num):
    result = 0
    if num == 0:
        pass
    else:
        binaryNumber = str(num)
        for i in range(0, len(binaryNumber)):
            result += int(binaryNumber[i]) * (2 ** (len(binaryNumber) - 1 - i))
    print result
    return result

def decimal_to_ternary(num):
    """
    Ternary Notation uses the digits 0,1,2 in combination with the powers of three (1,3,9,...)
    Decimal 0 = Ternary 00
    Decimal 1 = Ternary 01
    Decimal 2 = Ternary 02
    Decimal 3 = Ternary 10
    Decimal 4 = Ternary 11
    Decimal 5 = Ternary 12
    Decimal 6 = Ternary 20
    etc.
    """
    p = 0
    found = False
    res = ""
    n = num
    
    if num == 0:
        res = "0"
    else:
        while not found:
            if (3 ** (p + 1)) > n:
                found = True
                res += "1"
                n -= 3 ** (p)
            elif (3 ** (p + 1) + 1) > n:
                found = True
                res += "2"
                n -= 3 ** (p) + 1
            else:
                p += 1
        p -= 1
        
        while p >= 0:
            if 3 ** p > n:
                res += "0"
            elif 3 ** (p + 1) > n:
                res += "1"
                n -= 3 ** p
            else:
                res += "2"
                n -= 3 ** (p + 1)
            p -= 1
    
    print res
    return res

def newbin(num):
    p = 0
    found = False
    res = ""
    n = num
    
    if num == 0:
        res = "0"
    else:
        while not found:
            if (2 ** (p + 1)) > n:
                found = True
            else:
                p += 1
        
        res += "1"
        
        n -= 2 ** p
        p -= 1
        
        while p >= 0:
            if (2 ** p) > n:
                res += "0"
            else:
                res += "1"
                n -= 2 ** p
            p -= 1
    
    print res
    return res
    

# newbin(9)
# newbin(0)
# newbin(1)
# newbin(2)
# newbin(10)
# newbin(100)
# newbin(16)
# newbin(33)
# newbin(64)
# newbin(256)
# newbin(37)

# print "======="
# 
# decimal_to_binary(9)
# decimal_to_binary(0)
# decimal_to_binary(1)
# decimal_to_binary(2)
# decimal_to_binary(10)
# decimal_to_binary(100)
# decimal_to_binary(16)
# decimal_to_binary(33)
# decimal_to_binary(64)
# decimal_to_binary(256)
# decimal_to_binary(37)    
# 
# print "======="
# 
# binary_to_decimal(0)
# binary_to_decimal(1)
# binary_to_decimal(10)
# binary_to_decimal(11)
# binary_to_decimal(100)
# binary_to_decimal(100101)
# binary_to_decimal(1101)
# binary_to_decimal(1011)
# binary_to_decimal(1001010)
# 
# print "======="
# 
# print 67 ^ 28
# 
# print "======="
# 
decimal_to_ternary(0)
decimal_to_ternary(1)
decimal_to_ternary(2)
decimal_to_ternary(3)
decimal_to_ternary(4)
decimal_to_ternary(5)
decimal_to_ternary(6)
decimal_to_ternary(9)
decimal_to_ternary(28)
decimal_to_ternary(30)
decimal_to_ternary(81)
decimal_to_ternary(15)
decimal_to_ternary(64)

# 
# print "======="
# 
# print math.log(64,2)