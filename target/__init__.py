import enum
from .vim import Vim
from .tmux import Tmux
from .zsh import Zsh
from .git import Git
from .target import BackendedTarget


@enum.unique
class Targets(enum.Enum):
    VIM = 'vim'
    ZSH = 'zsh'
    TMUX = 'tmux'
    GIT = 'git'


targets = BackendedTarget({
    Targets.VIM:  Vim(),
    Targets.ZSH:  Zsh(),
    Targets.TMUX: Tmux(),
    Targets.GIT:  Git(),
})
