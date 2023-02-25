import os
import random

def intro() :
    print("----------------------------------------------------------------------------\n ")
    print("Hello, it's a game where you guess the number you think.  \n ")
    print("The game starts immediately.\n")
    print("When the game starts, the user enters a numeric range (1-1000)\n")
    print("If you want to select a larger range of numbers, please leave an inquiry to the developer.\n")
    print("If you want to stop the game in the middle, type exit.\n")
    print("Type 'Up' if the number displayed on the device is higher than you think. \n")
    print("Enter 'Low' if the number displayed on your device is lower than you think. \n")
    print("Enter yes if the number displayed on the device is correct.\n")
    print("If you want to stop the game in the middle, type exit.\n")
    print("----------------------------------------------------------------------------\n ")

# The part where the user initially enters the maximum value : 사용자가 처음에 최대값 입력하는 부분
def choiceMax() :
    """
    choiceMax : This function is the part where the user sets the max value at the start of the game. 
    Returns the bool value according to the value entered by the user. 
    이 기능은 사용자가 게임 시작 시 최대값을 설정하는 부분이다. 사용자가 입력한 값에 따라 부울 값을 반환합니다.
    """
    bool = False
    while bool != True:
         max_num = input("Please enter a maximum integer (starting is 1) : ")
         if max_num.isdigit() and  (0 < int(max_num) < 1001):
             return max_num
         elif max_num.upper() == "EXIT":
             return "EXIT"
         else:
             print("Invalid input Please write a natural number between 1 and 1000.")
             bool = False

def question(max_num):
    bool = False
    min_num = 1
    max_num = int(max_num)
    int_lst = []
    lst= list(range(min_num,max_num+1))
    
    while bool != True:     
         x = random.randint(min_num,max_num)
         str = input("{} Is this your number? : ".format(x))

         if str.upper() == "LOW":
             max_num = x-1
             int_lst = lst[min_num-1:max_num]
             print("list:{}".format(int_lst))
             bool = lst_check(max_num,int_lst)

         elif str.upper() == "UP":
             min_num = x+1 
             int_lst = lst[min_num-1:max_num]
             print("list:{}".format(int_lst))
             bool = lst_check(max_num,int_lst)

         elif str.upper() == "YES":
             print("S~~~~~o Easy")
             bool = True
         elif str.upper() == "EXIT":
             bool = True
         else :
             print("Invalid input Please write 'UP' or 'Low'.")
             bool = False
    return bool

def reGame() :    
    """
    reGame : This function is the part where you ask if the game continues. Returns the bool value. 이 기능은 게임이 계속 진행되는지 묻는 부분이다.  부울 값을 반환합니다.
    """
    bool = False
    while bool != True:
         x = input("Do you want to play the game again?(Enter O or X) :")
         if x.upper() == "O":
             os.system('cls')
             game()
             bool = True
         elif x.upper() == "X":
             print("Good Bye")
             bool = True
             return bool 
         else: 
             print("Invalid input Please write 'O' or 'X'.\n")

# not yet
def lst_check(num,lst):
    bool = False
    if num not in lst:
        print("거짓말 It's a number that's not in the list.")
        return True
    return bool


min_num = 1
max_num = 1

def game():
    bool = False
    while bool != True:
         intro()
         max_num = choiceMax()

         if max_num.isdigit():
             bool = question(max_num)
         bool = reGame()
         break
    

# start 
game()




# 유저가 작은 숫자 큰숫자 적게 하기 그중에 있게하기 

# def findNumber(min,max,num,bool,lst):
#     while bool != True:
#         x = input("{} Is this your number? : ".format(num))
        
#         if x.upper() == "LOW":
#             max = num-1
#             int_lst = lst[min-1:max]
#             print("list:{}".format(int_lst))
#             num = (min + max) // 2

#         elif x.upper() == "UP":
#             min = num+1 
    
#             int_lst = lst[min-1:max]
#             print("list:{}".format(int_lst))
#             num = (min + max) // 2

#         elif x.upper() == "YES":
#             print("S~~~~~o Easy")
#             bool = True
#         elif x.upper() == "EXIT":
#             bool = True
#         else :
#             print("Invalid input Please write 'UP' or 'Low'.")
#             bool = False
#             # findNumber(min,max,num,bool,lst)

            
#         if len(lst[min-1:max]) == 2:
#             bool = caseOf2(lst[min-1:max])
#             break
#         elif len(lst[min-1:max]) == 3:
#             bool = caseOf3(lst[min-1:max])
#             break


# # 어쩌면 2개남은 상황에서 왼쪽에것이 아니면 자르고 하나남은 배열에서 그 배열에 관한 함수를 만들면 통일되서 좋을것 같다 

# def caseOf1(lst) :
#     bool = False
#     while bool != True:
#         x = input("{} Is this your number? : ".format(lst))
#         if x.upper() == "LOW" or x.upper() == "UP":
#             print("거짓말쟁이 이 숫자는 마지막 숫자야 그래서 당신이 찾는 숫자는 없어")
#             return True
#         elif x.upper() == "YES":
#             print("S~~~~~o Easy")
#             return True
#         elif x.upper() == "EXIT":
#             return True
#         else :
#             print("Invalid input Please write 'UP' or 'Low'.\n")
#             bool = False
#         # caseOf1(lst)


# def caseOf2(lst) :
#     bool = False
#     while bool != True:
#         x = input("{} Is this your number? : ".format(lst[0]))

#         if x.upper() == "LOW":
#             print("거짓말쟁이 이 숫자보다 작은 숫자는 없어 ")
#             return True
#         elif x.upper() == "UP":
#             bool = caseOf1(lst[1])
#             return bool

#         elif x.upper() == "YES":
#             print("S~~~~~o Easy")
#             return True
#         elif x.upper() == "EXIT":
#             return True
#         else :
#             print("Invalid input Please write 'UP' or 'Low'.\n")
#             bool = False
#         # caseOf2(lst)

# def caseOf3(lst) :
#     bool = False
#     while bool != True:
#         x = input("{} Is this your number? : ".format(lst[1]))

#         if x.upper() == "LOW":
#             bool=caseOf1(lst[0])
#             return bool

#         elif x.upper() == "UP":
#             bool=caseOf1(lst[2])
#             return bool

#         elif x.upper() == "YES":
#             print("S~~~~~o Easy")
#             return True
#         elif x.upper() == "EXIT":
#             return True
#         else :
#             print("Invalid input Please write 'UP' or 'Low'.\n")
#             bool = False
#             # caseOf3(lst)

# def reGame() :
#     x = input("Do you want to play the game again?(Enter O or X) :")

#     if x.upper() == "O":
#         max = 100
#         min = 1
#         lst=list(range(min,max+1))
#         bool = False
#         num=((lst[0]+lst[-1]) // 2)
#         os.system('cls')
#         intro()
#         findNumber(min,max,num,bool,lst)
#         reGame()
#     elif x.upper() == "X":
#         return print("Good Bye")
#     else: 
#         print("Invalid input Please write 'O' or 'X'.\n")
#         reGame()


# max = 100
# min = 1
# lst=list(range(min,max+1))
# bool = False
# num=((lst[0]+lst[-1]) // 2)

# intro()
# findNumber(min,max,num,bool,lst)
# reGame()











