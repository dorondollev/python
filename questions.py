#!/usr/bin/python3

def verbing(word):
    my_str = word
    if len(my_str) < 3:
        return my_str
    elif my_str[-3:] == 'ing':
        my_str += 'ly'
    else:
        my_str += 'ing'
    return my_str
    
def words_concatenation(words):
    my_lst = ' '.join(words)
    return my_lst
    
def reverse_words_concatenation(words):
    strings = words
    strings.reverse()
    my_lst = words_concatenation(strings)
    return my_lst
    
def is_uniq_string(some_str):
    my_str = some_str
    if len(my_str) < 2:
        return True
    if len(set(my_str)) != len(my_str):
            return False
    else:
        return True
        
def prime_number(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
    return True
    
def palindrome_num(num):
    my_num = str(num)
    my_rnum = my_num[::-1]
    if my_num == my_rnum:
        return True
    else:
        return False
