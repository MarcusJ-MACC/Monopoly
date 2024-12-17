import random
def Dice_Roll():
    return random.randint(1,6)
class Board:
    def __init__(self):
        self.spaces = []
        self.spaces.append(Go_Space())
        self.spaces.append(Property("Old Kent Road", 60, 2, "Brown"))
        self.spaces.append(Space("Community Chest")) # TODO
        self.spaces.append(Property("Whitechapel Road", 60, 4, "Brown"))
        self.spaces.append(Tax("Income Tax", 200))
        self.spaces.append(Station("King's Cross Station"))
        self.spaces.append(Property("The Angel Islington", 100, 6, "Light Blue"))
        self.spaces.append(Space("Chance")) # TODO
        self.spaces.append(Property("Euston Road", 100, 6, "Light Blue"))
        self.spaces.append(Property("Pentonville Road", 120, 8, "Light Blue"))
        self.spaces.append(Space("Just Visiting"))
        self.spaces.append(Property("Pall Mall", 140, 10, "Pink"))
        self.spaces.append(Utility("Electric Company"))
        self.spaces.append(Property("Whitehall", 140, 10, "Pink"))
        self.spaces.append(Property("Northumberland Avenue", 160, 12, "Pink"))
        self.spaces.append(Station("Marylebone Station"))
        self.spaces.append(Property("Bow Street", 180, 14, "Orange"))
        self.spaces.append(Space("Community Chest")) # TODO
        self.spaces.append(Property("Marlborough Street", 180, 14, "Orange"))
        self.spaces.append(Property("Vine Street", 200, 16, "Orange"))
        self.spaces.append(Space("Free Parking"))
        self.spaces.append(Property("Strand", 220, 18, "Red"))
        self.spaces.append(Space("Chance")) # TODO
        self.spaces.append(Property("Fleet Street", 220, 18, "Red"))
        self.spaces.append(Property("Trafalgar Square", 240, 20, "Red"))
        self.spaces.append(Station("Fenchurch St Station"))
        self.spaces.append(Property("Leicester Square", 260, 22, "Yellow"))
        self.spaces.append(Property("Coventry Street", 260, 22, "Yellow"))
        self.spaces.append(Utility("Water Works"))
        self.spaces.append(Property("Piccadilly", 280, 24, "Yellow"))
        self.spaces.append(Go_To_Jail())
        self.spaces.append(Property("Regent Street", 300, 26, "Green"))
        self.spaces.append(Property("Oxford Street", 300, 26, "Green"))
        self.spaces.append(Space("Community Chest")) # TODO
        self.spaces.append(Property("Bond Street", 320, 28, "Green"))
        self.spaces.append(Station("Liverpool St Station"))
        self.spaces.append(Space("Chance")) # TODO
        self.spaces.append(Property("Park Lane", 350, 35, "Dark Blue"))
        self.spaces.append(Tax("Super Tax", 100))
        self.spaces.append(Property("Mayfair", 400, 50, "Dark Blue"))

    def __str__(self): #TODO: make players appear on the board - Marcus
        board = """
        ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗
        ║F P║STR║CHA║FLT║TRF║FNS║LST║COV║W W║PIC║GTJ║
        ╠═══╬═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╬═══╣
        ║VIN║                                   ║REG║
        ╠═══╣                                   ╠═══╣
        ║MAR║                                   ║OXF║
        ╠═══╣                                   ╠═══╣
        ║C C║                                   ║C C║
        ╠═══╣                                   ╠═══╣
        ║BOW║                                   ║BND║
        ╠═══╣                                   ╠═══╣
        ║MBS║                                   ║LSS║
        ╠═══╣                                   ╠═══╣
        ║NOR║                                   ║CHA║
        ╠═══╣                                   ╠═══╣
        ║WHT║                                   ║PAR║
        ╠═══╣                                   ╠═══╣
        ║E C║                                   ║S T║
        ╠═══╣                                   ╠═══╣
        ║PAL║                                   ║MAY║
        ╠═══╬═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╬═══╣
        ║J V║PTV║EUS║CHA║TAI║KCS║I T║WCR║C C║OKR║G O║
        ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝
        """
        CurrentPlayerIndexes = []
        for i in range(len(self.spaces)):
            if len(self.spaces[i].currentPlayers)>0:
                CurrentPlayerIndexes.append([self.spaces[i].currentPlayers[0],i])
        #NOTE: board[54*(2n-1):54*(2n)] gives the nth row of the board
        #NOTE: board[54*(2*row-1)+10+4*(col-1):54*(2*row-1)+10+4*(col-1)+3] returns the string of whatever is at the space on row,column e.g. row=1 col=1 returns "F P", row=11 col=5 returns "TAI"
        rows = []
        columns = []
        for i in CurrentPlayerIndexes:
            if i <=10:
                rows.append(11)
                columns.append(11-i)
            elif i<=19:
                columns.append(1)
                rows.append(11-i%10)
            elif i<=30:
                rows.append(1)
                columns.append(i-19)
            else:
                columns.append(11)
                rows.append(i%10+1)
        for i in range(len(rows)):
            row=rows[i]
            col=columns[i]
            print(board[54*(2*row-1)+10+4*(col-1):54*(2*row-1)+10+4*(col-1)+3])
        return ""

class Space:
    def __init__(self, name):
        self.name = name
        self.currentPlayers = []

    def on_land(self, player):
        self.currentPlayers.append(player)

class Go_Space(Space):
    def __init__(self):
        Space.__init__(self, "Go")

    def on_land(self, player):
        player.add_money(200)

class Go_To_Jail(Space):
    def __init__(self):
        Space.__init__(self, "Go To Jail")

    def on_land(self, player):
        player.go_to_jail()

class Tax(Space):
    def __init__(self, name, tax):
        Space.__init__(self, name)
        self.tax = tax

    def on_land(self, player):
        player.pay_bank(self.tax)

class Property(Space):
    def __init__(self, name, cost, rent, set):
        Space.__init__(self, name)
        self.cost = cost
        self.rent = rent
        self.super_rent = rent * 2
        self.owner = None
        self.set = set

    def on_land(self, player):
        if self.owner is None:
            player.buy(self)
        else:
            player.pay(self.owner, self.rent)
            # TODO: double rent if full set owned - Seth

class Station(Property):
    def __init__(self, name):
        Property.__init__(self, name, 200, 25, "Stations")


    def on_land(self, player):
        if self.owner is None:
            player.buy(self)
        else:
            player.pay(self.owner, self.rent * (2 ** (self.owner.num_owned("Stations") - 1)))

class Utility(Property):
    def __init__(self, name):
        Property.__init__(self, name, 150, 4, "Utilities")
        self.super_rent = 10
    
    
    def on_land(self, player):
        if self.owner is None:
            player.buy(self)
        else:
            pass # TODO: pay rent = 4 x dice roll (or 10x if both owned) - Seth
# TODO: implement player logic - Marcus
class Player:
    def __init__(self, name, game_piece, Board):
        self.name = name
        if game_piece not in ["thimble", "boot", "cannon", "battleship", "car", "terrier dog"]:
            raise ValueError("Piece must be one of thimble, boot, cannon, battleship, car, or terrier dog")
        self.gamer_piece = game_piece
        self.money = 0
        self.properties = []
        self.current_space = None
        self.board = Board
        self.jailed = False

    def add_money(self, amount):
        self.money += amount

    def pay_bank(self, amount):
        self.money -= amount

    def pay(self, player, amount):
        if self != player:
            self.money -= amount
            if self.money <= 0:
                player.money += amount + self.money
                self.is_bankrupt()
            else:
                player.money += amount 

    def go_to_jail(self):
        self.current_space = self.board.spaces[10]

    def move(self, board):
        roll_one = Dice_Roll()
        roll_two = Dice_Roll()
        currentIndex = self.Board.spaces.find(self.current_space)
        currentIndex = (currentIndex+roll_one + roll_two) % len(self.Board.spaces) - 1
        self.current_space = self.board.spaces[currentIndex]
        self.current_space.currentPlayers.pop(0)
        return [roll_one, roll_two]
        # TODO: player rolls dice, moves that many spaces

    def is_bankrupt(self):
        if self.money <= 0:
            return True
        
    def num_owned(self,set_):
        num = 0
        for Owned in self.properties:
            if Owned.set == set_:
                num+=1
        return num
    
    def set_owned(self, set_):
        if set_ == "Brown" or set_=="Dark Blue":
            if self.num_owned(set_) == 2:
                return True
            else:
                return False
        else:
            if self.num_owned(set_) == 3:
                return True
            else:
                return False
    def buy(self, Property):
        playerInput = None
        if self.money < Property.rent:
            print(f"You cannot buy {Property.name}")
            playerInput = "n"
        
        while not playerInput:
            playerInput = input(f"Do you want to buy {Property.name}? (y/n)").lower()
            if playerInput not in ["y","n"]:
                playerInput = None
                print("Input needs to be 'y' or 'n'")
        if playerInput == "y":
            self.pay_bank(Property.rent)
            self.properties.append(Property)
            Property.owner=self
    def __str__(self):
        return self.gamer_piece[0:3].upper()
print(Board())
class Game:
    def __init__(self):
        self.board = Board()
        self.players = []

    def add_player(self):
        pass # TODO: add a player with name, game piece, starting money, etc - Helena

    def setup(self):
        num_players = int(input("How many players? ")) # TODO: add error handling for bad inputs - Helena
        for i in range(num_players):
            self.add_player(self.board)
        
        current_player = self.players[0] # TODO: have players roll 1d6 to see who goes first - Helena

        game_over = False
        while not game_over:
            print(self.board)
            print(f"{current_player.name}'s turn:")
            input("press enter to roll")
            current_player.move(self.board)
            current_player.current_space.on_land(current_player)
            # TODO: roll again on double, send to jail on triple-double - Helena

            next_player = self.players[(self.players.index(current_player) + 1) % len(self.players)]
            if current_player.is_bankrupt():
                print(f"{current_player.name} is bankrupt!")
                self.players.remove(current_player)
                if len(self.players) == 1:
                    game_over = True
            current_player = next_player

        print(f"""
        Game over!
        {current_player.name} wins!
        They had £{current_player.money}
        """)
