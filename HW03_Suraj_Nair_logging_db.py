import sqlite3
from datetime import datetime
import socket


class Logger:

    def __init__(self) -> None:
        self.con = sqlite3.connect('logger.db',detect_types=sqlite3.PARSE_DECLTYPES)
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE if not exists game (id integer primary key autoincrement, date timestamp, ip text, game_word text)''')
        self.cur.execute('''CREATE TABLE if not exists game_info (id integer primary key autoincrement, date timestamp, attempt integer,user_word text, game_id integer, FOREIGN KEY(game_id) REFERENCES game(id))''')
        self.cur.execute('''CREATE TABLE if not exists game_stats (id integer primary key autoincrement, date timestamp, game_outcome text, games_played integer, win_rate real, guess_distribution text, game_id integer, FOREIGN KEY(game_id) REFERENCES game(id))''')
        self.ip = self.get_ip()
        self.current_game_id = None
    
    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP


    def write_game_log(self,game_word:str)->None:
        time = datetime.now()
        self.cur.execute("insert into game values (NULL, ?, ?, ?)", (time, self.ip, game_word))
        self.current_game_id = self.cur.lastrowid


    def write_game_info_log(self, attempt:int, user_word:str) -> None:
        time = datetime.now()
        self.cur.execute("insert into game_info values (NULL, ?, ?, ?, ?)", (time, attempt, user_word, self.current_game_id))
    

    def write_game_stats_log(self, did_win:bool, games_played:int, win_rate: float, guess_dist :str) -> None:
        time = datetime.now()
        win_text = "Won" if did_win else "Lost"
        self.cur.execute("insert into game_stats values (NULL, ?, ?, ?, ?, ?, ?)", (time, win_text, games_played, win_rate, guess_dist, self.current_game_id))
        self.con.commit()

    def close_log(self) -> None:
        self.con.commit()
        self.con.close()