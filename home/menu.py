#!/usr/bin/env python3

name = input("Your name: \n")
rank = 0

print("\n=== name ===")
print("1. START")
print("2. rules")
print("3. rank")
print("4. ")
print("5. Exit \n")
    







def start():
    print("\n.\n.\n.\n.")
    
    

    print("lets start!")
        
def rules() :
    print("rule1 -------------------------------")
    print("rule2 -------------------------------")
    print("rule3 -------------------------------")
    
def rank():
    print(f"Your rank : {rank}")
    if rank == 0 :
        print("no rank")
    elif rank == 1 :
        print("rank C")
    elif rank == 2 :
        print("rank B")
    elif rank == 3 :
        print("rank A")
    else :
        print("some thing is error")












while True:
    print("\n=== name ===")
    print("1. START")
    print("2. rules")
    print("3. rank")
    print("4. ")
    print("5. Exit \n")

    choice = int(input("Choice: "))

    if choice == 1 :
        start()
        home=input("Type anything to menu : ")
            
    elif choice == 2 :
        rules()
        home=input("Type anything to menu : ")
    elif choice == 3 :
        rank()
        home=input("Type anything to menu : ")        
    elif choice == 5 :
        break          
    else :
        print("error")