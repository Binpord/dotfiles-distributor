from . import vim, tmux, git, zsh

TARGETS = {
    'vim':  vim.VimSetuper(),
    'zsh':  zsh.ZshSetuper(),
    'tmux': tmux.TmuxSetuper(),
    'git':  git.GitSetuper(),
}
