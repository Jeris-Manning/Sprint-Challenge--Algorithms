'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

#set 'th' counter

th_count = 0


def count_th(word):
    #reset count after each run
    global th_count
    th_count = 0
    #get length of word
    word_l = len(word)
    #calls recursive helper function passing in length of the word, and the word itself
    return recurthion(word_l, word)

def recurthion(n, w):
    #Takes in parameters n, as word length, and w, as word to be searched for "th"
    global th_count
    #set base case
    if n <=0:
        return th_count
    #If current slice is equal to 'th', add one to counter
    if w[n-1:n+1] == 'th':
        th_count += 1
    #Function starts with slice of final 2 characters in word, and moves backward one position with each call
    return recurthion(n - 1, w)




print(count_th(""))



