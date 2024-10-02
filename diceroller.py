import random

dice_count = int(input("How many dice: "))
dice_side = int(input("How many sides: "))
play=ModuleNotFoundError

while(play!="q"):
    for x in range(dice_count):
        val = random.randint(1, dice_side)
        print(val)
        play=input("enter q to stop")
        if(play.lower()=="q"):
            break
        dice_count = int(input("How many dice: "))
        dice_side = int(input("How many sides: "))
    
    
    

