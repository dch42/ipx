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

The iPod stores audio files in a collection of subdirectories of the `iPod_Control/Music/` directory, incrementing from `F00`. The files themselves are named as strings of four uppercase alphabetical characters. 

Example structure:
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

`ipx` walks these subdirectories, passing discovered audio files to [TinyTag](https://github.com/devsnd/tinytag) for parsing.  

If parsing is successful, files are copied to a default location of `$HOME/iPod/Music/$artist/$album/` [^1] and renamed following a `$tracknum - $artist - $title.ext` convention.

`ipx` attempts to suss out compilation albums, and will place them in a `/Various/` subdirectory.

If unable to parse a file, the file will be copied to `/Unknown Tags/` subdirectory for manual evaluation.

Sorted local directory structure looks something like this:

~~~
/Users/user/iPod/Music
├──  Artist Name
│   ├── Album Name 
│   │   ├── 01 -  Artist Name - Track Title.m4a
│   │   └── 02 -  Artist Name - Track Title.m4a
│   └── Album Name 
│       ├── 01 -  Artist Name - Track Title.m4a
│       └── 02 -  Artist Name - Track Title.m4a
├── Various
│   ├── Compilation Name
│   │   ├── 01 - Artist Name - Track Title.m4a
│   │   ├── 02 - Artist Name - Track Title.m4a
│   │   ├── 03 - Artist Name - Track Title.m4a
|   |    ...
~~~

[^1]: This path can be overridden by specifying a custom path with `-o`.