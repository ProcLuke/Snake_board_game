import random
import os

#id 1 - empty
#id 2 - snake
#id 3 - ladder
#id 4-9 - player

class Game:
    max_players = 6
    player_count = 0
    player_dict = {}
    players = []
    Win = False
    board = {}

    for square_num in range(1, 101):
        board[square_num] = {"board_square": square_num, "id": 1, "skip": "Empty"}

    def __init__(self):
        self.square = 1
        self.name = None
        self.id = None

    def get_snakes_and_ladders(type: str, count: int):
        min_ = 1
        id_ = 2
        if type == "L":
            min_ = -1
            id_ = 3
        
        plus = 1
        while plus != count+1:
            m_start = random.randint(2,99)
            m_end = random.randint(2,99)

            if Game.board[m_start]['id'] == 1 and Game.board[m_end]['id'] == 1:
                if m_start != m_end and 0 < ((min_*m_start) - (min_*m_end)) < 40:
                    Game.board[m_start]["skip"] = type+"b-"+str(plus)
                    Game.board[m_start]["id"] = id_
                    Game.board[m_start]["board_square"] = type+"b-"+str(plus)
                    Game.board[m_end]["skip"] = type+"e-"+str(plus)
                    Game.board[m_end]["id"] = id_ 
                    Game.board[m_end]["board_square"] = type+"e-"+str(plus)
                    plus += 1
        

    def move(self):
        print(f"Hraje hráč {Game.player_dict[self.id]['name']}")
        self.square = Game.player_dict[self.id]["square"]
        if Game.board[self.square]["skip"] == "Empty":
            Game.board[self.square]["board_square"] = self.square
        else:
            Game.board[self.square]["board_square"] = Game.board[self.square]["skip"]
        Game.board[self.square]["id"] = 1
        if self.square != 1:
            self.rules()
        dice_roll = random.randint(1,6)
        while (dice_roll % 6) == 0: 
            dice_roll += random.randint(1,6)
        self.square += dice_roll
        self.rules()
        print(f"Posunul jsi se o {self.square - Game.player_dict[self.id]['square']} na pole {self.square}")
        Game.player_dict[self.id]["square"] = self.square
        Game.board[self.square]["board_square"] = self.name
        Game.board[self.square]["id"] = self.id
        Game.print_Board(self)
    
    def rules(self):
        if self.square == 100:
            print("Vyhrál jsi!!")
            Game.Win = True
        elif self.square > 100:
            self.square =  Game.player_dict[self.id]["square"]
        elif self.square < 1:
            self.square = 1
        elif Game.board[self.square]["skip"][1] == "b":
            snake = Game.board[self.square]["skip"]
            for square_num in range(1,101):
                if Game.board[square_num]["skip"] == snake[0]+"e"+snake[2:]:
                    self.square = square_num
                    print(f"Šlápl jsi na hada na poli {square_num} a sklouznul jsi dolů.")
        elif Game.board[self.square]["skip"][1] == "b":
            ladder = Game.board[self.square]["skip"]
            for square_num in range(1,101):
                if Game.board[square_num]["skip"] == ladder[0]+"e"+ladder[2:]:
                    self.square = square_num
                    print(f"Vylezl jsi po žebříku na poli {square_num} nahooru.")
        elif 4 <= Game.board[self.square]["id"] <= 9:
            print(f"Zakopnul jsi o hráče {Game.player_dict[Game.board[self.square]['id']]['name']} a shodil ho o 1 pole.")
            Game.player_dict[Game.board[self.square]["id"]]["square"] = Game.player_dict[Game.board[self.square]["id"]]["square"] - 1  

    def print_Board(self):
        print((10*8+1)*"-")
        for square_num in range(1, 101):
            if square_num % 10 == 1:
                print("|", end="")
            print(f"{str(Game.board[square_num]['board_square']).center(7)}|", end="")
            if square_num % 10 == 0:
                print()
                print((10*8+1)*"-")

    def get_players():
        playing_players = 0
        while True:
            playing_players = input("Kolik hráčů bude hrát: ")
            if playing_players.isdigit():
                playing_players = int(playing_players)
                if 0 < playing_players <= Game.max_players:
                    for player in range(1, playing_players+1):  
                        name = input(f"Zadejte jméno {player} hráče: ")
                        player = Player(name)
                        Game.players.append(player)
                    break
                else:
                    print("Pčte hráčů musí být od 1 - 6")
            else:
                print("Prosím zadejte číslo")

    def play():
        Game.get_snakes_and_ladders("S", 9)
        Game.get_snakes_and_ladders("L", 9)
        Game.get_players()

        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        while Game.Win != True:
            for player in Game.players:
                input("Stiskněte cokoli pro hod kostky")
                player.move()
                if Game.Win == True:
                    break
                input("Stiskněte cokoli pro pokračování")
                    
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')


class Player(Game):
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.square = 1
        if Game.player_count < Game.max_players:
            Game.player_count += 1
            self.id = Game.player_count + 3
            Game.player_dict[self.id] = {"name" : self.name, "square" : self.square}
        else:
            print("Byl překročen maximální počet hráčů.")

Game.play()









