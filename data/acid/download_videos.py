from __future__ import unicode_literals
import csv
import pdb
import os

# environment.
# https://github.com/coletdjnz/yt-dlp-youtube-oauth2?tab=readme-ov-file
# pip install yt_dlp
# python -m pip install -U https://github.com/coletdjnz/yt-dlp-youtube-oauth2/archive/refs/heads/master.zip

import yt_dlp

def download_youtube_video(youtube_url, vid, download_dir='.'):
    # Set up options for yt-dlp
    video_path = f"{download_dir}/{vid}.mp4"
    if os.path.exists(video_path):
        print(f'{video_path} exists')
        return
    ydl_opts = {
        'outtmpl': video_path,  # Output format: save in download_dir with video title and proper extension
        'format': 'best',  # Download the best available quality
        'username': 'oauth2',
        'password': '',
        'verbose': False
    }
    # Use yt-dlp to download the video
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=True)  # Extract and download
            # video_title = info_dict.get('title', None)
            # video_ext = info_dict.get('ext', None)
            # video_path = f"{download_dir}/{vid}.{video_ext}"
        print(f'{video_path} download successfully')
    except:
        print(f'{video_path} download failed')
        return

camera_src = '/data/ACID/acid/train/'
# ['acid/train/', 'acid/validation/', 'acid/test/', 'acid_large/']
download_directory = '/data/ACID/acid_video/train_video'
os.makedirs(download_directory, exist_ok=True)
for txt in sorted(os.listdir(camera_src)):
    txt_path = os.path.join(camera_src, txt)
    with open(txt_path, 'r') as f:
        youtube_link = f.readline().strip()
    if 'https://www.youtube.com/' in youtube_link:
        download_youtube_video(youtube_link, txt[:-4], download_directory)
    