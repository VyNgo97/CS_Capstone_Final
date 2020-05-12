import driver
# TODO: Add some error handling in here (maybe)

def main():
    # Connect to the database
    # If database is not in same folder as this script
    # be sure to include the relative path
    conn, c = driver.db_connect('IOT.db')

    # Examples:
    play_song_for_mood(c, 'Happy')
    play_song_for_mood(c, 'Sad')

    print(get_color(c, 'Happy'))
    print(get_color(c, 'Sad'))

def play_song(url):
    # TODO: Find a way to play the song via Youtube or something
    print(url) # Youtube API go brrrrrr(url)
    
    return

def play_song_for_mood(cursor, mood):

    # Get the ID for the associated mood
    mood_id = driver.get_mood_id(cursor, mood)
    
    # Get the ID for the first song associated with the mood
    song_id = driver.get_song_match(cursor, mood_id)

    # Get the URL of the song
    song_title = driver.get_song_title(cursor, song_id)
    song_url = driver.get_song_url(cursor, song_id)

    # Play the song on Youtube
    print('Playing %s on Youtube' %song_title)
    play_song(song_url)

    return 

def get_color(cursor, mood):

    # Get the ID for the associated mood
    mood_id = driver.get_mood_id(cursor, mood)

    # Get he ID fro the first color associated with the mood
    color_id = driver.get_color_match(cursor, mood_id)

    # Return the name of the color that goes with that ID
    return driver.get_color_alias(cursor, color_id)

if __name__=="__main__":
    main()