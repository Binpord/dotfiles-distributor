import abc
from . import Targets


class Target(abc.ABCMeta):
    @abc.abstractmethod
    def run(self, dotfiles):
        raise NotImplementedError


class BackendedTarget:
    def __init__(self, backends):
        self.backends = backends

    def run(self, target, dotfiles):
        if not isinstance(target, Targets):
            raise ValueError(f'{target!r} is not a target')

        self.backends[target].run(dotfiles)
