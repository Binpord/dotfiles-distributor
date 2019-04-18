from . import vim, tmux, git, zsh

TARGETS = {
    'vim':  vim.VimLinker(),
    'zsh':  zsh.ZshLinker(),
    'tmux': tmux.TmuxLinker(),
    'git':  git.GitLinker(),
}
