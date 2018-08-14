from pydub import AudioSegment
from pydub.silence import split_on_silence

import sys

def split(file_namem, min_silence_len=1000, silence_thresh=-16, keep_silence=100):
    #file_name = '2018-06-26-art-area-sodobnost-sodobne-umetnosti-drugič.mp3'


    sound = AudioSegment.from_mp3(file_name)[100000:120000]
    chunks = split_on_silence(sound, 
        # must be silent for at least half a second
        min_silence_len=min_silence_len,

        # consider it silent if quieter than -16 dBFS
        silence_thresh=silence_thresh,
        keep_silence=keep_silence,
    )

    # save chunks
    for i, chunk in enumerate(chunks):
        chunk.export('out/chunk{0}.mp3'.format(i), format='mp3')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        try:
            silence = sys.argv[2]
            trashold = sys.argv[3]
            keep_silence = sys.argv[4]
            split(file_name, silence, trashold, keep_silence)
        except:
            split(file_name)
    else:
        print("add file name as 1st argument")