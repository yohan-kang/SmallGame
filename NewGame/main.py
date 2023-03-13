import interface
import character
import os


def intro():
  os.system("cls")
  bool = True
  while bool:
    # os.system("cls")
    num = input("Game start? (press 1 : Start  press 2 : End) :")
    if num == '1':
      bool = False
    elif num == '2':
      bool = False
      print("~Good bye~")
      exit()
    else :
      print("Invalid input Please write a natural number 1 or 2.")


def choiceLevel():
  os.system("cls")
  bool = True
  while bool:
    # os.system("cls")
    num = input("choice level(1:Easy 2:soso 3:hard):")
    if num.isdigit() and 0 < int(num) < 4:
      bool = False
    else :
      print("Invalid input Please write a natural number 1 or 2 or 3")
  return num




def main():
  again = True
  while again:
    intro()
    choiceLevel()



main()