class config():
    """
    docstring for config
    """
    def __init__(self, file):
        self.conf = dict(line.strip().split('=') for line in open(file))

    def off_target(self):
        return self.conf["off-target"] == "True"
