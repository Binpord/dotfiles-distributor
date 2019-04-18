from .linker_marshall import LinkerMarshall


class TmuxLinker(LinkerMarshall):
    def __init__(self):
        super().__init__(srcs=['.tmux.conf'])
