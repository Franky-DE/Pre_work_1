#A. donuts

#Given an int count of a number of donuts, return a string of the form 'Number of donuts: ', where  is the number passed in. However, if the count is 10 or more, then use the word 'many' instead of the actual count.
#So donuts(5) returns 'Number of donuts: 5' and donuts(23) returns 'Number of donuts: many'

def donuts(count):
    out_string = ''
    if count >= 10:
        out_string = 'Number of donuts: many'
    else:
        out_string = 'Number of donuts: ' + str(count)
    return out_string

#B. both_ends

#Given a string s, return a string made of the first 2 and the last 2 chars of the original string, so 'spring' yields 'spng'. However, if the string length is less than 2, return instead the empty string.

def both_ends(s):
    if len(s)<2:
        out_string = ''
    else:
        out_string = s[0:2] + s[-2:len(s)]
    return out_string


#C. fix_start

#Given a string s, return a string where all occurences of its first char have been changed to '*', except do not change the first char itself.
#e.g. 'babble' yields 'ba**le'
#Assume that the string is length 1 or more. Hint: s.replace(stra, strb) returns a version of string s where all instances of stra have been replaced by strb.

def fix_start(s):
    if len(s)<1:
        out_string = 'input-string must have a length 1 or more'
    else:
        out_string = s[0] + s[1:len(s)].replace(s[0],'*')
    return out_string


#D. MixUp

#Given strings a and b, return a single string with a and b separated by a space '<a> <b>', except swap the first 2 chars of each string.
#e.g.
#'mix', pod' -> 'pox mid'
#'dog', 'dinner' -> 'dig donner'
#Assume a and b are length 2 or more.

def mix_up(a, b):
    out_string=''
    if len(a)<2 or len(b)<2:
        out_string = 'input-strings must have a length 2 or more'
    else:
        out_string = b[0:2] + a[2:len(a)] + ' ' + a[0:2] + b[2:len(b)]   
    
    return out_string


def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

    
def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


main()

#D. verbing

#Given a string, if its length is at least 3, add 'ing' to its end. Unless it already ends in 'ing', in which case add 'ly' instead. If the string length is less than 3, leave it unchanged. Return the resulting string.

def verbing(s):
    out_string = ''
    if len(s) < 3:
        out_string=s
    elif s[-3:len(s)]=='ing':
        out_string = s + 'ly'
    else:
        out_string = s + 'ing'
    return out_string

#E. not_bad

#Given a string, find the first appearance of the substring 'not' and 'bad'. If the 'bad' follows the 'not', replace the whole 'not'...'bad' substring with 'good'.
#Return the resulting string.
#So 'This dinner is not that bad!' yields: This dinner is good!

def not_bad(s):
    out_string = ''
    if not(s.find('not') == -1):
        if not(s[s.find('not'):len(s)].find('bad') == -1):
            out_string = s[0:s.find('not')] + 'good' + s[s.find('bad')+3:len(s)]
        else:
            out_string = s
            #out_string = 'substring \'bad\' not following \'not\''
    else:
        out_string = s
        #out_string = 'substring \'not\' not found'
    return out_string

#F. front_back

#Consider dividing a string into two halves. If the length is even, the front and back halves are the same length. If the length is odd, we'll say that the extra char goes in the front half.
#e.g. 'abcde', the front half is 'abc', the back half 'de'.
#Given 2 strings, a and b, return a string of the form a-front + b-front + a-back + b-back

def front_back(a, b):
    a_back = a[-int(len(a)/2):len(a)]
    a_front = a[0:len(a)-len(a_back)]
    b_back = b[-int(len(b)/2):len(b)]
    b_front = b[0:len(b)-len(b_back)]
    out_string = a_front + b_front + a_back + b_back
     
    return out_string

def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


main()
