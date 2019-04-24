import abc
from . import performer


class Marshall(abc.ABCMeta):
    @property
    @abc.abstractmethod
    def tasks(self):
        raise NotImplementedError

    def perform(self):
        for task in self.tasks:
            performer.perform(task)
