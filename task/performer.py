import abc


class Performer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def perform(self, task):
        raise NotImplementedError
