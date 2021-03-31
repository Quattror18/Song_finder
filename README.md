# Song_finder
Finds spotify song and it's corresponding genius page

The AutoHotKey script runs the python script where it is located with "right control" + "."

Searchs genius in the format: '<song_name> <primary_artist>'

Result is considered to be correct if the artist on genius matches one listed from spotify.
In cases where a match is not found, a genius not found page is opened.

Libraries used:

    spotipy
    requests
    json
    webbrowser

edit song_finder.pyw to enter your Spotify and Genius app credentials

    SPOTIPY_CLIENT_ID = 'your_client_id'
    SPOTIPY_CLIENT_SECRET = 'your_client_secret'
    genius_client_token = 'your_client_id_genius'

