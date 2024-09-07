import argparse
import logging
from downloader import YouTubeDownloader

def main():
    parser = argparse.ArgumentParser(description="YouTube Downloader CLI")
    parser.add_argument('url', type=str, help='YouTube video URL to download')
    parser.add_argument('--format', type=str, choices=['video', 'audio'], default='video', help='Download format (default: video)')
    parser.add_argument('--path', type=str, default='./downloads', help='Output directory for downloaded files')

    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        downloader = YouTubeDownloader(args.url, args.path, args.format)
        downloader.fetch_video()
        downloader.download()
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
