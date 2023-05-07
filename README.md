# Media Filename Manager

## Abstract
This small python script is designed to rename multiple media files (.mp4 or .mkv) into specific format
that could easily be identified in Infuse media player.

## Structure
There are two versions of python scripts available. One dedicated to MacOS, the other supports WindowsOS.

`main.py`

run this python file in terminal in the following format
<pre> $sudo main.py folder_address media_type name season_number/year episode mode </pre>
* folder_address: the absolute address of mediafile
* media_type: type `m` for movie, `t` for TV series
* name: names you want to change your files into
* season_number/year: enter season number for TV series or publish year for movie
* episode: starting episode number
* mode: `0` means a dry run, `1` means actual renaming. It is highly recommended that a dry run will be performed before the actual renaming process occurred

## Reference && Citations
