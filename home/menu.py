#!/usr/bin/env python3
name = input("Your name: \n")
Rank = int

Rank = 0
again = int 








'''======================= menu ======================='''

def start():
    print("\n.\n.\n.\n.")
    
    

    print("lets start!")
        
def rules() :
    print("rule1 -------------------------------")
    print("rule2 -------------------------------")
    print("rule3 -------------------------------")
    
def rank():
    print('hornor to : ',name)
    print("Your rank : " ,Rank)
    if Rank == 0 :
        print("no rank")
    elif Rank == 1 :
        print("rank C")
    elif Rank == 2 :
        print("rank B")
    elif Rank == 3 :
        print("rank A")
    else :
        print("some thing is error")

'''=========================================='''

'''=================== Games ======================='''
def gameA():
    global Rank
    

    ans1 = ['rock','paper','scissor']
    print('rock') 
    print('paper')
    print('scissor\n.\n.')

    ans1 = input("choose : ")
    import random
    options = ['rock','paper','scissor']
    ansAI =  random.choice(options)
    import time
    time.sleep(1)
    print("Computer chose: ", ansAI)

    if ans1=='rock' and ansAI == 'rock' :
        print('Tie')
        Rank=Rank+2 
    elif ans1=='rock' and ansAI == 'paper' :
        print('You lost')
        Rank=Rank+1
    elif ans1=='rock' and ansAI == 'scissor' :
        print('You win')
        Rank=Rank+3
    elif ans1=='paper' and ansAI == 'paper' :
        print('Tie')
        Rank=Rank+2   
    elif ans1=='paper' and ansAI == 'scissor' :
        print('You lost')
        Rank=Rank+1  
    elif ans1=='paper' and ansAI == 'rock' :
        print('You win')
        Rank=Rank+3
    elif ans1=='scissor' and ansAI == 'scissor' :
        print('Tie')  
        Rank=Rank+2
    elif ans1=='scissor' and ansAI == 'rock' :
        print('You lost')
        Rank=Rank+1  
    elif ans1=='scissor' and ansAI == 'paper' :
        print('You win')
        Rank=Rank+3
    else:
        print('error')
        return
        Rank = 0


        







while True:
    print("\n=== NONtendoOO Games ===")
    print("1. START")
    print("2. rules")
    print("3. rank")
    print("4. ")
    print("5. Exit \n")

    choice = str(input("Choice: "))

    if choice == '1' :
        start()
        Rank=0
        gameA()
        print('play again?\n ')
        print('yes for play again \n')
        
        again=input()
        while again=='yes':
                Rank = 0
                gameA()
                print('play again?\n ')
                print('yes for play again \n')
                again=input()
            
    elif choice == '2' :
        rules()
        home=input("Type anything to menu : ")
    elif choice == '3' :
        rank()
        Rank = 0
        home=input("Type anything to menu : ")        
    elif choice == '5':
        break      
    else :
        print("error")