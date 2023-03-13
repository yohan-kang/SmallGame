import interface
import character
import os
import random
from interface import Action

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

def choiceWeapon():
  os.system("cls")
  print("sword\n power: 5 \n skil:blow(데미지(damage)10+ 실드(Shield)+3)\n")
  print("axe\n power: 10 \n skil:Smash(데미지(damage)30)\n")
  print("axe\n power: 5 \n skil:Multi shot(데미지(damage)15+ 다중(Attack everyone))\n")
  bool = True
  while bool:
    num = input("choice weapon(1:sword 2:axe 3:bow):")
    if num.isdigit() and 0 < int(num) < 4:
      bool = False
    else :
      print("Invalid input Please write a natural number 1 or 2 or 3")
  return num 


def createCharacter():
  os.system("cls")
  bool = True
  while bool:
    str = input("이름을 작성하세요  Write the name of the character name :")
    if str.isspace():
      print("Don't leave it blank.")
    else :
      bool = False
  return str 


def stage(user):
  os.system("cls")
  stage = 1
  user = user
  i=0
  # boss = character.boss1
  while stage != 3:
    boss = character.arr[i]
    bool = fight(stage,user,boss)
    if bool:
      stage += 1
    i += 1


def fight(stage,user,enemy):
    bool = True 

    while 0 < int(enemy.hp):
      os.system("cls")
      print("-------------------------------")
      print('------------STAGE'+str(stage)+'-------------')
      print("-------------------------------")
      print(user)
      print("\n")
      print(enemy)
      print("\n")
      
      if 0 > user.hp:
        print("Game Over")
        exit()
      elif 0 > enemy.hp:
        print("Clear : next stage")
        return bool

      num = input("choice Action(1:Attack 2:Defense 3:Escape):")
      if num.isdigit():
        if int(num) == 1:
          user.attack(enemy)
        elif int(num) == 2: 
          user.defense()
        elif int(num) == 3: 
          user.run()
        else:
          print("Invalid input Please write a natural number 1 or 2 or 3")
      else :
        print("Invalid input Please write a natural number 1 or 2 or 3")


def main():
  again = True
  # while again:
  intro()
  level = choiceLevel()
  weapon = choiceWeapon()
  name = createCharacter()
  user = character.Character(name,50,15,10,weapon,10) 
  # print(user)
  stage(user)

main()