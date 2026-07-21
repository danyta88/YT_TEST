import os
import requests
import json
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLER = "MrBeast"
maxResults = 50

if not API_KEY:
    raise ValueError("API_KEY not found! Please check your .env file and its location.")

def get_playlist_id():
    
    try:
        url =  f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLER}&key={API_KEY}'

        response = requests.get(url)

        response.raise_for_status()
        #idPlaylist = "UUX6OQ3DkcsbYNE6H8uQQuVA"

        data = response.json()

        print(json.dumps(data, indent=4))

        channelItems = data["items"][0]
        channel_playlistId = channelItems["contentDetails"]["relatedPlaylists"]["uploads"]

        print(channel_playlistId)
        return channel_playlistId

    except requests.exceptions.RequestException as e:
        raise e
    

def get_video_ids():
    video_ids = []
    pageToken = None

    base_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={maxResults}&playlistId={playlist_id}&key={API_KEY}"

    try:
    
    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    playlist_id = get_playlist_id()