import spotipy
from spotipy import oauth2
import spotipy.util as util
import pprint
import requests
import json
import webbrowser

PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID = ''
SPOTIPY_CLIENT_SECRET = ''
genius_client_token = ''
REDIRECT_URI = 'http://localhost:8080'
SCOPE = 'user-read-playback-state'
CACHE = '.spotipyoauthcache'


#Removes the remaster label part of the title
def remaster_remove(song_name):
    song_name = song_name.lower()

    str1 = 'remaster'

    if song_name.find(str1) != -1:
        
        re_index = song_name.find(str1)
        song_name = song_name[0:re_index-2]
        print(song_name[0:len(song_name)-5])
        str2 = song_name[-3:]
        print(str2)
        if str2.isdigit() == True:
            song_name = song_name[0:len(song_name)-5]

    return song_name

#replaces 'and' with '&'
#because Blur's Girls and boys on spotify is Girls & Boys on genius
def and_replace(song_name):
    new_name = song_name.replace('and', '&')
    
    return(new_name)

#identifies the currently playing song and artist(s)
def spotify():

    token = util.prompt_for_user_token('vwb9gnnnmetryij9oyqepe541',
                               SCOPE,
                               client_id= SPOTIPY_CLIENT_ID,
                               client_secret= SPOTIPY_CLIENT_SECRET,
                               redirect_uri= REDIRECT_URI)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_playing_track()

        if results:
        
            item = results['item']

            album_type = item['album']['album_type']
            album_name = item['album']['name']
            album_date = item['album']['release_date']

            song_name = item['name']

            song_name = remaster_remove(song_name)

            song_id = item['id']

            artist_info = item['artists']

            artists = []
            for artist in artist_info:
                artist_name = artist['name']
                artist_id = artist['id']
                artists.append(artist_name)

            stop = False
            i = 0
            while stop == False:
                
                genius_search_query = song_name + " " + artists[0]
                
                (find, url) = genius(genius_search_query,artists)

                if find == False and i != 1:
                    song_name = and_replace(song_name)
                    i += 1
                else:
                    stop = True
                    webbrowser.open(url)



    else:
        print("Can't get token for", username)

#does the genius api search
def genius(query, artists):

    
    genius_base_url = 'https://api.genius.com'

    request_url = genius_base_url + '/search/'

    params = {
        'q' : query}


    token = 'Bearer {}'.format(genius_client_token)
    headers = {'Authorization' : token}

    r = requests.get(request_url, params=params, headers=headers)
    r=r.json()

    song_url = 'https://genius.com/not_found_page'
    
    for hit in r['response']['hits']:
        song_name = hit['result']['title']
        primary_artist_name = hit['result']['primary_artist']['name']
        

        same_artist = False
        for name in artists:
            if name == primary_artist_name:
                song_url = hit['result']['url']
                same_artist = True

        if same_artist == True:           
            break 
    
    return(same_artist,song_url)
    

spotify()
