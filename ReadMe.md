# Spotify Downloader

## Overview

The Spotify Downloader is a Python script that allows you to download songs from Spotify playlists and convert them into MP3 format. It utilizes the Spotify API to fetch song information and the PyTube library to download YouTube videos, which are then converted into MP3 using MoviePy.

## Features

- Download songs from Spotify playlists.
- Convert downloaded YouTube videos to MP3.
- Fetch song titles and artist information from Spotify playlists.
- Search for songs on YouTube based on Spotify metadata.

## Prerequisites

Before you can use the Spotify Downloader, you need to set up the following:

1. **Spotify API Credentials**: You'll need a Spotify API client ID, client secret, and redirect URI. You can obtain these credentials by registering your application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

2. **Python Environment**: Make sure you have Python 3.x installed on your system.

## Installation

1. Clone this repository:
`https://github.com/uddin-rajaul/Spotify-playlist-downloader.git`

2. Install the required Python packages:
`pip install -r requirements.txt`

3. Create a `.env` file in the project directory and add your Spotify API credentials:
`
    SPOTIPY_CLIENT_ID=your_client_id
    SPOTIPY_CLIENT_SECRET=your_client_secret
    SPOTIPY_REDIRECT_URI=your_redirect_uri
`


## Usage

1. Run the script

2. You will be prompted to enter a Spotify playlist URL.

3. The script will extract song titles and artist information from the Spotify playlist.

4. It will search for each song on YouTube and download the corresponding videos.

5. The downloaded videos will be converted to MP3 format and saved in the `downloads` directory.

## Example

Suppose you have a Spotify playlist URL like this:
`
https://open.spotify.com/playlist/0s1OP3Igb6OVNG2RI5SVvw
`
After running the script and providing this URL, the script will:

- Fetch the song titles and artist information from the Spotify playlist.
- Search for each song on YouTube.
- Download the YouTube videos and convert them to MP3.
- Save the MP3 files in the `downloads` directory.

## Disclaimer

Please note that downloading copyrighted material without proper authorization may infringe on copyright laws in your country. Make sure to use this script responsibly and respect copyright regulations.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


