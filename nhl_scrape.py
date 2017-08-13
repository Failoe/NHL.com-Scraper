import requests
import json
import csv

site = """http://www.nhl.com/stats/rest/grouped/team/basic/game/realtime?cayenneExp=gameDate%3E=%222016-10-12T07:00:00.000Z%22%20and%20gameDate%3C=%222017-04-11T06:59:59.999Z%22%20and%20gameLocationCode=%22H%22%20and%20gameTypeId=%222%22&factCayenneExp=gamesPlayed%3E=1&sort=[{%22property%22:%22hits%22,%22direction%22:%22DESC%22}]"""
blob = requests.get(site).content
json_data = json.loads(blob)['data']
csv_file = csv.writer(open("NHL.csv", "w+", newline=""))
csv_file.writerow([
					"blockedShots",
					"faceoffWinPctg",
					"faceoffs",
					"faceoffsLost",
					"faceoffsWon",
					"gameDate",
					"gameId",
					"gameLocationCode",
					"gamesPlayed",
					"giveaways",
					"goalsFor",
					"hits",
					"losses",
					"opponentTeamAbbrev",
					"otLosses",
					"points",
					"shootingPctg",
					"shotsFor",
					"takeaways",
					"teamAbbrev",
					"teamFullName",
					"teamId",
					"ties",
					"wins"])

for x in json_data:
	csv_file.writerow([
						x["blockedShots"],
						x["faceoffWinPctg"],
						x["faceoffs"],
						x["faceoffsLost"],
						x["faceoffsWon"],
						x["gameDate"],
						x["gameId"],
						x["gameLocationCode"],
						x["gamesPlayed"],
						x["giveaways"],
						x["goalsFor"],
						x["hits"],
						x["losses"],
						x["opponentTeamAbbrev"],
						x["otLosses"],
						x["points"],
						x["shootingPctg"],
						x["shotsFor"],
						x["takeaways"],
						x["teamAbbrev"],
						x["teamFullName"],
						x["teamId"],
						x["ties"],
						x["wins"]])
