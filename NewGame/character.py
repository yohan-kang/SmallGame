from interface import BasicAction,HunterAction,BossMonsterAction


class Character():
    def __init__(self,grade,name,hp,mp,power,weapon:None,shield):
        self.grade = grade 
        self.name = name 
        self.hp = hp
        self.mp = mp
        self.power = power
        self.weapon = weapon
        self.shield = shield
        # self.action_point = point

    def __str__(self):
	    # return "user1 님 HP:{} shield : {} point :{}".format(self.hp, self.shield, self.action_point)
        if self.hp > 1:
            return "{} 님 HP:{} MP:{}  weapon:{} power:{} shield: {}".format(self.name,self.hp,self.mp,self.weapon,self.power,self.shield)
        else:
            return "YOU DIE"




class Hunter(Character,HunterAction):

    def attack(self,enemy):
        if  enemy.shield > self.power:
            enemy.shield = enemy.shield - self.power
        elif self.power > enemy.shield:
            damage = self.power - enemy.shield
            enemy.shield = 0
            enemy.hp = enemy.hp - damage 
        elif enemy.shield == 0:
            enemy.hp = enemy.hp - self.power

    def defense(self):
        self.shield = self.shield + 10

    def skil():
        pass 

    def run():
        pass

class Monster(Character,BasicAction):
    def attack(self,user):
        # enemy.hp = enemy.hp - (self.weapon + self.power)
        user.hp = user.hp - self.power

    def defense(self):
        self.shield = self.shield + 10


class BossMonster1(Character,BossMonsterAction):
    def attack(self,enemy):
        if  enemy.shield > self.power:
            enemy.shield = enemy.shield - self.power
        elif self.power > enemy.shield:
            damage = self.power - enemy.shield
            enemy.shield = 0
            enemy.hp = enemy.hp - damage 
        elif enemy.shield == 0:
            enemy.hp = enemy.hp - self.power

    def defense(self):
        self.shield = self.shield + 20
    
    def skil(self,user):
        print("Boss Unique Skills  go to hell ~~~ damage 20")
        damage = 20
        if user.shield > 0:
            if damage > user.shield:
                damage = damage - user.shield
                user.shield = 0
                user.hp = user.hp - damage
        else:
            user.hp = user.hp - damage

class BossMonster2(Character,BossMonsterAction):
    def attack(self,enemy):
        enemy.hp = enemy.hp - self.power

    def defense(self):
        self.shield = self.shield + 20
    
    def skil(self,user):
        print("Boss Unique Skills  Crucio ~~~ damage 40")
        damage = 40
        if user.shield > 0:
            if damage > user.shield:
                damage = damage - user.shield
                user.shield = 0
                user.hp = user.hp - damage
        else:
            user.hp = user.hp - damage

class BossMonster3(Character,BossMonsterAction):
    def attack(self,enemy):
        enemy.hp = enemy.hp - self.power

    def defense(self):
        self.shield = self.shield + 20
    
    def skil(self,user):
        print("Boss Unique Skills abadaKedabra ~~~ damage 100")
        damage = 100
        if user.shield > 0:
            if damage > user.shield:
                damage = damage - user.shield
                user.shield = 0
                user.hp = user.hp - damage
        else:
            user.hp = user.hp - damage




# 스텟보는 창만드나??
# 어떻게 보여질것인가
# hp 게이지는 보이게 하는거 가능할것 같은데 
# 몬스터 점점 강하게 하기 ,10stage까지만  
# 보스 만들기  즉 몬스터 ,보스 클래스 객체 만들기?? 
# 인터페이스는 어떻게 활용하나.
# 랜덤 부분 필요하나..
# 콘솔 화살표창 움직이게 하는거 구현할때가 온듯 ...#
