from time import time, gmtime
import tkinter as tk


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
        self.hide_new_game()
        self.show_end_game()

    def show(self, frame):
        self.acc_frame = tk.Frame(frame)
        self.acc_frame.grid(column=(self.idd % 3), row=(self.idd//3))
        self.acc_l = tk.Label(self.acc_frame, text=self.name)
        self.acc_l.grid()
        self.new_game_stake_i = tk.Entry(self.acc_frame)
        self.new_game_stake_i.grid()
        self.new_game_btn = tk.Button(
            self.acc_frame, text="New Game", command=lambda: self.add_game(time(), 100))
        self.new_game_btn.grid()

    def hide_new_game(self):
        self.new_game_stake_i.grid_forget()
        self.new_game_btn.grid_forget()

    def show_new_game(self):
        self.new_game_stake_i.grid()
        self.new_game_btn.grid()

    def show_end_game(self):
        self.result_i = tk.Entry(self.acc_frame)
        self.result_i.grid()
        self.end_game_btn = tk.Button(
            self.acc_frame, text="Finish Game", command=lambda: self.games[len(self.games)-1].end_game(time(), self.result_i.get()))
        self.end_game_btn.grid()


class Game:
    def __init__(self, starttime, stake, frame):
        self.start = starttime
        self.stake = stake
        self.end = None
        self.result = 0
        self.costs = 0
        self.profit = 0
        self.frame = frame
        self.show(frame)

    def add_cost(self, amount):
        self.costs += amount
        self.costs_var.set("Costs {}".format(self.costs))

    def end_game(self, endtime, result):
        self.end = endtime
        try:
            int(result)
            self.result = result
        except ValueError:
            self.error_l = tk.Label(self.frame, text="Input was incorrect")
            self.error_l.grid()

        #! Need to colapse data and calculate profit

    def show(self, frame):
        # Description
        self.game_l = tk.Label(frame, text="Current Game")
        self.game_l.grid()

        # Costs
        self.costs_var = tk.StringVar()
        self.costs_var.set("Costs 0")
        self.game_costs = tk.Label(frame, textvariable=self.costs_var)
        self.game_costs.grid()
        self.add_cost_one = tk.Button(
            frame, text="+1", command=lambda: self.add_cost(100))
        self.add_cost_one.grid()
        self.add_cost_two = tk.Button(
            frame, text="+2", command=lambda: self.add_cost(200))
        self.add_cost_two.grid()
        self.add_cost_three = tk.Button(
            frame, text="+3", command=lambda: self.add_cost(300))
        self.add_cost_three.grid()
