# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:38:02 2023

@author: Michael.Agonsi
"""
import csv
def r():
    with open('player_lineup.csv', 'r', newline="") as lineup:
        players = csv.reader(lineup)
    return players

def w(player):
    with open ('player_lineup.csv','w', newline='') as lineup:
        players = csv.writer(lineup)
        players.writerows(player)