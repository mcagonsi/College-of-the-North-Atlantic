import sqlite3
from objects import Player


DATABASE = 'Baseball_Team.db'

def get_pos():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute('SELECT * FROM position')

    pos = c.fetchall()
    conn.close()
    return pos

def insert_player(player):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    query = "INSERT INTO player(?,?,?,?,?,?)"
    c.execute(query, (player.ID, player.fName, player.lName, player.pos, player.atBats, player.hits))
    conn.commit()
    conn.close()

def update_player(player):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    query = "UPDATE player SET fName = ?, lName = ?, pos = ?, atBats = ?, hits = ? WHERE id = ?"
    c.execute(query, (player.fName, player.lName, player.pos, player.atBats, player.hits, player.ID))
    conn.commit()
    conn.close()

def get_player(player):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    query = "SELECT * FROM player WHERE id = ?"
    c.execute(query, (player.id,))
    player = c.fetchall()
    conn.close()
    return player

