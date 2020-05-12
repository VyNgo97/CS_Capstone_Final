--Create songs table
CREATE TABLE Songs (
    song_id INTEGER
    ,song_title varchar(100) NOT NULL
    ,song_artist varchar(100) NOT NULL
    ,genre varchar(30)
    ,yt_url varchar(500)
    ,PRIMARY KEY (song_id ASC)
);

--Create colors table
CREATE TABLE Colors (
    rgb_id VARCHAR(9)
    ,color_alias varchar(50) NOT NULL
    ,hex_id varchar(6)
    ,PRIMARY KEY (rgb_id)
);

-- Create moods table
CREATE TABLE Moods (
    mood_id INTEGER
    , mood_alias varchar(50) NOT NULL
    , color_1 VARCHAR(9)
    , color_2 VARCHAR(9)
    , color_3 VARCHAR(9)
    , song_1 INTEGER
    , song_2 INTEGER
    , song_3 INTEGER
    , PRIMARY KEY (mood_id ASC)
    , FOREIGN KEY (color_1) REFERENCES Colors(rgb_id)
    , FOREIGN KEY (color_2) REFERENCES Colors(rgb_id)
    , FOREIGN KEY (color_3) REFERENCES Colors(rgb_id)
    , FOREIGN KEY (song_1) REFERENCES Songs(song_id)
    , FOREIGN KEY (song_2) REFERENCES Songs(song_id)
    , FOREIGN KEY (song_3) REFERENCES Songs(song_id)
);

INSERT INTO Songs (song_title, song_artist, genre, yt_url)
VALUES
      ('Henny in the Hamptons', 'Bren Joy', 'Hip-Hop', 'https://www.youtube.com/watch?v=T2NLoljpzkA')
    , ('Banana Clip', 'Miguel', 'Hip-Hop', 'https://www.youtube.com/watch?v=rqdeMyMl_pU')
    , ('Boyfriend', 'Coin', 'Alternative', 'https://www.youtube.com/watch?v=wkjSpojVgNg')
    , ('Con te Partiro', 'Andrea Bocelli', 'Opera', 'https://www.youtube.com/watch?v=Wdx5nGphnAI')
    , ('Frolic', 'Luciano Michelini', 'Instrumental', 'https://www.youtube.com/watch?v=6MYAGyZlBY0')
    , ('Captivity','Atlasaria','Hard Rock', 'https://www.youtube.com/watch?v=M8P2MITa7iw')
;

INSERT INTO Colors (rgb_id, color_alias, hex_id)
VALUES
      ('250000000', 'Red','FF0000')
    , ('000250000', 'Green','00FF00')
    , ('000000250', 'Blue','0000FF')
    , ('104030150', 'Nice purple', '681e96')
    , ('120219255', 'Baby blue', '78dbdff')
    , ('255259005', 'Mango', 'ff9f05')
;

INSERT INTO Moods (mood_alias, song_1, color_1)
VALUES
      ('Happy', '1', '104030150')
    , ('Sad', '2', '120219255')
    , ('Neutral', '3', '000250000')
    , ('Surprised', '5', '000000250')
    , ('Angry', '6', '250000000')
    , ('Disgust', '4', '255259005')
;