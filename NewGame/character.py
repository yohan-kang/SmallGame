class Character():
    def __init__(self,grade:str,name:str,hp:int,mp:int,power:int,armor:int,shield:int,weapon:None,skill_name:None):
        self.grade = grade 
        self.name = name 
        self.hp = hp
        self.mp = mp
        self.power = power
        self.armor = armor
        self.shield = shield
        self.weapon = weapon
        self.skill_name = skill_name
        # self.action_point = point

    def attack(self,enemy):
        if  enemy.armor > self.power:
            enemy.armor = enemy.armor - self.power
        elif self.power > enemy.armor:
            damage = self.power - enemy.armor
            enemy.armor = 0
            enemy.hp = enemy.hp - damage 
        elif enemy.armor == 0:
            enemy.hp = enemy.hp - self.power

    def defense(self):
        self.armor = self.armor + self.shield
        pass


    def __str__(self):
	    # return "user1 님 HP:{} shield : {} point :{}".format(self.hp, self.shield, self.action_point)
        if self.hp > 1:
            return "{} 님 HP:{} MP:{}  weapon:{} power:{} armor: {}".format(self.name,self.hp,self.mp,self.weapon,self.power,self.armor)
        else:
            return "YOU DIE"



class Skill():
    
    def blow(self,enemy):
        damage = self.power*2
        print("Unique Skills {} ~~~  damage :{} ".format(self.skill_name,damage)) 

        if enemy.armor > 0:
            if damage > enemy.armor:
                damage = damage - enemy.armor
                enemy.armor = 0
                enemy.hp = enemy.hp - damage
        else:
            enemy.hp = enemy.hp - damage

    def run():
        pass


class Hunter(Character,Skill):
    pass

class Soldier(Character):
    pass

class Boss(Character,Skill):
    pass



# class BossMonster1(Character,BossMonsterAction):
#     def skill(self,user):
#         print("Boss Unique Skills  go to hell ~~~ damage 20")
#         damage = 20
#         if user.armor > 0:
#             if damage > user.armor:
#                 damage = damage - user.armor
#                 user.armor = 0
#                 user.hp = user.hp - damage
#         else:
#             user.hp = user.hp - damage

# class BossMonster2(Character,BossMonsterAction):
#     def skill(self,user):
#         print("Boss Unique Skills  Crucio ~~~ damage 40")
#         damage = 40
#         if user.armor > 0:
#             if damage > user.armor:
#                 damage = damage - user.armor
#                 user.armor = 0
#                 user.hp = user.hp - damage
#         else:
#             user.hp = user.hp - damage

# class BossMonster3(Character,BossMonsterAction):
#     def skill(self,user):
#         print("Boss Unique Skills abadaKedabra ~~~ damage 100")
#         damage = 100
#         if user.armor > 0:
#             if damage > user.armor:
#                 damage = damage - user.armor
#                 user.armor = 0
#                 user.hp = user.hp - damage
#         else:
#             user.hp = user.hp - damage




# 스텟보는 창만드나??
# 어떻게 보여질것인가
# hp 게이지는 보이게 하는거 가능할것 같은데 
# 몬스터 점점 강하게 하기 ,10stage까지만  
# 보스 만들기  즉 몬스터 ,보스 클래스 객체 만들기?? 
# 인터페이스는 어떻게 활용하나.
# 랜덤 부분 필요하나..
# 콘솔 화살표창 움직이게 하는거 구현할때가 온듯 ...#
