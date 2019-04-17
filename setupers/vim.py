import setuper


class VimSetuper(setuper.Setuper):
    def __init__(self):
        super(sources=[
            '.vimrc', '.config/nvim/init.vim', '.vim/ycm_extra_conf.py'
        ])
