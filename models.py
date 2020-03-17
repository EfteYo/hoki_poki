from time import time, gmtime
import tkinter as tk
import json


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

    def evaluate_session(self):
        self.profit_total = 0
        self.rake_total = 0
        self.cost_total = 0
        self.amount_games = 0
        self.amount_costs = 0
        for account in self.accounts:
            for game in account.games:
                self.profit_total += game.profit
                self.rake_total += game.rake
                self.cost_total += game.costs
                self.amount_costs += game.costs // game.stake
                self.amount_games += 1

        self.duration = round(self.end - self.start)

        self.balance_total = self.profit_total + self.startbalance

    def session_to_JSON(self):
        accounts = []
        for account in self.accounts:
            games = []
            for game in account.games:
                game_dict = {
                    "starttime": game.start,
                    "endtime": game.end,
                    "stake": game.stake,
                    "result": game.result,
                    "costs": game.costs,
                    "profit": game.profit
                }
                games.append(game_dict)

            account_dict = {
                "name": account.name,
                "games": games
            }
            accounts.append(account_dict)

        session_stats_dict = {
            "name": self.name,
            "starttime": self.start,
            "endtime": self.end,
            "startbalance": self.start,
            "endbalance": self.balance_total,
            "profit": self.profit_total,
            "rake": self.rake_total,
            "costs": self.cost_total,
            "amount_costs": self.amount_costs,
            "duration": self.duration,
            "accounts": accounts
        }

        return json.dumps(session_stats_dict)


class Account:
    def __init__(self, name, idd):
        self.idd = idd
        self.name = name
        self.games = []

    def set_name(self, name):
        self.name = name

    def add_game(self, starttime, stake):
        try:
            self.games.append(Game(starttime, float(stake), self.acc_frame))
            self.hide_new_game()
            self.show_end_game()
        except ValueError:
            print("Wooong")



    def show(self, frame):
        self.acc_frame = tk.Frame(frame)
        self.acc_frame.grid(column=(self.idd % 3), row=(self.idd//3))
        self.acc_l = tk.Label(self.acc_frame, text=self.name)
        self.acc_l.grid()
        self.new_game_stake_i = tk.Entry(self.acc_frame)
        self.new_game_stake_i.grid()
        self.new_game_btn = tk.Button(
            self.acc_frame, text="New Game", command=lambda: self.add_game(time(), self.new_game_stake_i.get()))
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
            self.acc_frame, text="Finish Game", command=lambda: self.end_game())
        self.end_game_btn.grid()

    def hide_end_game(self):
        self.result_i.grid_forget()
        self.end_game_btn.grid_forget()

    def end_game(self):
        self.games[-1].end_game(time(), self.result_i.get())
        self.hide_end_game()
        self.show_new_game()


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
        self.rake = 0
        try:
            self.result = float(result)
            if self.result > 0:
                self.profit = self.result*0.95 - self.costs
                self.rake = self.result*0.05
            elif self.result <= 0:
                self.profit = self.result - self.costs
            self.hide()
            self.show_profit_l = tk.Label(self.frame, text=str(self.profit))
            self.show_profit_l.grid()

        except ValueError:
            print("Wooong")

    def show(self, frame):
        # Description
        self.game_l = tk.Label(frame, text="Current Game")
        self.game_l.grid()

        # Costs
        self.costs_var = tk.StringVar()
        self.costs_var.set("Costs 0")
        self.game_costs = tk.Label(frame, textvariable=self.costs_var)
        self.game_costs.grid()
        btn_frame = tk.Frame(frame)
        btn_frame.grid()
        self.add_cost_one = tk.Button(
            btn_frame, text="1bb", command=lambda: self.add_cost(self.stake))
        self.add_cost_one.grid(column=0, row=0)
        self.add_cost_two = tk.Button(
            btn_frame, text="2bb", command=lambda: self.add_cost(self.stake*2))
        self.add_cost_two.grid(column=1, row=0)
        self.add_cost_three = tk.Button(
            btn_frame, text="3bb", command=lambda: self.add_cost(self.stake*3))
        self.add_cost_three.grid(column=2, row=0)

    def hide(self):
        self.game_l.grid_forget()
        self.game_costs.grid_forget()
        self.add_cost_one.grid_forget()
        self.add_cost_two.grid_forget()
        self.add_cost_three.grid_forget()
