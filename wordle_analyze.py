import sqlite3
from datetime import datetime

class WordleAnalyze:

    def __init__(self) -> None:
        self.con = sqlite3.connect('logger.db',detect_types=sqlite3.PARSE_DECLTYPES)
        self.cur = self.con.cursor()
        self.start_date = datetime.now()
        self.start_date = self.start_date.replace(hour=00,minute=00, second=00, microsecond=00)
        self.end_date = datetime.now()
        self.end_date = self.end_date.replace(hour=23, minute=59, second=59, microsecond=00)
    
    def select_start_date(self) -> None:
        try:
            print("Enter start date in the format mm-dd-yyyy. (Press enter to skip and take today's date)")
            start_input = input()
            if start_input:
                self.start_date = datetime.strptime(start_input, "%m-%d-%Y")
                self.start_date = self.start_date.replace(hour=00,minute=00, second=00, microsecond=00)
        except:
            print("Invalid date. Try again")
            self.start_date = datetime.now()
            self.start_date = self.start_date.replace(hour=00,minute=00, second=00, microsecond=00)
            self.select_start_date()

    def select_end_date(self)-> None:
        try:
            print("Enter end date in the format mm-dd-yyyy. (Press enter to skip and take today's date)")
            end_input = input()
            if end_input:
                self.end_date = datetime.strptime(end_input, "%m-%d-%Y")
                self.end_date = self.end_date.replace(hour=23, minute=59, second=59, microsecond=00)
        except:
            print("Invalid date. Try again")
            self.end_date = datetime.now()
            self.end_date = self.end_date.replace(hour=23, minute=59, second=59, microsecond=00)
            self.select_end_date()
    
    def get_report(self)-> None:
        self.select_start_date()
        self.select_end_date()
        db_report = open('report.txt', 'w')
        print("\n***Generating Report from Database****\n")
        db_report.write("***Report from Database****\n")
        print(f"Game Statistics Report from {self.start_date.strftime('%m-%d-%Y')} to {self.end_date.strftime('%m-%d-%Y')}")
        db_report.write(f"Game Statistics Report from {self.start_date.strftime('%m-%d-%Y')} to {self.end_date.strftime('%m-%d-%Y')}\n")
        self.cur.execute("SELECT * FROM game WHERE date BETWEEN :start AND :end",{"start":self.start_date,"end":self.end_date})
        data = self.cur.fetchall()
        self.cur.execute("SELECT * FROM game_stats ORDER BY rowid DESC LIMIT 1")
        game_stat = self.cur.fetchone()
        print(f'Total Games Played: {len(data)}')
        db_report.write(f'Total Games Played: {len(data)}\n')
        print(f'Total Games Won: {game_stat[4]}')
        db_report.write(f'Total Games Won: {game_stat[4]}\n')
        print(f'Guess Distribution: ')
        db_report.write(f'Guess Distribution: \n')
        guess = game_stat[5][1:-1].replace(' ','').split(',')
        for i, dist in enumerate(guess):
            print(f'Attempt {i+1}: {dist}')
            db_report.write(f'Attempt {i+1}: {dist}\n')
        db_report.close();
        
