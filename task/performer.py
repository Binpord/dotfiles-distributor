import abc


class Performer(abc.ABCMeta):
    @abc.abstractmethod
    def perform(self, task):
        raise NotImplementedError
