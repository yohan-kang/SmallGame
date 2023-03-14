from character import Character,Hunter,Monster,BossMonster1,BossMonster2,BossMonster3

# def goToHell(enemy,user):

#     print("보스 고유 스킬 go to hell ~~~ 데미지 20")
#     damage = 40
#     if user.shield > 0:
#         if damage > user.shield:
#             damage = damage - user.shield
#             user.shield = 0
#             user.hp = user.hp - damage
#     else:
#         user.hp = user.hp - damage

# def Crucio(enemy,user):

#     print("보스 고유 스킬 Crucio ~~~ 데미지 40")
#     damage = 40
#     if user.shield > 0:
#         if damage > user.shield:
#             damage = damage - user.shield
#             user.shield = 0
#             user.hp = user.hp - damage
#     else:
#         user.hp = user.hp - damage

# def abadaKedabra(enemy,user):

#     print("보스 고유 스킬 abadaKedabra ~~~ 데미지 100")
#     damage = 100
#     if user.shield > 0:
#         if damage > user.shield:
#             damage = damage - user.shield
#             user.shield = 0
#             user.hp = user.hp - damage
#     else:
#         user.hp = user.hp - damage



easy = []
soso = []
hard = []



boss1 = BossMonster1('boss',"King of Skeleton",60,60,20,"sword",30)
boss2 = BossMonster2('boss',"minotaur",60,60,20,"The Devil's Wand",30)
boss3 = BossMonster3('boss',"Ruined King",60,60,20,"The magic wand of death",30)


arr = [boss1,boss2,boss3]