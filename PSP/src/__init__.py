import os, re
# asdf = "Hello World!"
# 
# something = raw_input("dude, enter something:")
# print type(something)
# print something
# print os.path.

line = "Cats are smarter than dogs";

matchObj = re.match(r'(.*) are(\.*)', line, re.M | re.I)

# if matchObj:
#    print "matchObj.group() : ", matchObj.group()
#    print "matchObj.group(1) : ", matchObj.group(1)
#    print "matchObj.group(2) : ", matchObj.group(2)
# else:
#    print "No match!!"
def check(test_str):
    #pattern = r'-?[0-9]*.?[0-9]*\.*'
    pattern = re.compile(r'-?[1-9]+\d*[.]?[0-9]*\Z')
    if pattern.match(test_str):
        print test_str,":  TRUE"
    else:
        print test_str,":  FALSE"
#     
#     regex = re.search(pattern, test_str)
#     if re.search(pattern, test_str):
#         # Character other then . a-z 0-9 was found
#         print 'Invalid : %r' % (test_str,)
#     else:
#         # No character other then . a-z 0-9 was found
#         print 'Valid   : %r' % (test_str,)
     
check(test_str='abcde.1')
check(test_str='abcde.1#')
check(test_str='ABCDE.12')
check(test_str='_-/>"!@#12345abcde<')
check('78.99')
check('7-8.99')
check('-78.99')
check('78.99.88')
check('78.99.')
check('78')
check("-784320")
check('-----7982')
check('0823')