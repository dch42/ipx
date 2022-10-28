#!/usr/bin/env python3
"""Extract and rename iPod audio data to local drive"""

import sys
import argparse
import os
import logging
from pathlib import Path
from tinytag import TinyTag
from tqdm import tqdm


LOG = "./ipx.log"
home = os.path.expanduser("~")
extensions = [".mp3", ".m4a", ".mp4", ".m4b", ".aac", ".aiff"]
various = ["VA", "Various", "Various Artists"]

logging.basicConfig(
    filename=LOG,
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


def parse_args(args):
    """Define and parse args"""
    parser = argparse.ArgumentParser(
        description="Extract and rename iPod audio data to local drive"
    )
    parser.add_argument("-i", type=str, required=True, help="path to mounted iPod")
    parser.add_argument(
        "-o",
        type=str,
        help="path to local directory for extraction (default: ~/iPod/Music)",
    )
    return parser.parse_args()


def cleanse(val):
    """Sanitize tag strings for dir/filenames"""
    val = val.replace("/", "").replace(":", "-").replace("?", "")
    return val


def pad_zeroes(track):
    """Pad zeros on track numbers < 10"""
    if track[0].isdigit() and track[0] != "0":
        if int(track) in range(0, 10):
            padded = f"0{track}"
            return padded
    return track


def iter_files(ipod_path):
    """Walk iPod dir path and pass files to parser"""
    for root, dirs, files in os.walk(ipod_path, topdown=False):
        for filename in tqdm(
            files, colour="green", desc=f"{os.path.basename(root)}..."
        ):
            if filename.endswith(tuple(extensions)) and not filename.startswith("._"):
                audio_file = os.path.join(root, filename)
                ext = Path(audio_file).suffix
                try:
                    tags = TinyTag.get(f"{audio_file}")
                    extract_file(audio_file, tags, ext)
                except Exception as error:
                    msg = f"Parsing `{audio_file}` failed: {error}"
                    unparsed_dump = (
                        f"{str(args.o)}" if args.o else f"{home}/iPod/Unknown_Tags/"
                    )
                    os.system(f"cp {audio_file} {unparsed_dump}")
                    tqdm.write(msg)
                    


def extract_file(file, tags, ext):
    """Make directory for audio files, copy files into proper dirs, rename files"""
    artist = "Various" if tags.albumartist in various else cleanse(tags.artist)
    album = cleanse(tags.album)
    album_path = (
        f"{str(args.o)}/{artist}/{album}/"
        if args.o
        else f"{home}/iPod/Music/{artist}/{album}/"
    )
    new_filename = f"{pad_zeroes(tags.track)} - {cleanse(tags.artist)} - {cleanse(tags.title)}{ext}"
    try:
        os.makedirs(f"{album_path}", exist_ok=True)
        os.system(f'cp "{file}" "{album_path}"')
        os.system(
            f'mv "{album_path}/{os.path.split(file)[1]}" "{album_path}/{new_filename}"'
        )
        msg = f"Copied {file} to {album_path}{new_filename}"
        tqdm.write(msg)
        logging.info(msg)
    except Exception as error:
        msg = f"Copy {file} failed: {error}"
        tqdm.write(msg)
        logging.info(msg)


if __name__ == "__main__":
    
    args = parse_args(sys.argv[:1])
    ipod_path = args.i
    logging.info(f"[START] Script traversing {ipod_path}...")
    iter_files(ipod_path)
    logging.info(f"[FINISH] Run complete.\n")

