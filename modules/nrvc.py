from rvc_python.infer import RVCInference


class NRVC():
    def __init__(self):
        self.rvc = RVCInference(device="cuda:0")
        self.rvc.load_model("models/villager/villager.pth", index_path="models/villager/added_IVF81_Flat_nprobe_1_v2.index")
        #self.rvc.set_params(index_rate="0.5", filter_radius=0.2, f0method="harvest", resample_sr=48000, rms_mix_rate=0.2, protect=0.1, f0up_key=0)
        self.rvc.set_params(filter_radius=0.2, f0method="harvest", resample_sr=8000, rms_mix_rate=0.2, protect=0.2, f0up_key=0)

    def infer_file(self, dirpath, name, extension, outname):
        self.rvc.infer_file(dirpath + name + extension, dirpath + outname + extension)