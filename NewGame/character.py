import interface

print("hi")
# 여기에 캐릭터 무기를 넣는다 



class Hunter():
    def __init__(self,hp,mp,power,weapon,shield):
        self.hp = hp
        self.mp = mp
        self.power = power
        self.weapon = weapon
        self.shield = shield
        # self.action_point = point


    def __str__(self):
	    # return "user1 님 HP:{} shield : {} point :{}".format(self.hp, self.shield, self.action_point)
        return "user1 님 HP:{} weapon:{} power:{} shield : {}".format(self.hp,self.mp,self.weapon,self.power,self.shield)






# 스텟보는 창만드나??
# 어떻게 보여질것인가
# hp 게이지는 보이게 하는거 가능할것 같은데 
# 몬스터 점점 강하게 하기 ,10stage까지만  
# 보스 만들기  즉 몬스터 ,보스 클래스 객체 만들기?? 
# 인터페이스는 어떻게 활용하나.
# 랜덤 부분 필요하나..
# 콘솔 화살표창 움직이게 하는거 구현할때가 온듯 ...#
