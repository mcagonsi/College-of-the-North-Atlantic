import csv
with open('song_list.txt') as file:
    playlist = file.read().split(', ')
print(playlist)