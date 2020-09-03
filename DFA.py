#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:59:43 2020

@author: aurelio
"""


from pythomata import SimpleDFA
alphabet = {"0", "1"}
states = {"q0", "q1"}
initial_state = "q0"
accepting_states = {"q1"}
transition_function = {
    "q0": {
        "0" : "q1",
        "1" : "q0"
    },
    "q1": {
        "0" : "q0",
        "1" : "q1"
    }
}

dfa = SimpleDFA(states, alphabet, initial_state, accepting_states, transition_function)

def testString():
    string = input("Enter a string to test \n")
    print(dfa.accepts(string))
    
def printDFA():
    graph = dfa.to_graphviz()
    graph.render("/Users/aurelio/Desktop/Project/my_render.png")
    
def menu():
    options = ('Enter 1 to test strings\n'
               'Enter 2 to print the DFA\n'
               'Enter 3 to exit\n')
    choice = input(options)
    return int(choice)

print("Main Menu")

while True:
    choice = menu()
    if choice == 1:
        testString()
    elif choice == 2:
        printDFA()
    elif choice == 3:
        break
        
        
        
        
        
        
        
        