import setuper


class TmuxSetuper(setuper.Setuper):
    def __init__(self):
        super(sources=['.tmux.conf'])
