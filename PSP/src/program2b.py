'''
Created on Jun 5, 2013

@author: rmaharaj
@summary: This program will either read a file, write to a file, or modify a file.
'''
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#
# Reuse Instructions
# program1b(filename, entryMode)
# Purpose: to open filename in mode <entryMode>
#     and either read the file or write numbers
#     to the file.
# filename must be a file, not a path 
# entryMode can only be "Read" or "Write"
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#


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
    print "Welcome! This program will either read from, write to, or modify a file of numbers.\n"
    
    # prompt for entry of file name
    path = raw_input("Please enter the full file path & file name:")
    
    # prompt for entry of mode: read or write
    mode = raw_input("\nPlease enter the mode: Read, Write, or Modify")
    
    if check_filename(path) and check_entryMode(str(mode).lower()):
        set_filename(path)
        set_entryMode(str(mode).lower())
        areEntriesCorrect = True
        body()
    else:
        areEntriesCorrect = False
        print "\nPlease re-run the program and fix your entries."
    
def body():
    if entryMode == 0:
        read_from_file()
    elif entryMode == 1:
        write_to_file()
    elif entryMode == 2:
        modify_file()
    else:
        print "Entry mode error in body."
        
def read_from_file():
    file_to_read = open(filename, 'r')
    print file_to_read.read()
    file_to_read.close()

def write_to_file():
    file_to_write = open(filename, 'w')
    
    # prompt for quantity of numbers
    numberQuantity = raw_input("\nPlease enter n, the quantity of digits to be entered. (INTEGERS ONLY)")
    n = 0
    
    while (n == 0):
        if is_valid_integer(numberQuantity):
            n = int(numberQuantity)
        else:
            numberQuantity = raw_input("Please enter a valid integer:")
    
    numbers = []
    for i in range(0,n):
        numbers.append(number_prompt(True))
  
    with file_to_write as f:
        f.writelines("\n".join(numbers))
    file_to_write.close()
    
def number_prompt(firstTime):
    validNumber = False
    if firstTime:
        msg = "\nPlease enter a number:"
    else:
        msg = "\nPlease enter a replacement number:"
    num = raw_input(msg)
    while not validNumber:
        if is_valid_number(num):
            validNumber = True
        else:
            num = raw_input("Please enter a valid number:")
            validNumber = False
    return num

def modify_prompt():
    validAction = False
    while not validAction:
        modify_action = raw_input("\nPlease enter a valid action: Accept, Replace, or Delete.")
        if check_modifyAction(modify_action):
            validAction = True
    return str(modify_action).lower()
    
def modify_file():
    file_to_modify = open(filename, 'r+')
    numbers = file_to_modify.read().split()
    file_to_modify.close()
    
    print "\nFor each of the following numbers, please choose Accept, Replace, or Delete"
    
    acceptAll = False
    insertedNumber = False
    # for each num in file, read -> accept, replace, delete
    for i, num in enumerate(numbers):
        if not acceptAll:
            print "\nPosition:", i + 1, ";   Number:", num
            modify_action = modify_prompt()
            
            if modify_action == "accept":
                continue
            elif modify_action == "replace":
                numbers[i] = number_prompt(False)
            elif modify_action == "delete":
                numbers.pop(i)
            else:
                print "Please enter a valid action", modify_action
            
        # insert new num after, or before any other num
            countNumbersLeft = len(numbers) - (i + 1)
            print "\nThere are", str(countNumbersLeft), "numbers between this number and the end of the file."
            doInsert = yes_no_prompt("Would you like to insert a number? Yes or No:")
            
            if doInsert == "yes":
                insert_where = insert_where_prompt(countNumbersLeft)
                numbers.insert(int(insert_where), number_prompt(True))
            
            elif doInsert == "no":
                pass
            else:
                print "Incorrect entry"
                pass
            
        # accept all after
            shouldAcceptAll = yes_no_prompt("\nWould you like to Accept all remaining numbers? Yes or No:")
            if shouldAcceptAll == "yes":
                acceptAll = True
                continue
        
        # save or save as
        else:
            pass
    else:
        pass
    
    saveOrSaveAs = save_or_saveAs_prompt("\nWould you like to save the current file, or save as a new file? Save / SaveAs (ONE WORD):")
    if saveOrSaveAs[0]:
        fileToSave = ""
        if saveOrSaveAs[1] == "save":
            fileToSave = filename
        elif saveOrSaveAs[1] == "saveas":
            fileToSave = filename_prompt("\nPlease enter the new full file path & file name:")
        else:
            print "Error, incorrect save/saveas entry. Not saving file."
            
        if fileToSave == "":
            pass
        else:
            file = open(fileToSave, 'w')
            file.truncate()
            with file as f:
                f.writelines("\n".join(numbers))
                file.close()
        
    print "End:", numbers
    
def filename_prompt(msg):
    validFilename = False
    while not validFilename:
        name = raw_input(msg)
        if check_filename(name):
            validFilename = True
        else:
            "Please enter a valid filename."
    return name

def save_or_saveAs_prompt(msg):
    validAnswer = False
    while not validAnswer:
        answer = raw_input(msg)
        if str(answer.lower()) == "save" or str(answer.lower()) == "saveas":
            validAnswer = True
        else:
            print "You did not enter a valid choice:", str(answer)
    return [True, answer.lower()]

def insert_where_prompt(end):
    validWhere = False
    while not validWhere:
        msg = "Where do you want to insert the number? 1 = after this number, ..., " + str(end) + ", before last number."
        where = raw_input(msg)
        if is_valid_integer(where) and int(where) > 0 and int(where) <= end:
            validWhere = True
        else:
            validWhere = False
            print "INVALID Entry Choice!", str(where)
    return where.lower()
    
def yes_no_prompt(msg):
    validAnswer = False
    while not validAnswer:
        answer = raw_input(msg)
        if str(answer.lower()) == "yes" or str(answer.lower()) == "no":
            validAnswer = True
        else:
            print "You did not enter a valid choice:", str(answer)
    return answer.lower()
    
def is_valid_number(num):
    pattern = re.compile(r'-?[1-9]+\d*[.]?[0-9]*\Z')
    if pattern.match(num):
        return True
    else:
        return False

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
    if value == "write":
        entryMode = 1
    elif value == "modify":
        entryMode = 2
    else:
        entryMode = 0

def check_filename(value):
    if type(value) == str:
        return True
    else:
        print "There is an error in your file name:", type(value)
        return False

def check_entryMode(value):
    if (value == "read") or (value == "write") or (value == "modify"):
        return True
    else:
        print "There is an error in your entry mode:", value
        return False

def check_modifyAction(value):
    if (value == "accept") or (value == "replace") or (value == "delete"):
        return True
    else:
        print "There is an error in your modify Action:", value
        return False

main()
