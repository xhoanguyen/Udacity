# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

print("DROP tables DONE.")
print("CREATE TABLES...")
# CREATE TABLES

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (artist_id VARCHAR PRIMARY KEY ,
                                      name VARCHAR  NOT NULL,
                                      location VARCHAR,
                                      latitude NUMERIC,
                                      longitude NUMERIC               
                                    );
""")

print("artists table created.")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (user_id varchar PRIMARY KEY,
                                      first_name VARCHAR  NOT NULL,
                                      last_name VARCHAR  NOT NULL,
                                      gender VARCHAR,
                                      level VARCHAR  NOT NULL           
                                    );
""")
print("users table created.")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY,
                                      title VARCHAR  NOT NULL,
                                      artist_id VARCHAR  NOT NULL,
                                      year INTEGER  NOT NULL,
                                      duration NUMERIC(15,5)  NOT NULL           
                                    );
""")

print("songs table created.")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (start_time TIMESTAMP PRIMARY KEY,
                                      hour INTEGER  NOT NULL,
                                      day INTEGER  NOT NULL,
                                      week INTEGER  NOT NULL,
                                      month INTEGER  NOT NULL,
                                      year INTEGER  NOT NULL,
                                      weekday VARCHAR  NOT NULL
                                    );
""")

songplay_table_create = (""" 
CREATE TABLE IF NOT EXISTS songplays (        
                                    songplay_id INTEGER ,
                                    start_time TIMESTAMP NOT NULL,
                                    user_id INTEGER NOT NULL,
                                    level VARCHAR,
                                    song_id VARCHAR,
                                    artist_id VARCHAR,
                                    session_id INTEGER NOT NULL,
                                    location VARCHAR,
                                    user_agent VARCHAR
                                    );
""")
print("songplays table created.")
print("INSERT RECORDS...")
# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);
""")
print("Inserted songplays RECORDS.")
user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s,%s,%s,%s,%s) 
    ON CONFLICT (user_id)
    DO UPDATE
        SET level      = EXCLUDED.level
""")
print("Inserted users RECORDS.")
song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s,%s,%s,%s,%s) 
ON CONFLICT (song_id) 
DO NOTHING;
""")
print("Inserted songs RECORDS.")
artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s,%s,%s,%s,%s) 
ON CONFLICT (artist_id) 
DO NOTHING;
""")
print("Inserted artists RECORDS.")

time_table_insert = ("""
INSERT INTO time (start_time , hour ,day , week , month ,year ,weekday ) VALUES (%s,%s,%s,%s,%s,%s,%s) 
ON CONFLICT  (start_time) 
DO NOTHING;
""")
print("Inserted time RECORDS.")
# FIND SONGS
song_select = ("""
SELECT songs.song_id, artists.artist_id 
FROM songs 
JOIN artists
ON songs.artist_id = artists.artist_id
WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]