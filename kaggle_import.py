import psycopg2
import pandas as pd

username = 'Shevchenko_Nikolay'
password = 'Sapience69'
database = 'postgres'
host = 'localhost'
port = '5432'

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)




#opening team csv file and
#writing it into created erlier a data base tables
df = pd.read_csv("club.csv", sep=",")
with con:
    cur = con.cursor()
    cur.execute("DELETE FROM clubs;")
    for ind in df.index:
        query = f'''
INSERT INTO clubs(team_id,
                    team_name)
VALUES ({df['id'][ind]}, '{df['club'][ind]}');

'''
        cur.execute(query)

#opening college csv file and
#writing it into created erlier a data base tables
df = pd.read_csv("nationality.csv")
with con:
    cur = con.cursor()
    cur.execute("DELETE FROM countries;")
    for ind in df.index:
        query = f'''
INSERT INTO countries(country_id,
                    country_name)
VALUES ({df['id'][ind]}, '{df['nationality'][ind]}');

'''
        cur.execute(query)



#opening palyers csv file and
#writing it into created erlier a data base tables
df = pd.read_csv("players.csv", sep=";")

with con:
    cur = con.cursor()
    cur.execute("DELETE FROM players;")
    for ind in df.index:
        query = f'''
        INSERT INTO Players(player_id,
                    player_photo,
                    player_workrate,
                    player_name,
                    player_age,
                    player_wage,
                    team_id,
                    country_id)
VALUES ({df['Player_id'][ind]}, 
        '{df['Photo'][ind]}',
        '{df['Work Rate'][ind]}' ,
        '{df['Name'][ind]}',
         {df['Age'][ind]},
        '{df['Wage'][ind]}', 
        {df['club_id'][ind]}, 
        {df['Nationality_id'][ind]});


'''
        cur.execute(query)

