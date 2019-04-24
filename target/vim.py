import os
from .marshall import Marshall


class Vim(Marshall):
    def __init__(self):
        self._dstdir = os.getenv('HOME')
        self._srcs = [
            '.vimrc', '.config/nvim/init.vim', '.vim/ycm_extra_conf.py'
        ]
        self._cmds = [
            'curl -fLo ~/.vim/autoload/plug.vim --create-dirs '
            'https://raw.githubusercontent.com/junegunn/vim-plug/'
            'master/plug.vim',
            'vim +PlugInstall +qall'
        ]

    @Marshall.dstdir
    def dstdir(self):
        return self._dstdir

    @Marshall.srcs
    def srcs(self):
        return self._srcs

    @Marshall.cmds
    def cmds(self):
        return self._cmds
