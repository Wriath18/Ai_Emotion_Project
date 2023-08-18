import speech_recognition as sr
import pyttsx3
from config import api_key
import openai
openai.api_key = api_key
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET,REDIRECT_URI
import random

def speak(string, voice_id=1):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)
    engine.setProperty('rate', 190) # adjust the speaking rate
    engine.setProperty('volume', 0.9) # adjust the speaking volume
    engine.say(string)
    engine.runAndWait()

def get_playlist_name(mood_category):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=REDIRECT_URI,
                                                   scope="user-library-read playlist-read-private"))
    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        if mood_category in playlist['name'].lower():
            playlist_name = playlist['name'].lower()
            playlist_tracks = sp.playlist_tracks(playlist['id'])
            track_uris = [track['track']['uri'] for track in playlist_tracks['items']]
            chosen_track_uri = random.choice(track_uris)
            chosen_url = (sp.track(chosen_track_uri))['external_urls']['spotify']
            return f"{playlist['name']} - {playlist['external_urls']['spotify']}\nSong Uri : {chosen_track_uri}\nSong url : {chosen_url}"
            
    return "Sorry, no matching playlist found."

    