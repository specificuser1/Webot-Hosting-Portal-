import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("bots.db", check_same_thread=False)
        self.conn.execute("CREATE TABLE IF NOT EXISTS bots(token TEXT)")
        self.conn.commit()

    def add_bot(self, token):
        self.conn.execute("INSERT INTO bots VALUES(?)", (token,))
        self.conn.commit()

    def get_bots(self):
        data = self.conn.execute("SELECT token FROM bots").fetchall()
        return [i[0] for i in data]
