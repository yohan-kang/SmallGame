import os
import random

def intro():
  os.system("cls")
  print("----------------------------------------------------------------------------\n ")
  print("Hello, it's a game where you guess the number you think.  \n ")
  print("The game starts immediately.\n")
  print("When the game starts, the user enters a numeric range (1 ~ positive integer)\n")
  print("If you want to select a larger range of numbers, please leave an inquiry to the developer.\n")
  print("If you want to stop the game in the middle, type exit.\n")
  print("Type 'Up' if the number displayed on the device is higher than you think. \n")
  print("Enter 'Low' if the number displayed on your device is lower than you think. \n")
  print("Enter yes if the number displayed on the device is correct.\n")
  print("If you want to stop the game in the middle, type exit.\n")
  print("----------------------------------------------------------------------------\n ")

def choiceMax():
    """
    choiceMax : This function is the part where the user sets the max value at the start of the game. 
    Returns the bool value according to the value entered by the user. 
    이 기능은 사용자가 게임 시작 시 최대값을 설정하는 부분이다. 사용자가 입력한 값에 따라 부울 값을 반환합니다.
    """
    bool = True
    while bool:
        max_num = input("Please enter a maximum integer (starting is 1) : ")
        if max_num.isdigit() and 0 < int(max_num):
            bool = False
            return max_num
        elif max_num.upper() == "EXIT":
            bool = False
            return "EXIT"
        else :
            print("Invalid input Please write a natural number between 1 and positive integer.")

             
def question(num_limit):
    bool = True     
    min_num = 1 
    max_num = int(num_limit)
    while bool:     
        x = random.randint(min_num,max_num)
        str = input("{} Is this your number? : ".format(x))
        str = str.upper()
        if str == "LOW":
            max_num = x - 1
            bool = lst_check(x,min_num,max_num)
        elif str == "UP":
            min_num = x + 1 
            bool = lst_check(x,min_num,max_num)
        elif str == "YES":
            print("S~~~~~o Easy")
            bool = False
        elif str == "EXIT":
            bool = False
        else :
            print("Invalid input Please write 'UP' or 'Low'.")
    return bool

def lst_check(num,min_num,max_num):
    bool = True
    print("num :{},min_num:{},max_num:{}".format(num,min_num,max_num))
    if min_num > max_num:
        print("거짓말 It's a number that's not in the list.")
        return False
    return bool

def restart():
#   os.system("cls")
  val = None
  bool = True
  while bool != False:
    # os.system("cls")
    val = input("Do you want to restart ? [Y]es, [N]o : ").upper()
    if val == "Y":
       return bool
    elif val == "N":
       print("Good Bye.\n")
       exit()
    else:
       print("Invalid input Please write 'O' or 'X'.\n")


def main():
  again = True
  while again:
    intro()
    val = choiceMax()
    if val.isdigit() :
        question(val)
    again = restart()

main()