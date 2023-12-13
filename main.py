import random

class Game():
    def __init__(self):
        game_board = []

        for pole in range(0,100):
            pole += 1
            game_board.append(pole)

    def move(self):
        dice_roll = random.randint(1,6)

        while dice_roll%6 == 0:
            dice_roll += random.randint(1,6)
            
        self.position += dice_roll

        return position
    
class Player(Game):
    def __init__(self, position = 1):
    


#class Snake(Game):
