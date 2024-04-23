# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:17:45 2023

@author: Michael.Agonsi
"""

import csv
column = ['Player','POS','AB','H','AVG']
Players = [['Joe', 'P ', 10, 2, 0.2],
           ['Tom', 'SS', 11, 4, 0.364],
           ['Ben', '3B', 9, 3, 0.333],
           ['Mike','C ', 4, 1, 0.25]]
with open('player_lineup.csv', 'w', newline="") as lineup:
    players = csv.writer(lineup)
    players.writerow(column)
    players.writerows(Players)