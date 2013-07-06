'''
Created on May 30, 2013

@author: rmaharaj
@summary:
Flow:
1    Start program
2    Enter the file name
     - If new file, it must be created, then opened.
     - If existing file, it should be opened.
3    Select Read or Write mode.
    3a Read:
     - If new file, displays nothing.
     - If existing file, displays numbers in the file, one per line.
    3b Write:
     - Prompt for quantity of numbers to be recorded > n
     - Prompt for each of the n numbers to be entered, one at a time.
4    Program saves any appended numbers to file.
5    Program ends.
'''
# --#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#
# Reuse Instructions
# program1b(filename, entryMode)
# Purpose: to open filename in mode <entryMode>
#     and either read the file or write numbers
#     to the file.
# filename must be a file, not a path
# entryMode can only be "Read" or "Write"
# --#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#


# imported methods
import math, re

# define global variables
# filename will hold the file which will be opened
# entryMode will be 0 for Read, 1 for Write
filename = ""
entryMode = 0
areEntriesCorrect = False

# the main method will prompt the user for the filename, the entry method,
# and verify that the values entered by the user are valid
# if it is, it will pass control to the body() method
# otherwise, the program will end.
def main():
    global areEntriesCorrect
    print "Welcome!"
    print "This program will either read from"
    print "or write to a file a series of n real numbers.\n"

    # prompt for entry of file name
    path = raw_input("Please enter the file name using the format C:\\folder\\folder\\filename.ext")

    # prompt for entry of mode: read or write
    mode = raw_input("Please enter the mode: Read or Write")

    if check_filename(path) and check_entryMode(mode):
        set_filename(path)
        set_entryMode(mode)
        areEntriesCorrect = True
        body()
    else:
        areEntriesCorrect = False
        print "Please re-run the program and fix your entries."

def body():
    if entryMode == 0:
        read_from_file()
    elif entryMode == 1:
        write_to_file()
    else:
        "Entry mode error in body."

def read_from_file():
    file_to_read = open(filename, 'r+')
    file_to_read.read()
    file_to_read.close()

def write_to_file():
    file_to_write = open(filename, 'w+')

    # prompt for quantity of numbers
    numberQuantity = raw_input("Please enter n, the quantity of digits to be entered. (INTEGERS ONLY)")
    n = 0

    while (n == 0):
        if is_valid_integer(numberQuantity):
            n = int(numberQuantity)
        else:
            numberQuantity = raw_input("Please enter a valid integer:")

    numbers = []
    validNumber = False
    for i in range(0, n):
        num = raw_input("Please enter a number:")
        while not validNumber:
            if is_valid_number(num):
                numbers.append(num)
                validNumber = True
            else:
                num = raw_input("Please enter a valid number:")
                validNumber = False

    file_to_write.writelines(numbers)
    file_to_write.close()

def is_valid_number(num):
    pattern = re.compile(r'[-0-9]')
    return pattern.match(num)

def is_valid_integer(num):
    if (num.find("-") == -1) and (num.find(".") == -1) and (int(num) > 0):
        return True
    else:
        print "That was not a valid number."
        return False

def get_filename():
    print "File Name:", filename
    return filename

def set_filename(value):
    global filename
    filename = value

def get_entryMode():
    print "Entry Mode:", entryMode
    return entryMode

def set_entryMode(value):
    global entryMode
    if value == "Write":
        entryMode = 1
    else:
        entryMode = 0

def check_filename(value):
    if type(value) == str:
        return True
    else:
        print "There is an error in your file name:", type(value)
        return False

def check_entryMode(value):
    if (str(value) == "Read") or (str(value) == "Write"):
        return True
    else:
        print "There is an error in your entry mode:", value
        return False

main()
