import psycopg2
import pandas as pd

username = 'Shevchenko_Nikolay'
password = 'Sapience69'
database = 'postgres'
host = 'localhost'
port = '5432'

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


query1 = """select player_id, TRIM(player_photo), TRIM(player_workrate), TRIM(player_name),
            player_age, TRIM(player_wage) ,country_id , team_id from players;"""

query2 = """select country_id, TRIM(country_name) from countries;"""
query3 = """select team_id, TRIM(team_name) from clubs;"""

with con:
    cur = con.cursor()
    cur.execute(query1)
    df = pd.DataFrame(cur)
    df.columns = ["player_id", "player_photo", "player_workrate", "player_name", "player_age", "player_wage",
            "country_id", "team_id"]
    df.to_csv("export_players.csv", index=False)
    print(df.head())


    cur.execute(query2)
    df = pd.DataFrame(cur)
    df.columns = ["country_id", "country_name"]
    df.to_csv("export_countries.csv", index=False)
    print(df.head())

    cur.execute(query3)
    df = pd.DataFrame(cur)
    df.columns = ["team_id", "team_name"]
    df.to_csv("export_clubs.csv", index=False)
    print(df.head())
