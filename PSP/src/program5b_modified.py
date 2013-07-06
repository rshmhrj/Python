'''
Created on Jun 15, 2013

@author: rmaharaj
@summary: This program will either read a file, write to a file, or modify a file.
'''
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#
# Reuse Instructions
# N/A
#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#--#

# imported methods
from lib import prompts as prompts

# define global variables
# filename will hold the file which will be opened
# entryMode will be 0 for Read, 1 for Write
# maxArraySize represents the maximum number of elements in an inputted array (K)
filename = ""
entryMode = 0
maxArraySize = 10

# the main method will prompt the user for the filename, the entry method,
# and verify that the values entered by the user are valid
# if it is, it will pass control to the body() method
# otherwise, the program will end.
def main():
    print "Welcome! This program will either read from, write to, or modify a file of numbers.\n"
    
    # prompt for entry of file name & entry mode, and set global variables
    set_entryMode(prompts.entry_mode_prompt("\nPlease enter the mode: Read, Write, or Modify"))
    set_filename(prompts.filename_prompt("Please enter the full file path & file name:", False))
    body()
    
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
    fileToRead = open(filename, 'r')
    print fileToRead.read()
    fileToRead.close()

def write_to_file():
    fileToWrite = open(filename, 'w')
    
    # prompt for quantity of numbers
    n = int(prompts.numberQuantity_prompt("\nPlease enter n, the quantity of records to be entered. (INTEGERS ONLY)"))
    print "Please note that arrays should only contain numbers and spaces..."
    
    numbers = []
    for _ in range(0,n):
        numbers.append(prompts.number_prompt(True))
  
    with fileToWrite as f:
        f.writelines("\n".join(numbers))
    fileToWrite.close()

def modify_file():
    fileToModify = open(filename, 'r+')
    numbers = []
    for line in fileToModify:
        numbers.append(' '.join(line.split()))
    fileToModify.close()
#     print numbers
    
    print "\nFor each of the following numbers/arrays, please choose Accept, Replace, or Delete"
    
    acceptAll = False
    # for each num in file, read -> accept, replace, delete
    for i, num in enumerate(numbers):
        if not acceptAll:
            print "\nPosition:", i + 1, ";   Number:", num
            modifyAction = prompts.modify_prompt("\nPlease enter a valid action: Accept, Replace, or Delete.")
            
            if modifyAction == "accept":
                pass
            elif modifyAction == "replace":
                numbers[i] = prompts.number_prompt(False)
            elif modifyAction == "delete":
                numbers.pop(i)
            else:
                print "Error with action:", modifyAction
            
        # insert new num after, or before any other num
            countNumbersLeft = len(numbers) - (i + 1)
            if countNumbersLeft > 0:
                print "\nThere are", str(countNumbersLeft), "numbers between this number and the end of the file."
                doInsert = prompts.yes_no_prompt("Would you like to insert a number? Yes or No:")
            
                if doInsert == "yes":
                    insertWhere = prompts.insert_where_prompt(countNumbersLeft)
                    numbers.insert(int(insertWhere)+i, prompts.number_prompt(True))
                elif doInsert == "no":
                    pass
                else:
                    print "Error with entry:", doInsert
            
        # accept all numbers after
                shouldAcceptAll = prompts.yes_no_prompt("\nWould you like to Accept all remaining numbers? Yes or No:")
                if shouldAcceptAll == "yes":
                    acceptAll = True
                    continue
        
        # save or save as
    saveOrSaveAs = prompts.save_or_saveAs_prompt("\nWould you like to save the current file, or save as a new file? Save / SaveAs / No (ONE WORD):")
    if saveOrSaveAs[0]:
        fileToSave = ""
        if saveOrSaveAs[1] == "no":
            pass
        elif saveOrSaveAs[1] == "save":
            fileToSave = filename
        elif saveOrSaveAs[1] == "saveas":
            fileToSave = prompts.filename_prompt("\nPlease enter the new full file path & file name:", True)
        else:
            print "Error, incorrect save/saveas entry. Not saving file."
            
        if fileToSave != "":
            savedFile = open(fileToSave, 'w')
            savedFile.truncate()
            with savedFile as f:
                f.writelines("\n".join(numbers))
                savedFile.close()
        
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

main()
