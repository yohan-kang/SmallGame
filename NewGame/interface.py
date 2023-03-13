from abc import ABC, abstractmethod


class Action(ABC):

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defense(self, new_content: str) -> None:
        """작성한 메시지를 수정하는 메소드"""
        # 여기에는 활동수 하나를 추가 해주는걸 넣는다 
        # 방어 성공할 경우? 
        # 아니면 보호력?? 증가로 
        pass
    
    # @abstractmethod
    # def cure(self, new_content: str) -> None:
    #     pass

    # 고유 강기술? 


    @abstractmethod
    def run(self, destination: str) -> bool:
        """작성한 메시지를 전송하는 메소드"""
        pass

class MonsterAction(ABC):
    @abstractmethod
    def attack(self):
        pass
    @abstractmethod
    def defense(self, new_content: str) -> None:
        """작성한 메시지를 수정하는 메소드"""
        pass
    @abstractmethod
    def skil(self):
        pass