# ipx

`ipx` is a quick script to extract audio files from an iPod and sanely organize the files locally. 

## Usage

~~~
usage: ipx.py [-h] -i I [-o O]

Extract and rename iPod audio data to local drive

options:
  -h, --help  show this help message and exit
  -i I        path to mounted iPod
  -o O        path to local directory for extraction (default:
              ~/iPod/Music)
~~~

Point the script to a mounted iPod's music directory (`${ipod}/iPod_Control/Music/`) with the `-i` option.

By default, audio files will be extracted to an `iPod/Music/` directory in `$HOME`. If desired, pass an alternate path with `-o`.

### How It Works

The iPod stores audio files in a collection of subdirectories of the `iPod_Control/Music/` directory, incrementing upwards from `F00`. The files themselves are named as strings of four uppercase alphabetical characters. 

Example:
~~~
/Volumes/IPOD/iPod_Control/Music/
├── F00
│   ├── AABH.m4a
│   ├── AAHD.m4a
│   ├── AAMX.m4a
...
├── F01
│   ├── AAQW.m4a
│   ├── ACZR.m4a
│   ├── AHCN.m4a
...
├── F02
...
~~~