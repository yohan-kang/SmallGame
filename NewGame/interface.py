from abc import ABC, abstractmethod

class BasicAction:
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defense(self):
        pass

class HunterAction(ABC,BasicAction):

    # # 고유 강기술? 
    @abstractmethod
    def skil(self):
        """작성한 메시지를 전송하는 메소드"""

        # if 문을사용하여 각 무기만의 스킬 구현
        pass

    @abstractmethod
    def run(self):
        """작성한 메시지를 전송하는 메소드"""
        pass


# 몬스터 액션 클래스가 따로 필요할까??  

# class MonsterAction(ABC,Basic):
#     @abstractmethod
#     def attack(self):
#         pass
#     @abstractmethod
#     def defense(self):
#         """작성한 메시지를 수정하는 메소드"""
#         pass


class BossMonsterAction(ABC,BasicAction):
    @abstractmethod
    def skil(self):
        pass