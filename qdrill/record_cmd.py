class RecordCmd:
    def __init__(self, config, rec):
        self.config = config
        self.recording = rec

    def record(self):
        self.recording.start()
        sys.stdout.write("recording... [enter to stop] ")
        raw_input()
        self.recording.stop()
        print "recorded %.2fs" % self.recording.duration()

    def execute(self):
        sys.stdout.write("\033[92m%s\033[0m\t" % self.recordings.text)

        sys.stdout.write("  [Rsq] ")
        while True:
            ans = raw_input() or "r"
            if ans == 'q':
                print "Exiting..."
                exit(2)
            elif ans == 's':
                break
            elif ans == 'r':
                accepted = False
                while not accepted:
                    self.record()

                    if self.config.autoreplay:
                        self.recording.play()
                        default = 'y'
                        sys.stdout.write("accept ? [Ynp] ")
                        while True:
                            ans = raw_input() or default
                            if ans == 'y':
                                accepted = True
                                break
                            elif ans == 'n':
                                break
                            elif ans == 'p':
                                self.recording.play()
                                default = 'p'
                                sys.stdout.write("accept ? [ynP] ")
                            else:
                                print "invalid answer [y: yes, n: no, p: play]"
                    else:
                        accepted = True
                break
            else:
                print "Invalid answer [r: record, q: quit]"
