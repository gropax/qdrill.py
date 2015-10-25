class SoundConfig:
    def __init__(self, **args):
        self.outdir = args.get('outdir', './sound')
        self.recdir = args['recdir']
        self.tmpdir = args['tmpdir']
        self.autoreplay = args.get('autoreplay', False)
