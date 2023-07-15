#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    countDown =10
    while countDown >0:
        print(countDown)
        countDown-=1
    print("Happy New Year!")
    

def square_integers(int_list):
    # code goes here!
    int_list =[i * i for i in int_list]
    return int_list
    

def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            
        elif i % 3 == 0:
            print("Fizz")
            
        elif i % 5 == 0:
            print("Buzz")
            
        else:
            print(i) 
    
