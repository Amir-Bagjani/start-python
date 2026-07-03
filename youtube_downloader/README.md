# YouTube Downloader

A simple Python wrapper around `pytube` for downloading YouTube videos with progress updates.

## Features

- Download the highest available MP4 quality.
- Download a specific resolution (e.g. `720p`, `480p`).
- Real-time download progress.
- Download completion notification.
- Uses the current working directory by default.

## Requirements

- Python 3.10+
- pytube

Install dependencies:

```bash
pip install pytube
```

## Usage

### Download the highest quality

```python
from youtube_downloader import YoutubeDownloader

YoutubeDownloader(
    url="https://www.youtube.com/watch?v=VIDEO_ID"
).download()
```

### Download a specific quality

```python
YoutubeDownloader(
    url="https://www.youtube.com/watch?v=VIDEO_ID",
    quality="720p"
).download()
```

### Specify an output directory

```python
YoutubeDownloader(
    url="https://www.youtube.com/watch?v=VIDEO_ID",
    output_path="./downloads"
).download()
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `url` | `str` | YouTube video URL. |
| `output_path` | `str \| None` | Directory where the video will be saved. Defaults to the current working directory. |
| `quality` | `str \| None` | Video resolution such as `1080p`, `720p`, `480p`. If omitted, the highest available quality is downloaded. |

## Example

```python
from youtube_downloader import YoutubeDownloader

downloader = YoutubeDownloader(
    url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    output_path="downloads",
    quality="720p"
)

downloader.download()
```

## Output

```
downloading...  65% | 18.2MB of 28.0MB | finished
Download completed, File saved to: downloads/video.mp4
```

## Notes

- Only progressive MP4 streams are downloaded.
- If the requested resolution is unavailable, no download will occur.
- Some YouTube videos may not be downloadable depending on YouTube restrictions or changes to the platform.