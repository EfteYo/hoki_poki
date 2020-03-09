import tkinter as tk
from time import time, gmtime

class Session:
    '''One poker session with multiple accounts'''
    def __init__(self, name, starttime, startbalance=0):
        self.name = name
        self.start = starttime
        self.startbalance = startbalance
        self.end = None
        self.accounts = []

    def add_account(self, name, idd):
        self.accounts.append(Account(name, idd))

class Account:
    def __init__(self, name, idd):
        self.idd = idd
        self.name = name
        self.games = []

    def set_name(self, name):
        self.name = name

    def add_game(self, starttime, stake):
        self.games.append(Game(starttime, stake, self.acc_frame))

    def show(self, frame):
        self.acc_frame = tk.Frame(frame)
        self.acc_frame.grid(column=(self.idd%3), row=(self.idd//3))
        self.acc_l = tk.Label(self.acc_frame, text=self.name)
        self.acc_l.grid()
        self.new_game_stake_i = tk.Entry(self.acc_frame)
        self.new_game_stake_i.grid()
        self.new_game_btn = tk.Button(self.acc_frame, text="New Game", command=lambda: self.add_game(time(), 100))
        self.new_game_btn.grid()

class Game:
    def __init__(self, starttime, stake, frame):
        self.start = starttime
        self.stake = stake
        self.end = None
        self.result = 0
        self.costs = 0
        self.profit = 0
        self.show(frame)

    def add_cost(self, amount):
        self.costs += amount
        self.costs_var.set("Costs {}".format(self.costs))

        
    def endGame(self, endtime, result):
        self.end = endtime
        self.result = result

    def show(self, frame):
        self.costs_var = tk.StringVar()
        self.costs_var.set("Costs 0")
        self.game_l = tk.Label(frame, text="Current Game")
        self.game_l.grid()
        self.game_costs = tk.Label(frame, textvariable=self.costs_var)
        self.game_costs.grid()
        self.add_cost_one = tk.Button(frame, text="+1", command=lambda: self.add_cost(100))
        self.add_cost_one.grid() #column=0, row=0
        self.add_cost_two = tk.Button(frame, text="+2", command=lambda: self.add_cost(200))
        self.add_cost_two.grid()#column=1, row=0)
        self.add_cost_three = tk.Button(frame, text="+3", command=lambda: self.add_cost(300))
        self.add_cost_three.grid()#column=2, row=0)