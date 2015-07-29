# Problem Set 1 : Part 2

def countBob(s):

    '''Loops through a given string and prints the number of times the substring 
    'bob' occurs'''
    
    count = 0
    for i in range(1, len(s) - 1):
        if s[i-1 : i+2] == 'bob':
            count += 1
    print 'Number of times bob occurs is:' + str(count)
countBob(s)