import requests
import IOT_Interactions as inter
from facial_recognition import live_feed as feed
    
mood = feed.captureMood()




def updateLed (mood):

    c = inter.main()
    grb = inter.get_color(c, mood)
    # inter.play_song_for_mood(c, mood)

    nodeMCU = 'http://192.168.0.7'
    color = {'colors': grb}

    sendColor = requests.post(nodeMCU, data=color)

    print(sendColor.text)


updateLed(mood)
