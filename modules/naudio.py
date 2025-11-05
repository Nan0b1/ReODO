from soundfile import read, write


def convert_to_wav(dirpath:str, name:str, extension:str, outextension:str, outdirpath:str="", outname:str="") -> str:
    """
    :param dirpath: The directory path of the input audio file
    :param name: The name of the input audio file without the extension
    :param extension: The extension of the input audio file with a dot
    :param outdirpath: The directory path of the output audio file
    :param outname: The name of the output audio file without the extension
    :param outextension: The extension of the output audio file with a dot
    :return: The path of the output audio file
    """

    if outname=="":
        outname=name
    if outdirpath=="":
        outdirpath=dirpath

    if extension != outextension:
        data, samplerate = read(f"{dirpath}\\{name}{extension}")
        write(f"{outdirpath}\\{outname}{outextension}", data, samplerate)

    return f"{outdirpath}\\{outname}{outextension}"
