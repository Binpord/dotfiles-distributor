import enum
from .linker import Linker
from .bash import Bash
from .performer import BackendedPerformer


@enum.unique
class TaskType(enum.Enum):
    LINK = enum.auto()
    BASH = enum.auto()


performer = BackendedPerformer({
    TaskType.LINK: Linker(),
    TaskType.BASH: Bash(),
})
