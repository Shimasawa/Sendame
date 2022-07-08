class Player:
    """An object that represents the player"""
    
    action: str
    charge: int
    entry: bool
    name: str

    def __init__(self):
        self.action = None
        self.charge = 0
        self.entry = False
        self.name = None
    
    def is_charge(self) -> bool:
        if self.charge > 0:
            return True
        return False

class Sendame:
    """An object that represents one game"""

    player_1: Player
    player_2: Player
    turn: int

    def __init__(self):
        self.player_1 = Player()
        self.player_2 = Player()
        self.turn = 0
    
    def action(self,player: Player,player_action: str):
        if player.entry:
            raise Exception("Already entered")
        
        if player_action not in ["タメ","バリア","ハー"]:
            raise ValueError("Should choose from 'タメ','バリア','ハー'")
        
        if player_action == "ハー" and player.is_charge():
            player.charge -= 1
        elif player_action == "ハー" and not player.is_charge():
            raise Exception("Not enough charge")
        
        if player_action == "タメ":
            player.charge += 1

        player.action = player_action
        player.entry = True

    def showdown(self):
        selection = (self.player_1.action,self.player_2.action)
        
        if selection in [("ハー","ハー"),("ハー","バリア"),("バリア","ハー")] or "ハー" not in selection:
            result = None
        elif selection == ("ハー","タメ"):
            result = self.player_1
        elif selection == ("タメ","ハー"):
            result = self.player_2

        self.turn += 1
        self.player_1.entry = False
        self.player_2.entry = False

        return result