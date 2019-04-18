from .linker_marshall import LinkerMarshall


class ZshLinker(LinkerMarshall):
    def __init__(self):
        super().__init__(srcs=['.zshrc'])
