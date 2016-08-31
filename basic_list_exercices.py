#LIST MANIPULATION IN PYTHON

# A. match_ends
# Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.
# Note: python does not have a ++ operator, but +=  works.

def match_ends(words):
    
    i=0
    count_match_ends = 0
    while i < len(words):
        if len(words[i])>=2 and words[i][0] == words[i][-1]:
            count_match_ends += 1
        i += 1
    return count_match_ends

#test = ['a','b','ab','aba','bba','bab','ba', 'aaaaaa']
#match_ends(test)

#B. front_x

#Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first.
#e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
#Hint: this can be done by making 2 lists and sorting each of them before combining them.

def front_x(words):
    i=0
    words_just_x = []
    words_without_x = []
    words_sort_x_first = []
    while i < len(words):
        if words[i][0]=='x':
            words_just_x.append(words[i])
        else:
            words_without_x.append(words[i])
        i += 1
    words_sort_x_first = sorted(words_just_x)
    words_sort_x_first.extend(sorted(words_without_x))
    return words_sort_x_first

#test = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
#front_x(test)

#C. sort_last

#Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple.
#e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
#Hint: use a custom key= function to extract the last element form each tuple.

def sort_last(tuples):
    list_tmp=[tuples[0]]
    i=1
    while i < len(tuples):
        j=0
        while j < i:
            if tuples[i][-1] < list_tmp[j][-1]:
                list_tmp.insert(j,tuples[i])
                j = i
            else:
                j += 1
        i += 1
    return list_tmp

#test = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
#sort_last(test)

def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
    
    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
main()

print

#D. remove_adjacent

#Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.

def remove_adjacent(nums):
    i=0
    nums_new = nums
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums_new.remove(nums[i])
        else:
            i += 1
    return nums_new

#E. linear_merge

#Given two lists sorted in increasing order, create and return a merged list of all the elements in sorted order. You may modify the passed in lists. Ideally, the solution should work in "linear" time, making a single pass of both lists.

def linear_merge(list1, list2):
    list_merge = list1 + list2
    list_merge = sorted(list_merge)
    
    return list_merge

def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])

main()