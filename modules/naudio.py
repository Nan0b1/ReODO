import os
from soundfile import read, write


def convert_to_wav(dirpath, name, extension) -> str:
    if extension == ".ogg":
        data, samplerate = read(dirpath + name)
        write(os.path.join(dirpath + name + ".wav"), data, samplerate)
    return dirpath + name + ".wav"