class Session:
    '''One poker session with multiple accounts'''
    def __init__(self, name, starttime, startbalance=0):
        self.name = name
        self.start = starttime
        self.startbalance = startbalance
        self.end = None
        self.accounts = []

    def add_account(self, name):
        self.accounts.append(Account(name))

class Account:
    def __init__(self, name):
        self.name = name
        self.games = []

    def set_name(self, name):
        self.name = name

    def add_game(self, starttime, stake):
        self.games.append(Game(starttime, stake))

class Game:
    def __init__(self, starttime, stake):
        self.start = starttime
        self.stake = stake
        self.end = None
        self.result = 0
        self.costs = 0
        self.profit = 0
        
    def end(self, endtime, result):
        self.end = endtime
        self.result = result