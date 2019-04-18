from .linker_marshall import LinkerMarshall


class GitLinker(LinkerMarshall):
    def __init__(self):
        super().__init__(srcs=['.gitconfig'])
