# Audio word spliter

##### Install requirements:

`pip install pydub`


##### Usage:

#### split audio on silence:
  * file name
  * min_silence_len - (in ms) minimum length of a silence to be used for a split. default: 1000ms
  * silence_thresh - (in dBFS) anything quieter than this will be considered silence. default: -16dBFS
  * keep_silence - (in ms) amount of silence to leave at the beginning and end of the chunks. Keeps the sound from sounding like it is abruptly cut off. (default: 100ms)

python split_on_silence.py "mp3-file-name.mp3" 100 -12 1000



#### remove audio background

python remove_audio.py "mp3-file-name.mp3"