# Problem Set 1 : Part 3

'''Given a string, this returns the longest alphabetical substring within'''

start = 1
string = ''
real_string = ''
while start <= len(s) -1:

    if len(string) < 1:
        string = s[start - 1] 

    if s[start - 1] <= s[start]:
        string += s[start]
        if len(string) > len(real_string):
            real_string = string
    else:
        string = ''

    start += 1

if real_string == '':
    real_string = s[0]

print("Longest substring in alphabetical order is: " + real_string)