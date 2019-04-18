from .setuper import Setuper


class VimSetuper(Setuper):
    def __init__(self):
        super().__init__(srcs=[
            '.vimrc', '.config/nvim/init.vim', '.vim/ycm_extra_conf.py'
        ])
