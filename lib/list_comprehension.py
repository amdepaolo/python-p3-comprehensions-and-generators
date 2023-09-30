#!/usr/bin/env python3

def return_evens(num_list):
    evens_list = [num for num in num_list if num%2 == 0]
    print (evens_list)
    return evens_list

def make_exclamation(sentence_list):
    loud_list = [sentence + "!" for sentence in sentence_list]
    return loud_list