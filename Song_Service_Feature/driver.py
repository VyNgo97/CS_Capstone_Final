import sqlite3

def db_connect(dbName):
    # connect to database
    conn = sqlite3.connect(dbName, isolation_level=None)

    # return cursor object
    return conn, conn.cursor()

def get_mood_id(cursor, mood_alias):
    # Returns the mood ID for a given mood Name
    data = (mood_alias,)
    cursor.execute(
        '''
        SELECT mood_id
        FROM Moods
        WHERE mood_alias = ?
        ;
        '''
        , data
    )
    return cursor.fetchone()[0]

def get_song_title(cursor, song_id):
    # Returns the song name for a given song ID
    data = (song_id,)
    cursor.execute(
        '''
        SELECT song_title
        FROM Songs
        WHERE song_id = ?
        ;
        '''
        , data
    )
    return cursor.fetchone()[0]

def get_song_url(cursor, song_id):
    # Returns the song url for a given song ID
    data = (song_id,)
    cursor.execute(
        '''
        SELECT yt_url
        FROM Songs
        WHERE song_id = ?
        ;
        '''
        , data
    )
    return cursor.fetchone()[0]

def get_color_alias(cursor, color_id):
    # returns the name of a color for a given ID
    data = (color_id,)
    cursor.execute(
        '''
        SELECT color_alias
        FROM Colors
        WHERE rgb_id = ?
        ;
        '''
        , data
    )
    return cursor.fetchone()[0]

def get_color_match(cursor, mood_id):
    # REturns the first color associated with a given Mood
    data = (mood_id,)
    cursor.execute(
        '''
        SELECT color_1
        FROM Moods
        WHERE mood_id = ?
        ;
        '''
        , data
    )
    return cursor.fetchone()[0]

def get_song_match(cursor, mood_id):
    # REturns the first song associated with a given Mood
    data = (mood_id,)
    cursor.execute(
        '''
        SELECT song_1
        FROM Moods
        WHERE mood_id = ?
        ;
        '''
        , data
    )
    return cursor.fetchone()[0]