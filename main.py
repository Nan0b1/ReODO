import modules.ntext as ntext
import modules.naudio as naudio
import modules.nrvc as nrvc



def transform_audio(in_path, out_name="outputeuuahh"):
    dirpath, name, extension = ntext.decompose(in_path)
    if not in_path.endswith(".ogg"):
        naudio.convert_to_wav(dirpath, name, extension)
        extension = ".wav"
    rvc.infer_file(dirpath, name, extension, out_name)

rvc = nrvc.NRVC()


transform_audio("C:\\Users\\USER\PycharmProjects\\re_ODO\\franck.mp3") #franck leboeuf est utilisé pour les tests
