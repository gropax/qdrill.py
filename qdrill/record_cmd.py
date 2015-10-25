import sys

class RecordCmd:
    def __init__(self, config, rec):
        self.config = config
        self.recording = rec

    def record(self):
        self.recording.start()
        sys.stdout.write("recording... [enter to stop] ")
        input()
        self.recording.stop()
        sys.stdout.write("recorded %.2fs\n" % self.recording.duration())

    def execute(self):
        sys.stdout.write("\033[92m%s\033[0m\t" % self.recording.text)

        sys.stdout.write("  [Rsq] ")
        while True:
            ans = input() or "r"
            if ans == 'q':
                sys.stdout.write("Exiting...")
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
                            ans = input() or default
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
                                sys.stdout.write("invalid answer [y: yes, n: no, p: play]")
                    else:
                        accepted = True
                break
            else:
                sys.stdout.write("Invalid answer [r: record, q: quit]")
