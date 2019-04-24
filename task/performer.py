import abc
from .task import Task


class Performer(abc.ABCMeta):
    @abc.abstractmethod
    def perform(self, task):
        raise NotImplementedError


class BackendedPerformer(Performer):
    def __init__(self, backends):
        self.backends = backends

    def perform(self, task):
        if not isinstance(task, Task):
            raise ValueError(f'{task!r} is not a task')

        self.backends[task.type].perform()
