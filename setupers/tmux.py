from .setuper import Setuper


class TmuxSetuper(Setuper):
    def __init__(self):
        super().__init__(srcs=['.tmux.conf'])
