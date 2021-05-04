# Name: Yonatan Babore
# Date: May 3rd 2021
# Description: This scrip scrapes the jeopardy archives and stores the information into a local sqlite3 db

import requests
import sqlite3
from bs4 import BeautifulSoup as bs
import numpy as np
import re
import lxml
from w3lib.html import replace_entities
import os # get current file path directorry

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

###################### GET THE GENERAL SEASON INFORMATION #################
# r = requests.get("https://www.j-archive.com/listseasons.php")
# soup = bs(r.text, "html.parser")

# # for each season get its number, date range, and number of games archived
# table = soup.select("table")
# trs = soup.find_all("tr")

# seasons = []
# for i in np.arange(len(trs)):
#   tds = trs[i].find_all("td")
#   features = [td.text.strip() for td in tds if td.text.strip() != ""]
#   seasons.append(features)

# # clean up information to fit the following season - date - game format
#   # Season 37, 2020-09-14 to 2021-08-13, 156

# for season in seasons:
#   season[2] = season[2].split(" ")[0]
#   season[2] = season[2][1:]
#   season[0] = season[0].replace("Season ", "")
# ##### SEASON LIST FORMAT : ['36', '2019-09-09 to 2020-06-12', '190'] (season, date, num games archived)

# # Put General Season Information into Table

# # create connection with database
# conn = sqlite3.connect("Jeopardy.db")

# c = conn.cursor()

# c.execute(""" CREATE TABLE JeopardySeasons (
# 			Season text,
# 			DateRange text,
# 			GameCount int
# 			)
# 			""")

# for season in seasons:
# 	c.execute("INSERT INTO JeopardySeasons VALUES  (?, ?, ?)", (season[0], season[1], season[2]))
# 	conn.commit()

# conn.close()

################ SECOND GET THE SPECIFIC SEASON INFORMATION ###############
# create a list of al of the seasnos
# special_seasons = np.array(["goattournament", "trebekpilot", "superjeopardy"]) 
# seasons = np.arange(37)
# np.concatenate((seasons, special_seasons))

# # create a table of games and seasons
# conn = sqlite3.connect("Jeopardy.db")
# c = conn.cursor()

# # c.execute(""" CREATE TABLE GameBasicInformation (
# # 	GameNumber int,
# # 	Year int,
# # 	Month int,
# # 	Day int,
# # 	GameType text,
# # 	GameID int)
# # 	""")

# for season in seasons:
# 	r = requests.get("https://www.j-archive.com/showseason.php?season={}".format(str(season)))
# 	soup = bs(r.text, "html.parser")

# 	# for each game get its number, id, air_date, and type of game
# 	table = soup.select("table")
# 	trs = soup.find_all("tr")

# 	games = []
# 	for i in np.arange(len(trs)):
# 	  tds = trs[i].find_all("td")
# 	  features = [td.text.strip() for td in tds if td.text.strip() != ""]
# 	  if (len(features) == 2):
# 	    features.append("Normal")

# 	  # clean up the game and date information
# 	  game_and_date = features[0]
# 	  pattern = "\d+"
# 	  temp_list = re.findall(pattern, game_and_date)
# 	  features.remove(features[0])
# 	  temp_list.extend(features)
# 	  temp_list.remove(temp_list[4])

# 	  # get the game_id
# 	  tds = trs[i].find_all("a")
# 	  string = tds[0]["href"]
# 	  pattern = "\d+"

# 	  game_id = re.findall(pattern, string)[0]
# 	  temp_list.append(game_id)
# 	  games.append(temp_list)

# ##### GAMES LIST FORMAT: ['6239','2011','11','03','2011 Tournament of Champions quarterfinal game 2.','3752']
# 		# (game number, year, month, day, game type, game_id)
# 	for game in games:
# 		c.execute("INSERT INTO GameBasicInformation VALUES (?, ?, ?, ?, ?, ?)", (game[0], game[1], game[2], game[3], game[4], game[5]))
# 		conn.commit()

# conn.close()










