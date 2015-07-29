# Problem Set 1 : Part 1

def countVowels(s):

    '''Loops through a given string and counts the number of vowels in it'''
    
    count = 0
    for letter in s:
        if letter in 'aeiou':
            count += 1
    print 'Number of vowels: ' + str(count)

countVowels(s)