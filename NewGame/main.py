import interface
import os
import random
from character import Character, Hunter
from monster import monster_list


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


# def choiceLevel():
#   os.system("cls")
#   bool = True
#   while bool:
#     # os.system("cls")
#     num = input("choice level(1:Easy 2:soso 3:hard):")
#     if num.isdigit() and 0 < int(num) < 4:
#       bool = False
#     else :
#       print("Invalid input Please write a natural number 1 or 2 or 3")
#   return num


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


def stage(user:Character):
  os.system("cls")
  user = user

  while monster_list:
    stage = 1
    monster = monster_list.pop(0)
    for obj in monster:
      fight(stage,user,obj)
      if user.hp < 0:
        return 2
    stage += 1
  return 1 


def fight(stage: int,user : Character,enemy : Character):
  bool = True 

  while (0 < int(user.hp)) or bool:
    os.system("cls")
    print("-------------------------------")
    print('------------STAGE'+str(stage)+'-------------')
    print("-------------------------------")
    print(user)
    print("\n")
    print(enemy)
    print("\n")

    if 0 >= user.hp:
      print("=========Game Over========")
      bool = False
    elif 0 > enemy.hp:
      print("Clear : next stage")
      bool = False
      return
    print("======= user Action =======")
    userAct(user,enemy)
    print("======= monster Action =======")
    monsterAct(user,enemy)



def userAct(user,enemy):
  bool = True
  while bool:
    num = input("choice Action(1:Attack 2:Defense 3:Escape):")
    if num.isdigit():
      if int(num) == 1:
        if enemy.shield > 0 :
          print( " {} attacks the enemy with {} power.  enemy hp :{} enemy armor :{} -> ".format(user.name,user.power,enemy.hp,enemy.armor))
          user.attack(enemy)
          print( "enemy hp: {} enemy armor: {} decrease".format(enemy.hp,enemy.armor))
          bool = False
        else : 
          print( " {} attacks the enemy with {} power.  enemy hp: {} -> ".format(user.name,user.power,enemy.hp))
          user.attack(enemy)
          print( "enemy hp: {} decrease", end=''.format(enemy.hp))
          bool = False
      elif int(num) == 2: 
        print( " {} has a defensive posture.  Shield {} -> ".format(user.name,user.shield))
        user.defense()
        print( "armor: {} Increase" .format(user.armor))
        bool = False
      elif int(num) == 3: 
        user.run()
        bool = False
      elif str(num).upper == "EXIT": 
        exit()
      else:
        print("Invalid input Please write a natural number 1 or 2 or 3")
    else :
      print("Invalid input Please write a natural number 1 or 2 or 3")


def monsterAct(user,enemy):

  act_num = randomNum(enemy)
  if act_num == 1:
    if user.shield > 0 :
      print( " {} attacks the user with {} power.  user hp :{} user armor :{} -> ".format(enemy.name,enemy.power,user.hp,user.armor))
      enemy.attack(user)
      print( "user hp: {} user armor: {} decrease".format(user.hp,user.armor))
      bool = False
    else : 
      print( " {} attacks the user with {} power.  user hp {} -> ".format(enemy.name,enemy.power,user.hp))
      enemy.attack(user)
      print( "user hp: {} decrease".format(user.hp))
      bool = False


  elif act_num == 2:
    print( " {} has a defensive posture.  Shield {} ->".format(enemy.name,enemy.shield))
    enemy.defense()
    print( "armor: {} Increase" .format(enemy.armor))

  elif act_num == 3:
    print( " Boss: {} used skill to {}".format(enemy.name,user.name))
    if user.shield > 0 :
      enemy.skil(user)
      print( "user hp: {} user Shield: {} decrease".format(user.hp,user.shield))
      bool = False
    else : 
      enemy.skil(user)
      print( "user hp: {} decrease".format(user.hp))
      bool = False


  bool = True
  while bool:
    enter = input("press enter.")
    if enter == "":
      bool = False
    else:
      print("Please press enter.")


def randomNum(enemy):

  if enemy.grade == "soldier":
    # 80% attack 20% defense
    x = random.randint(1,10)
    if x <= 8:
      return 1
    else : 
      return 2


  if enemy.grade == "boss":
    # 60% attack 30% skill 10% defense
    x = random.randint(1,10)
    if x <= 6:
      return 1
    elif 7 <= x <= 9:
      return 3
    elif x == 10:
      return 2 



def main():
  again = True
  # while again:
  intro()
  # level = choiceLevel()
  weapon = choiceWeapon()
  name = createCharacter()
  user = Hunter('hunter',name,50,20,10,15,10,weapon,'blow') 
     
  result = stage(user)
  if result == 2:
    print("Game Over")
  elif result == 1:
    print("Clear Game")
  print("Good Bye")
main()