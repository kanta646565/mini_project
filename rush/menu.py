#!/usr/bin/env python3

name = input("Your name: \n")
lastname = input("Your lastname: \n")
PLAYER={
     'name': 'name',
     'lastname' : 'lastname'
     
}

Rank = int
i = str


Rank = 0
again = int 








'''======================= menu ============================================================'''

def start():
    print("\n.\n.\n.\n.")
    
    

    print("lets start!")
        
def rules() :
    print("rule1 : You have to be 18 years old")
    print("rule2 : You need to read your chosen answer")
    print("rule3 : Rock beats Scissor")
    print("rule4 : Scissor beats Paper")
    print("rule5 : Paper beats Rock")
    print("rule5 : If you choose the same as bot, it's a draw \n")
    print("Tips : You can checked your rank in RANK at the menu")
    print("Tips : Your rank rewrite after play next game")

    
def rank():
    global Rank
    print('honor to : ',name,lastname)
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

def Your_House_At42_Bangkok() :
    global i

    print('Your_House_At42_Bangkok') 
    for i in range (1,11) :
        print(i)
    Yourhouse = input("insert your house in number \n")
    return Yourhouse 
    

'''================================================================================================'''







'''===================================== Games ====================================================='''
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
        


        
'''========================================== while ========================================='''






while True:
    print("\n=== NONtendoOO Games ===")
    print("1. START")
    print("2. rules")
    print("3. rank")
    print("4. select your house")
    print("5. Exit \n")
    print("CERT for certificate")

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
    elif choice == '4' :
        Your_House_At42_Bangkok()
        home=input("Type anything to menu : ")        
    elif choice == '5':
        break 
    elif choice == 'CERT' :
        print("Thank you for playing our game\n")
        print(f"This CERTIFICATE for {name} {lastname}")     
         

    else :
        print("error")



'''============================================= end ======================================='''