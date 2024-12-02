import random
import os
import time as t
clear = lambda: os.system('cls')
time = lambda: t.sleep(2)
close = lambda:os.system('exit()')
   
def work(n):
    if n == 1:
        n = "Zaid"
    elif n == 2:
        n = "Sevitha"
    else:
        n = "Mevan"
    print()
    print(n,"is your slave now")
    print("1.Cotton Picking\n2.Chimmney Cleaning\n3.Coal Minning")
    xn = int(input("Choose his job: "))
    print()
    if xn == 1:
        print("1. Cotton Picking")
    elif xn == 2:
        print("2. Chimmney Cleaner") 
    elif xn == 3:
        print("3. Coal miner") 
        raise Exception("U r a dum nigger idiot dude")
def buying_the_Slave(cash):
    print("Ah- Nice so you are buying this slave. Ok!")
    
    
def slave():
        print('/n')            
        print("1.Zaid\n2.Sevitha\n3.Mevan")
        y = int(input("Choose your slave: "))
        if y == 1:
            
            work(y)
            print()
        elif y == 2:
            work(y) 
            print()
        elif y == 3:
            work(y)
            print()
        else:
            raise Exception("Idiot nigger")
    
def work_Cash_cash(cash):
    print()
    print()
    print("<-----------------------------------------------------WORK----------------------------------------------------->")
    print("You enter a number, Computer will select a random number. You are supposed to multiply your number with the number the computer has selected. If the answer you type is correct you get +5000 cash!\n")
    print("Be Careful though, because if your answer is wrong it is -5000 cash")
    num_Selected_By_user = int(input("Enter the number you select to type here: "))
    Continue = True
    while Continue == True:
            num_Selected_By_computer = random.randint(1,101)
            print(num_Selected_By_computer," :-> This is the number selected by the Computer")
            total_of_Numbers = num_Selected_By_user*num_Selected_By_computer
            answer_from_the_user_of_the_calculation = int(input("Enter your answer here: "))
            if total_of_Numbers == answer_from_the_user_of_the_calculation:
                print("Correct answer My freind. You get +5000 cash!!")
                cash = cash+5000
                global again
                again = input("Do you want to play again for more cash?:")
                if again =="Yes" or again =="YES" or again =="yes" or again =="y" or again =="Y":
                    print
                    time()
                    clear()
                    work_Cash_cash(cash)
                elif again =="No" or again =="no" or again =="NO" or again =="N" or again =="n":
                    print
                    time()
                    clear()
                    Continue=False
                    work_Cash(cash)
                else:
                    raise ValueError("Wrong input")
            else:
                print("Failure bruv, Failure. -5000 cash")
                cash = cash-5000
                if again =="Yes" or again =="YES" or again =="yes" or again =="y" or again =="Y":
                    print
                    time()
                    clear()
                    work_Cash_cash(cash)
                elif again =="No" or again =="no" or again =="NO" or again =="N" or again =="n":
                    print
                    time()
                    clear()
                    Continue=False
                    work_Cash(cash)
                else:
                    raise ValueError("Wrong input")
            
def main_menu():
    print()
    print("                          Welcome to the Main Menu!/n")
    _close_ = int(input("Do you want to close the application?: "))
    if _close_ == 1:
        clear()
        close()

    
def work_Cash(cash):
    print("You can do 5 things to get more and more cash!")
    print("Which one would you like to do?: ")
    print("?? ")
    print("1) Work\n2) Sell your slaves\n3) Work as a slave\n4)Do that*Sus Emoji\n5)Check current cash?*")
    choice = int(input("Enter you choice: "))
    if choice == 1:
        print("Work Selected")
        work_Cash_cash(cash)    
    elif choice ==2:
        pass
    elif choice==3:
        pass
    elif choice ==4:
        pass
    elif choice ==5:
        print('Ah so you wanna know your current cash? Kk nws')
        print(cash)
        if cash <= 25000:
            print("Not enough CASH.. Work and get sum CASH")
            work_Cash(cash)
        elif cash >= 40000 and cash <=50000:
            print("You can only buy 1 slave")
            print()
            print("Work more a bit to buy more slaves")
            want_to_buy_slaves= input("Do you want to buy slaves now?: ")
            if want_to_buy_slaves == "Y"or want_to_buy_slaves =="y" or want_to_buy_slaves =="yes" or want_to_buy_slaves =="Yes":
                print
                print("Ok then you can buy just 1 slave!")
                time()
                clear()
                slave()
            else:
                raise Exception(22)
                
        else:
            print("You have enough cash to buy many slaves!")
            print("Cash enough so can buy but you can still get more cash buy doing more work")
                 
    else:
        raise ValueError("Wrong Value inputted")
        

# ans= ["yes", "Yes", "YES", "ya", "Ya", "YA", "yea", "Yea", "YEA","Y","y","yup","Yup","YUP","Yos","yos","YOS"]
 
# x4= input("Do you want to buy slaves?: ")
# for x in ans:
#     for x4 in x:
print("How much CASH you have? *SUS EMOJI*: ")
cash = int(input())
if cash <= 25000:
    print("Not enough CASH.. Work and get sum CASH")
    time()
    clear()
    work_Cash(cash)
elif cash >= 40000 or cash <=50000:
    print("You can only buy 1 slave")
    print
    print("Work more a bit to buy more slaves")
    time()
    clear()
    anssss = (input("Enter Y/N if you want to buy slaves?: "))
    if anssss == "Y" or anssss=="y":
        print
        print("OK! Then let's get you one slave.")
        buying_the_Slave(cash)
    elif anssss == 'N' or anssss == 'n':
        print
        print("Ok! I will guide you to the main menu where you can check wether to buy a slave or work in \n order to get more money.")
        main_menu()
        
else:
    print("You have enough cash to buy many slaves!")
    print("Cash enough so can buy but you can still get more cash buy doing more work")    