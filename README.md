# Song_finder
Finds spotify song and it's corresponding genius page

<span>SPOTIPY_CLIENT_ID</span>  and <SPOTIPY_CLIENT_SECRET> are generated from a personal app in https://developer.spotify.com/dashboard/applications 

<genius_client_token> is from an api client from https://genius.com/api-clients

The AutoHotKey script runs the python script where it is located with "right control" + "."

Searchs genius in the format: '<song_name> <primary_artist>'

Result is considered to be correct if the artist on genius matches one listed from spotify.
Url should be opened on primary browser.
In cases where a match is not found, a genius not found page is opened.

Libraries used:
spotipy
requests
json
webbrowser
