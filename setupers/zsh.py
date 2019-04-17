from .setuper import Setuper


class ZshSetuper(Setuper):
    def __init__(self):
        super().__init__(sources=['.zshrc'])
