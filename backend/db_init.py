import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as db_file:
    connection.executescript(db_file.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO waveMaps (map, description, spu) VALUES (?,?,?)",
                ('Hagglefish Market', 'Incredibly good spots in mid, with decent utility both on offense and defense. Better on tower control since you can throw wave on the tower.', 1.1)
              )
cursor.execute("INSERT INTO waveMaps (map, description, spu) VALUES (?,?,?)",
                ('Makomart', 'The entire middle of the map is a wave breaker spot, but there are also good spots on the stacks for defense and offense.', 0.0)
              )
cursor.execute("INSERT INTO waveMaps (map, description, spu) VALUES (?,?,?)",
                ('Flounder Heights', 'You can\'t mess up throwing wave on this map, but try to aim for higher locations for better coverage.', 0.1)
              )

cursor.execute("INSERT INTO waveMaps (map, description, spu) VALUES (?,?,?)",
               ('Um\'ami Ruins', 'Very good spots if you know where to look for them. Nothing spectacular, but wave is good in all areas.', 1.1)
              )

connection.commit()
connection.close()