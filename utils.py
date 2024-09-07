import re

def validate_url(url):
    # Simple regex validation for a YouTube URL
    youtube_regex = r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$'
    return re.match(youtube_regex, url) is not None
