import modules.ntext as ntext
import modules.naudio as naudio
import modules.nrvc as nrvc


#print(ntext.decompose("https://musicyoutubecom/watch?v=DDT_kJJuw8E&list=RDAOCqTDigjO19bXmF1fglzCAw.ahh"))


def transform_audio(in_path, out_name="outputeuuahh"):
    dirpath, name, extension = ntext.decompose(in_path)
    if not in_path.endswith(".ogg"):
        naudio.convert_to_wav(dirpath, name, extension)
        extension = ".wav"
    rvc.infer_file(dirpath, name, extension, out_name)

rvc = nrvc.NRVC()

'''
rvc = RVCInference(device="cuda:0")
rvc.load_model("models/villager/villager.pth", index_path="models/villager/added_IVF81_Flat_nprobe_1_v2.index")
#rvc.set_params(index_rate="0.5", filter_radius=0.2, f0method="harvest", resample_sr=48000, rms_mix_rate=0.2, protect=0.1, f0up_key=0)
rvc.set_params(filter_radius=0.2, f0method="harvest", resample_sr=8000, rms_mix_rate=0.2, protect=0.2, f0up_key=0)
'''

transform_audio("C:\\Users\\USER\PycharmProjects\\re_ODO\\franck.mp3")
#rvc.infer_file("C:\\Users\\USER\PycharmProjects\\re_ODO\\franck.wav", "output.wav")
