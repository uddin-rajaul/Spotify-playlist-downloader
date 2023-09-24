import spotipy
from spotipy.oauth2 import SpotifyOAuth
from youtubesearchpython import VideosSearch
from pytube import YouTube
from moviepy.editor import VideoFileClip
import time  # Import the time module
import os

from decouple import config

def get_api_credentials():
    """Fetches API credentials (client ID, client secret, and redirect URI) from a .env file.

    Returns:
        tuple: A tuple containing client ID, client secret, and redirect URI.
    """
    client_id = config('SPOTIPY_CLIENT_ID')
    client_secret = config('SPOTIPY_CLIENT_SECRET')
    redirect_uri = config('SPOTIPY_REDIRECT_URI')
    return client_id, client_secret, redirect_uri

def download_video_and_convert_to_mp3(video_url, output_directory="."):
    """Downloads a YouTube video in MP4 format and converts it to MP3.

    Args:
        video_url (str): The URL of the YouTube video to download.
        output_directory (str): The directory where the MP3 file will be saved. Default is the current directory.
    """
    yt = YouTube(video_url)
    stream = yt.streams.filter(file_extension="mp4", progressive=True).first()

    if stream:
        mp4_file_path = stream.download(output_path=output_directory)
        mp4_file_name = mp4_file_path.split(os.path.sep)[-1]
        
        # Convert MP4 to MP3 using moviepy
        mp4_clip = VideoFileClip(mp4_file_path)
        mp3_file_name = mp4_file_name.replace(".mp4", ".mp3")
        mp3_file_path = os.path.join(output_directory, mp3_file_name)
        mp4_clip.audio.write_audiofile(mp3_file_path)

        # Wait for moviepy to finish processing
        mp4_clip.close()

        # Remove the downloaded MP4 file
        os.remove(mp4_file_path)

        return mp3_file_path
    else:
        return None
    
def extract_first_youtube_search_link(search_query):
    """Extracts the first YouTube search result link for a given search query.

    Args:
        search_query (str): The search query to use on YouTube.

    Returns:
        str: The URL of the first search result, or None if no results are found.
    """
    try:
        # Perform the YouTube search
        videos_search = VideosSearch(search_query, limit=1)
        results = videos_search.result()

        # Extract the URL of the first search result
        if results['result']:
            first_result = results['result'][0]
            return first_result['link']
        else:
            print("No results found on YouTube.")
            return None

    except Exception as e:
        print(f"Error extracting YouTube search link: {e}")
        return None

def extract_spotify_playlist_songs(playlist_url, client_id, client_secret, redirect_uri):
    """Extracts and prints the song titles from a Spotify playlist.

    Args:
        playlist_url (str): The URL of the Spotify playlist.
        client_id (str): Your Spotify API client ID.
        client_secret (str): Your Spotify API client secret.
        redirect_uri (str): Your Spotify API redirect URI.
    """

    song_titles = []
    # Initialize the Spotify API client
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="playlist-read-private",  # Ensure the necessary scope is set
    ))
    try:
        # Extract the playlist ID from the Spotify URL
        playlist_id = playlist_url.split('/')[-1]

        # Get the playlist details
        playlist = sp.playlist(playlist_id)

        # Extract and append the song titles to the list
        for track in playlist['tracks']['items']:
            song_title = track['track']['name']
            # song_titles.append(song_title)
            artists = [artist['name'] for artist in track['track']['artists']]
            artist_info = ', '.join(artists)
            song_titles.append(f"{song_title} - {artist_info}")

        return song_titles  # Return the list of song titles

    except Exception as e:
        print(f"Error extracting playlist songs: {e}")
        return []



if __name__ == "__main__":
    client_id, client_secret, redirect_uri = get_api_credentials()

    output_directory = "C:/Users/uddin/Downloads/Music/IU"  # Replace with your desired directory
    playlist_url = input("Enter playlist URL: ")
    song_titles = extract_spotify_playlist_songs(playlist_url,client_id, client_secret, redirect_uri)
    
    # Now you have a list of song titles that you can iterate over or process further
    for song_title in song_titles:
        try:
            first_link = extract_first_youtube_search_link(song_title)
            if first_link:
                download_video_and_convert_to_mp3(first_link, output_directory)
            else:
                print("No link found.")
        except Exception as e:
            print(f"Error processing song '{song_title}': {str(e)}")
