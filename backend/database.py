import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("bots.db", check_same_thread=False)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS bots(
                token TEXT UNIQUE
            )
        """)
        self.conn.commit()

    def add_bot(self, token: str):
        self.conn.execute("INSERT OR IGNORE INTO bots (token) VALUES (?)", (token,))
        self.conn.commit()

    def add_bulk(self, tokens: list[str]):
        for t in tokens:
            self.conn.execute("INSERT OR IGNORE INTO bots (token) VALUES (?)", (t,))
        self.conn.commit()

    def get_all(self):
        result = self.conn.execute("SELECT token FROM bots").fetchall()
        return [i[0] for i in result]
