from character import Soldier,Boss


# stage1 = ['Slime','Wolf','skeletal soldier']
# stage2 = ['Mutant','warrior','Assassin']
# stage3 = ['Grim Reaper','Ruined King','headless horseman']

soldier_list = []
boss_list = [] 

slime = Soldier('soldier','Slime',15,20,3,0,5,"","")
wolf = Soldier('soldier','wolf',20,20,5,10,5,"","")
skeletal_soldier = Soldier('soldier','skeletal_soldier',20,20,6,15,5,"","")
mutant = Soldier('soldier','mutant',30,20,8,10,5,"","")
warrior = Soldier('soldier','warrior',40,20,10,20,5,"","")
assassin = Soldier('soldier','assassin',25,20,15,10,5,"","")
grim_reaper = Soldier('soldier','grim_reaper',40,20,20,20,10,"","")
ruined_king = Soldier('soldier','ruined_king',50,20,25,20,10,"","")
headless_horseman = Soldier('soldier','headless_horseman',50,20,30,30,10,"","")

stage1_boss = Boss('boss',"King of Skeleton",50,50,10,30,20,'sword',"Go to hell" )
stage2_boss = Boss('boss',"Minotaur",80,60,20,40,30,"axe","Smash")
stage3_boss = Boss('boss',"Hades",100,60,20,40,20,"The magic wand of death","abadaKedabra")

stage1 = [slime,wolf,skeletal_soldier,stage1_boss]
stage2 = [mutant,warrior,assassin,stage2_boss]
stage3 = [grim_reaper,ruined_king,headless_horseman,stage3_boss]

monster_list = [stage1,stage2,stage3]
# soldier_list = [slime,wolf,skeletal_soldier,mutant,warrior,assassin,grim_reaper,ruined_king,headless_horseman]
# boss_list = [stage1_boss,stage2_boss,stage3_boss]