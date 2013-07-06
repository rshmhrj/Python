'''
Created on Jun 1, 2013

@author: rmaharaj
@summary: This program will count the lines of code in the given program.
'''
# Imports
import os

# Global Variables
programName = ""

# Helper Functions
def get_programName():
    return programName

def set_programName(name):
    global programName
    programName = name

def check_filename(name):
    if os.path.exists(name):
        #the file is there
        return True
    elif os.access(os.path.dirname(name), os.W_OK):
        #the file does not exists but write privileges are given
        return True
    else:
        #can not write there
        print "There is an error in the filename."
        return False

# Main Functions
def main():
    print "Welcome!  This program will count the lines of code in a file."
    
    # prompt for entry of file name
    path = raw_input("Please enter the file name:")
    
    if check_filename(path):
        set_programName(path)
        body()
    else:
        print "Please re-run the program and enter a valid filename."
        
def body():    
    # open file, read file, close file
    f = open(programName, 'r+')
    lines = f.readlines()
    f.close()
    
    print count_loc(lines)
    

def count_loc(lines):
    nb_lines  = 0
    docstring = False
    for line in lines:
        line = line.strip()

        if line == "" \
           or line.startswith("#") \
           or docstring and not (line.startswith('"""') or line.startswith("'''"))\
           or (line.startswith("'''") and line.endswith("'''") and len(line) >3)  \
           or (line.startswith('"""') and line.endswith('"""') and len(line) >3) :
            continue

        # this is either a starting or ending docstring
        elif line.startswith('"""') or line.startswith("'''"):
            docstring = not docstring
            continue

        else:
            nb_lines += 1

    return nb_lines


# Start of Program
main()