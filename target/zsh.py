import os
from .marshall import Marshall


class Zsh(Marshall):
    def __init__(self):
        self._dstdir = os.getenv('HOME')
        self._srcs = ['.zshrc']
        self._cmds = []

    @Marshall.dstdir
    def dstdir(self):
        return self._dstdir

    @Marshall.srcs
    def srcs(self):
        return self._srcs

    @Marshall.cmds
    def cmds(self):
        return self._cmds
