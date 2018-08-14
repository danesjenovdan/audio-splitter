from pydub import AudioSegment
from pydub.playback import play

import sys


def split(file_name):
    # read in audio file and get the two mono tracks
    sound_stereo = AudioSegment.from_file(file_name)[100000:120000]

    sound_monoL = sound_stereo.split_to_mono()[0]
    sound_monoR = sound_stereo.split_to_mono()[1]

    #play(sound_stereo)

    # Invert phase of the Right audio file
    sound_monoR_inv = sound_monoR.invert_phase()

    # Merge two L and R_inv files, this cancels out the centers
    sound_CentersOut = sound_monoL.overlay(sound_monoR_inv)

    inverse_music = sound_CentersOut.invert_phase()

    voice = sound_stereo.overlay(sound_CentersOut)

    # Export merged audio file
    fh = inverse_music.export('music.mp3', format="mp3")
    fh = voice.export('wo-audio.mp3', format="mp3")
    fh = sound_stereo.export('org_cut.mp3', format="mp3")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        split(file_name)
    else:
        print("add file name as 1st argument")
