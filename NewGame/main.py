import interface
import os
import random
from character import Character, Hunter
from monster import arr


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
  i = 0
  # boss = character.boss1
  while stage != 3:
    boss = arr[i]
    bool = fight(stage,user,boss)
    if bool:
      stage += 1
    i += 1
# 여기에 스테이지 별로 난이도 설정을 할려고 한다 



def fight(stage,user,enemy):
  # 여기에 전투 유저의 행동과 적의 랜던 행동을 반복해서 전투를 하려고 만들생각이다.  
  # 1 사용자의 액션
  # 2 적군의 액션 
  # 스테이지 이동 OR 끝 

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
    
    if 0 >= user.hp:

      print("=========Game Over========")
      exit()
    elif 0 > enemy.hp:
      print("Clear : next stage")
      return bool
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
          print( " {} attacks the enemy with {} power.  enemy hp :{} enemy Shield :{} -> ".format(user.name,user.power,enemy.hp,enemy.shield))
          user.attack(enemy)
          print( "enemy hp: {} enemy Shield: {} decrease".format(enemy.hp,enemy.shield))
          bool = False
        else : 
          print( " {} attacks the enemy with {} power.  enemy hp: {} -> ".format(user.name,user.power,enemy.hp))
          user.attack(enemy)
          print( "enemy hp: {} decrease", end=''.format(enemy.hp))
          bool = False
      elif int(num) == 2: 
        print( " {} has a defensive posture.  Shield {} -> ".format(user.name,user.shield))
        user.defense()
        print( "Shield: {} Increase" .format(user.shield))
        bool = False
      elif int(num) == 3: 
        user.run()
        bool = False
      else:
        print("Invalid input Please write a natural number 1 or 2 or 3")
    else :
      print("Invalid input Please write a natural number 1 or 2 or 3")


def monsterAct(user,enemy):

  act_num = randomNum(enemy)
  if act_num == 1:
    if user.shield > 0 :
      print( " {} attacks the user with {} power.  user hp :{} user Shield :{} -> ".format(enemy.name,enemy.power,user.hp,user.shield))
      enemy.attack(user)
      print( "user hp: {} user Shield: {} decrease".format(user.hp,user.shield))
      bool = False
    else : 
      print( " {} attacks the user with {} power.  user hp {} -> ".format(enemy.name,enemy.power,user.hp))
      enemy.attack(user)
      print( "user hp: {} decrease".format(user.hp))
      bool = False


  elif act_num == 2:
    print( " {} has a defensive posture.  Shield {} ->".format(enemy.name,enemy.shield))
    enemy.defense()
    print( "Shield: {} Increase" .format(enemy.shield))

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
    # 90% attack 20% defense
    x = random.randint(1,10)
    if x % 2 == 0 or x % 3 == 0 or x == 1 :
      return 1
    else : 
      # case 5,7 == 210 %
      return 2


  if enemy.grade == "boss":
    # 60% attack 30% skill 10% defense
    x = random.randint(1,10)
    if x % 2 == 0 or x == 1:
      return 1
    elif x == 3 or x == 5 or x == 7:
      return 3
    elif x == 9:
      return 2 



def main():
  again = True
  # while again:
  intro()
  level = choiceLevel()
  weapon = choiceWeapon()
  name = createCharacter()
  user = Hunter('warrior',name,50,15,10,weapon,10) 
  # print(user)
  stage(user)

main()