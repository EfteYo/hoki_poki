from time import time, gmtime
import tkinter as tk
from models import Session, Account, Game


class App:
    def __init__(self, master):
        self.session = None
        self.master = master

        # Presets for accounts
        self.acc_preset_a = ["Account 1"]
        self.acc_preset_b = ["Account 1",
                             "Account 2",
                             "Account 3",
                             "Account 4"]

        master.title("Hoki Poki 1.1")

        # Frame on the top of the window to show information about the session
        self.header = tk.Frame(master)
        self.header.grid(padx=10, pady=10, sticky="w")

        self.brand = tk.Label(self.header, text="Hoki Poki", anchor="w")
        self.brand.grid(sticky="w")

        self.stats_l = tk.Button(self.header, text="See Stats", command=lambda: self.show_stats())
        self.stats_l.grid(row=0, column=1, sticky="w")

        self.error_message_l = tk.Label(self.header, text = "", anchor="e")
        self.error_message_l.grid(row=0, column=2,columnspan=3, sticky = "e")

        self.show_new_session()

    def show_new_session(self):
        '''Part to start new sessions'''
        self.sess_name_l = tk.Label(self.header, text="Session Name:", anchor="w")
        self.sess_name_l.grid(row=1, column=0, sticky="w")
        self.sess_name_i = tk.Entry(self.header)
        self.sess_name_i.grid(row=1, column=1)
        self.sess_startbalance_l = tk.Label(self.header, text="Startbalance:")
        self.sess_startbalance_l.grid(row=1, column=2)
        self.sess_startbalance_i = tk.Entry(self.header)
        self.sess_startbalance_i.grid(row=1, column=3)
        self.btn_start = tk.Button(
            self.header, text="Start Session", command=lambda: self.start_session(self.sess_name_i.get(), self.sess_startbalance_i.get()))
        self.btn_start.grid(row=1, column=4)

    def hide_new_session(self):
        self.sess_name_l.grid_forget()
        self.sess_name_i.grid_forget()
        self.sess_startbalance_l.grid_forget()
        self.sess_startbalance_i.grid_forget()
        self.btn_start.grid_forget()

    def show_cur_session(self):
        '''Part with information about the session'''
        self.sess_show_name_l = tk.Label(self.header, text=self.session.name, anchor="w")
        self.sess_show_name_l.grid(row=1, column=0, sticky="w")
        self.btn_end = tk.Button(
            self.header, text="End Session", command=lambda: self.end_session())
        self.btn_end.grid(row=1, column=1)

    def hide_cur_session(self):
        self.sess_show_name_l.grid_forget()
        self.btn_end.grid_forget()

    def start_session(self, sessionname, startbalance):
        try:
            self.clear_error()
            self.session = Session(sessionname, time(), int(startbalance))
            self.hide_new_session()
            self.show_cur_session()

            try:
                self.session_stats_f.grid_remove()
            except AttributeError:
                pass

            self.body = tk.Frame(self.master)
            self.body.grid(padx=10, pady=10)

            # creates the accounts from the templates
            for i, name in enumerate(self.acc_preset_b):
                self.session.add_account(name, i)

            # brings the created accounts on the screen (the body frame)
            for acc in self.session.accounts:
                acc.show(self.body)

            print("Session startet at {}".format(gmtime(time())))

        except ValueError:
            self.show_error("Startbalance must be a number")
            

        
         

        # Frame to show the main content, thus the accounts and their games

    def end_session(self):
        
        self.session.end = time()
        self.session.evaluate_session()

        self.session_stats_f = tk.Frame(self.master)
        self.session_stats_f.grid(padx=10, pady=10)

        self.profit_total_l = tk.Label(self.session_stats_f, text = "Total profit: {}".format(self.session.profit_total), anchor = "w")
        self.profit_total_l.grid()

        self.balance_total_l = tk.Label(self.session_stats_f, text = "Total balance: {}".format(self.session.balance_total), anchor = "w")
        self.balance_total_l.grid()

        self.rake_total_l = tk.Label(self.session_stats_f, text = "Total rake: {}".format(self.session.rake_total), anchor = "w")
        self.rake_total_l.grid()

        self.amount_games_l = tk.Label(self.session_stats_f, text = "Games: {}".format(self.session.amount_games), anchor = "w")
        self.amount_games_l.grid()
        
        self.duration_l = tk.Label(self.session_stats_f, text = "Duration: {}".format(self.format_duration(self.session.duration)), anchor = "w")
        self.duration_l.grid()


        self.session = None
        self.body.grid_forget()
        self.hide_cur_session()
        self.show_new_session()


    def save_session(self, session):
        '''stores the session from the argument in a database'''
        ...

    def show_stats(self):
        self.top = tk.Toplevel()
        self.top.title("Hoki Poki 1.1 Stats")
        self.top_frame = tk.Frame(self.top)
        self.top_frame.grid()
        self.top_l = tk.Label(self.top_frame, text="Crazy Stats")
        self.top_l.grid()
        self.ex_l = tk.Label(self.top_frame, text="0030023523534025")
        self.ex_l.grid(row=1)

    def format_duration(self, duration):
        duration_f = ""
        if duration//3600 < 10:
            duration_f += "0"
            duration_f += str(duration//3600)
        else:
            duration_f += str(duration//3600)
        duration_f += ":"
        if duration%3600//60 < 10:
            duration_f += "0"
            duration_f += (str(duration%3600//60))
        else:
            duration_f += (str(duration%3600//60))
        return duration_f
        
    def show_error(self, message):
        self.error_message_l.configure(text = message)   

    def clear_error(self):
        self.error_message_l.configure(text = "")
        


if __name__ == "__main__":
    root = tk.Tk()          # creates the main window
    app = App(root)         # calls our app class from above
    root.mainloop()         # permission for the window to stay open
