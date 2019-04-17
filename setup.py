#!/usr/bin/env python3
import argparse
import logging
import os
import setupers

TARGETS = {
    'vim':  setupers.vim.VimSetuper(),
    'zsh':  setupers.zsh.ZshSetuper(),
    'tmux': setupers.tmux.TmuxSetuper(),
    'git':  setupers.git.GitSetuper(),
}


def parse_args():
    ap = argparse.ArgumentParser(description='Set up my config files')
    ap.add_argument(
        '--repo',
        type=str,
        default='https://github.com/Binpord/dotfiles.git',
        help='Repository with dotfiles')
    ap.add_argument('targets', metavar='T', type=str,
                    nargs='*', help='Targets to setup')
    return ap.parse_args()


def clone_dotfiles_repo(repo, dotfiles):
    os.system('git clone {} {}'.format(repo, dotfiles))


def pull_dotfiles_repo(dotfiles):
    os.system('cd {} && git pull && cd -'.format(dotfiles))


def get_dotfiles(repo, dotfiles):
    logger = logging.getLogger()
    if not os.path.exists(dotfiles):
        logger.info('Clonning {} to {}'.format(args.repo, dotfiles))
        clone_dotfiles_repo(args.repo, dotfiles)
    else:
        logger.info('Pulling existing dotfiles')
        pull_dotfiles_repo(dotfiles)


def setup_target(target, dotfiles):
    logger = logging.getLogger()
    if target not in TARGETS:
        logger.warn('{} is not an available target'.format(target))
        logger.info('Skipping {}'.format(target))
        return

    logger.info('Setting up {}'.forma(target))
    TARGETS[target].setup(dotfiles)


def setup_targets(targets, dotfiles):
    for target in targets:
        setup_target(target, dotfiles)


if __name__ == '__main__':
    args = parse_args()
    dotfiles = './dotfiles'
    get_dotfiles(args.repo, dotfiles)
    setup_targets(dotfiles)
