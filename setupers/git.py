from .setuper import Setuper


class GitSetuper(Setuper):
    def __init__(self):
        super().__init__(sources=['.gitconfig'])
