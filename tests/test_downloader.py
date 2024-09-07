import pytest
from ..downloader import YouTubeDownloader

def test_invalid_url():
    invalid_url = "https://invalidurl.com"
    downloader = YouTubeDownloader(invalid_url)
    with pytest.raises(ValueError):
        downloader.fetch_video()

def test_valid_video_download():
    valid_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    downloader = YouTubeDownloader(valid_url)
    downloader.fetch_video()
    assert downloader.video is not None
