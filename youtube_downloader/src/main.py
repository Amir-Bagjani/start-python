from pytube import YouTube
from pathlib import Path
from typing import Any
import time
from tqdm import tqdm
import argparse


class YoutubeDownloader:
    """
    Download YouTube videos using pytube.

    The downloader supports downloading either the highest available
    progressive MP4 stream or a user-specified resolution.

    Attributes:
        url:
            The YouTube video URL.

        output_path:
            Directory where downloaded videos are saved.
            Defaults to the current working directory.

        quality:
            Desired video resolution (e.g. "720p", "1080p").
            If omitted or set to ``None``, the highest available
            progressive MP4 stream is downloaded.

        yt:
            The underlying ``pytube.YouTube`` object.
    """

    def __init__(
        self, url: str, output_path: str | None = None, quality: str | None = None
    ):
        """
        Initialize a YouTube downloader.

        Args:
            url:
                The YouTube video URL.

            output_path:
                Directory where the downloaded video will be saved.
                Defaults to the current working directory.

            quality:
                Desired video resolution such as ``720p`` or ``1080p``.
                If omitted, the highest available quality is downloaded.
        """
        self.url = url
        self.output_path = output_path or Path.cwd()
        self.quality = quality or "highest"
        self.yt = YouTube(
            self.url,
            on_progress_callback=self.on_progress,
            on_complete_callback=self.on_complete,
        )

    def on_complete(self, stream: Any, file_path: str | None):
        """
        Callback executed when a download finishes.

        Args:
            stream:
                The downloaded pytube stream.

            file_path:
                Path to the downloaded file.
        """
        print(f"\nDownload completed, File saved to: {file_path}")

    def on_progress(self, stream: Any, chunk: bytes, bytes_remaining: int):
        """
        Callback executed periodically while downloading.

        Displays the download progress, downloaded size,
        and total file size.

        Args:
            stream:
                The stream currently being downloaded.

            chunk:
                The latest downloaded chunk.

            bytes_remaining:
                Number of bytes remaining to download.
        """
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining

        self.pbar.update(bytes_downloaded - self.pbar.n)

        # print(
        #     f"\r{'downloading...'}:<15"
        #     f"{(100*(total_size-bytes_remaining)/total_size):>3.0f}%"
        #     f"| {bytes_downloaded/1024/1024:>5.1f}MB"
        #     f" of {total_size/1024/1024:>5.1f}MB"
        #     f"| {'finished':<10}",
        #     end="",
        # )

    def download(self):
        """
        Download the video.

        If ``quality`` is ``"highest"``, the highest available
        progressive MP4 stream is downloaded. Otherwise, the downloader
        attempts to download the specified resolution.

        Returns:
            None
        """
        try:

            if self.quality == "highest":
                stream = self.yt.streams.filter(
                    progressive=True, file_extension="mp4"
                ).get_highest_resolution()
            else:
                stream = self.yt.streams.filter(
                    progressive=True, file_extension="mp4", res=self.quality
                ).first()

            if stream is not None:
                stream.download(output_path=str(self.output_path))
                self.pbar = tqdm(
                    desc="downloading...",
                    total=stream.filesize,
                    unit="B",
                    unit_scale=True,
                )
        except Exception as e:
            print(e)
            exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Youtube Downloader")
    parser.add_argument("-u", "--url", help="Youtube video URL")
    parser.add_argument("-q", "--quality", help="Video quality", default="highest")
    parser.add_argument("-o", "--output", help="Path of downloaded file", default=None)

    args = parser.parse_args()

    YoutubeDownloader(
        url=args.url, quality=args.quality, output_path=args.output
    ).download()
