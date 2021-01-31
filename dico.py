# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 14:00:50 2020

@author: Naima
"""
import difflib
from difflib import get_close_matches
import json

data=json.load(open("data.json",'r'))
D=data.keys()
 
def dico(word):
    word=word.lower() 
    if word in data:
        return(data[word])
    elif word.title() in data:
        return(data[word.title()])
    elif word.upper() in data:
        return(data[word.upper()])
    elif len(get_close_matches(word,D))>0 :
        ans=input ("did you mean %s instead? enter Y if yes or N if no:" % get_close_matches(word,D)[0])
        if ans =="Y":
           return(data[get_close_matches(word,D)[0]])
        elif ans=="N":
            return("the word doesn't exist")
        else:
            return("we didn't understand your entry")
    else:     
        return("this word doesn't exist try again")

word=input("rechercher:")
L=dico(word)
if type(L)==list:
   for i in L:
       print(i+"\n")
else:
    print(L)



