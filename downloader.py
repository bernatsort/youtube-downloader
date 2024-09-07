import os
from pytubefix import YouTube
import logging
from utils import validate_url

class YouTubeDownloader:
    def __init__(self, url, download_path='./downloads', format='video'):
        self.url = url
        self.format = format
        self.download_path = download_path
        self.video = None

    def fetch_video(self):
        if not validate_url(self.url):
            raise ValueError(f"Invalid URL: {self.url}")
        self.video = YouTube(self.url)
        logging.info(f"Fetched video details: {self.video.title}")

    def download(self):
        if not self.video:
            raise RuntimeError("Video not fetched. Run fetch_video() first.")
        
        try:
            logging.info(f"Available streams for {self.video.title}:")
            for stream in self.video.streams:
                logging.info(f"{stream}")
            
            if self.format == 'audio':
                stream = self.video.streams.filter(only_audio=True).first()
            else:
                # Attempt to fetch a progressive stream (contains both video and audio)
                stream = self.video.streams.filter(progressive=True).first()

            if stream:
                logging.info(f"Starting download for: {self.video.title}")
                output_path = stream.download(output_path=self.download_path)
                logging.info(f"Download completed. Saved to {output_path}")
            else:
                logging.error("No suitable stream found for download.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

