import os

def intro() :
    print("----------------------------------------------------------------------------\n ")
    print("Hello, it's a game where you guess the number you think.  \n ")
    print("The game starts immediately.\n")
    print("Type 'Up' if the number displayed on the device is higher than you think. \n")
    print("Enter 'Low' if the number displayed on your device is lower than you think. \n")
    print("Enter yes if the number displayed on the device is correct.\n")
    print("If you want to stop the game in the middle, type exit.\n")
    print("----------------------------------------------------------------------------\n ")



# 유저가 작은 숫자 큰숫자 적게 하기 그중에 있게하기 

def findNumber(min,max,num,bool,lst):
    while bool != True:
        x = input("{} Is this your number? : ".format(num))
        
        if x.upper() == "LOW":
            max = num-1
            int_lst = lst[min-1:max]
            print("list:{}".format(int_lst))
            num = (min + max) // 2

        elif x.upper() == "UP":
            min = num+1 
    
            int_lst = lst[min-1:max]
            print("list:{}".format(int_lst))
            num = (min + max) // 2

        elif x.upper() == "YES":
            print("S~~~~~o Easy")
            bool = True
        elif x.upper() == "EXIT":
            bool = True
        else :
            print("Invalid input Please write 'UP' or 'Low'.")
            bool = False
            # findNumber(min,max,num,bool,lst)

            
        if len(lst[min-1:max]) == 2:
            bool = caseOf2(lst[min-1:max])
            break
        elif len(lst[min-1:max]) == 3:
            bool = caseOf3(lst[min-1:max])
            break


# 어쩌면 2개남은 상황에서 왼쪽에것이 아니면 자르고 하나남은 배열에서 그 배열에 관한 함수를 만들면 통일되서 좋을것 같다 

def caseOf1(lst) :
    bool = False
    while bool != True:
        x = input("{} Is this your number? : ".format(lst))
        if x.upper() == "LOW" or x.upper() == "UP":
            print("거짓말쟁이 이 숫자는 마지막 숫자야 그래서 당신이 찾는 숫자는 없어")
            return True
        elif x.upper() == "YES":
            print("S~~~~~o Easy")
            return True
        elif x.upper() == "EXIT":
            return True
        else :
            print("Invalid input Please write 'UP' or 'Low'.\n")
            bool = False
        # caseOf1(lst)


def caseOf2(lst) :
    bool = False
    while bool != True:
        x = input("{} Is this your number? : ".format(lst[0]))

        if x.upper() == "LOW":
            print("거짓말쟁이 이 숫자보다 작은 숫자는 없어 ")
            return True
        elif x.upper() == "UP":
            bool = caseOf1(lst[1])
            return bool

        elif x.upper() == "YES":
            print("S~~~~~o Easy")
            return True
        elif x.upper() == "EXIT":
            return True
        else :
            print("Invalid input Please write 'UP' or 'Low'.\n")
            bool = False
        # caseOf2(lst)

def caseOf3(lst) :
    bool = False
    while bool != True:
        x = input("{} Is this your number? : ".format(lst[1]))

        if x.upper() == "LOW":
            bool=caseOf1(lst[0])
            return bool

        elif x.upper() == "UP":
            bool=caseOf1(lst[2])
            return bool

        elif x.upper() == "YES":
            print("S~~~~~o Easy")
            return True
        elif x.upper() == "EXIT":
            return True
        else :
            print("Invalid input Please write 'UP' or 'Low'.\n")
            bool = False
            # caseOf3(lst)

    

def reGame() :
    x = input("Do you want to play the game again?(Enter O or X) :")

    if x.upper() == "O":
        max = 50
        min = 1
        lst=list(range(min,max+1))
        bool = False
        num=((lst[0]+lst[-1]) // 2)
        os.system('cls')
        intro()
        findNumber(min,max,num,bool,lst)
        reGame()
    elif x.upper() == "X":
        return print("Good Bye")
    else: 
        print("Invalid input Please write 'O' or 'X'.\n")
        reGame()


max = 100
min = 1
lst=list(range(min,max+1))
bool = False
num=((lst[0]+lst[-1]) // 2)

intro()
findNumber(min,max,num,bool,lst)
reGame()





