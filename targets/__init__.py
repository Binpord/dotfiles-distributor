from . import vim, tmux, git, zsh

targets = {
    'vim':  vim.VimSetuper(),
    'zsh':  zsh.ZshSetuper(),
    'tmux': tmux.TmuxSetuper(),
    'git':  git.GitSetuper(),
}
