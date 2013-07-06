'''
Created on May 26, 2013

@author: rmaharaj
'''

# program1b.__init__()

import os, re
# # asdf = "Hello World!"
# #
# # something = raw_input("dude, enter something:")
# # print type(something)
# # print something
# # print os.path.
#
# line = "Cats are smarter than dogs";
#
# matchObj = re.match(r'(.*) are(\.*)', line, re.M | re.I)
#
# # if matchObj:
# #    print "matchObj.group() : ", matchObj.group()
# #    print "matchObj.group(1) : ", matchObj.group(1)
# #    print "matchObj.group(2) : ", matchObj.group(2)
# # else:
# #    print "No match!!"
# def check(test_str):
#     #pattern = r'-?[0-9]*.?[0-9]*\.*'
#     pattern = re.compile(r'-?[1-9]+\d*[.]?[0-9]*\Z')
#     if pattern.match(test_str):
#         print test_str,":  TRUE"
#     else:
#         print test_str,":  false"
# #
# #     regex = re.search(pattern, test_str)
# #     if re.search(pattern, test_str):
# #         # Character other then . a-z 0-9 was found
# #         print 'Invalid : %r' % (test_str,)
# #     else:
# #         # No character other then . a-z 0-9 was found
# #         print 'Valid   : %r' % (test_str,)
#
# check(test_str='abcde.1')
# check(test_str='abcde.1#')
# check(test_str='ABCDE.12')
# check(test_str='_-/>"!@#12345abcde<')
# check('78.99')
# check('7-8.99')
# check('-78.99')
# check('78.99.88')
# check('78.99.')
# check('78')
# check("-784320")
# check('-----7982')
# check('0823')
#
#
#
# def checkPath(p):
#     #pattern = re.compile(r'[a-zA-Z].:[/|\].^[\/:*?"<>|]*[\.].[a-zA-Z]{3}')
#     pattern = re.compile(r'\w{1}:{1}[\\|/]{1}.*[^\\/:*?"<>|]*[\.]*[.]{1}[\w]{3}')
#     if pattern.match(p):
#         print p,":  TRUE"
#     else:
#         print p,":  false"
#
# checkPath('c:/path.txt')
# checkPath('c')
# checkPath("C:/jest.doc")
# checkPath("c:\jest.doc")
# checkPath('D:\Users\maharaj\Documents\__CMU\__Year2\MSE\01_PSP\Assignments')
# checkPath('D:\Users\rmaharaj\Documents\__CMU\__Year2\MSE\01_PSP\Assignments\test.txt')
# checkPath('D:\Users\maharaj\jest.txt')
# checkPath('D:\Users\maharaj\Documents\jest.txt')
# checkPath('D:\Users\maharaj\Documents\__CMU\jest.txt')
# checkPath('D:\Users\maharaj\Documents\__CMU\__Year2\jest.txt')
# checkPath('D:\Users\maharaj\Documents\__CMU\__Year2\MSE\jest.txt')
# checkPath('D:\Users\maharaj\Documents\__CMU\__Year2\MSE\01_PSP\jest.txt')
# checkPath("SD:FLKJDF(*3rm")
# checkPath('D:\Users\rmaharaj\Documents\__CMU\__Year2\MSE\01_PSP\Assignments')


def check_array(array):
    maxArraySize = 10
#     pattern = re.compile(r'[-?[1-9]+\d*[.]?[0-9]*\s?]%d\Z'%maxArraySize)
    pattern = re.compile(r'(-?[1-9]+\d*[.]?[0-9]*){1}\Z|(-?[1-9]+\d*[.]?[0-9]*\s{1}){1,%s}(-?[1-9]+\d*[.]?[0-9]*)\Z' % (maxArraySize - 1))
#     pattern = re.compile(r'([0-9]*\s?)+\Z')
    if pattern.match(array):
        print array, ":  TRUE"
    else:
        print array, ":  FALSE"


check_array('1')
check_array('-123')
check_array('45.67')
check_array('1 ')
check_array('-123 ')
check_array('45.67 ')
print '-----------------'
check_array('1 2')
check_array('-123 45.67')
print '-----------------'
check_array('1 2 3 ')
check_array('1 2 3 4 5 6 7 8 9 10')
check_array('1 2 3 4 5 6 7 8 9 10 11')
check_array('[1]')
check_array('[1, 2]')
check_array('1  2')
