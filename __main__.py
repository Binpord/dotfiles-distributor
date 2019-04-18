#!/usr/bin/env python3
import argparse
import logging
import os
import sys
from targets import targets


def parse_args():
    ap = argparse.ArgumentParser(description='Set up my config files')
    ap.add_argument(
        '--repo',
        type=str,
        default='https://github.com/Binpord/dotfiles.git',
        help='Repository with dotfiles')
    ap.add_argument('targets', metavar='T', type=str,
                    nargs='+', help='Targets to setup')
    return ap.parse_args()


def setup_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)
    root.info('Logging is set')


def clone_dotfiles_repo(repo, dotfiles):
    logger = logging.getLogger()
    logger.info('Clonning {} to {}'.format(args.repo, dotfiles))
    os.system('git clone {} {}'.format(repo, dotfiles))


def pull_dotfiles_repo(dotfiles):
    logger = logging.getLogger()
    logger.info('Pulling existing dotfiles')
    os.system('cd {} && git pull && cd -'.format(dotfiles))


def get_dotfiles(repo, dotfiles):
    logger = logging.getLogger()
    logger.info('Getting dotfiles')
    if not os.path.exists(dotfiles):
        clone_dotfiles_repo(args.repo, dotfiles)
    else:
        pull_dotfiles_repo(dotfiles)


def setup_target(target, dotfiles):
    logger = logging.getLogger()
    if target not in targets:
        logger.warn('{} is not an available target'.format(target))
        logger.info('Skipping {}'.format(target))
        return

    logger.info('Setting up {}'.format(target))
    targets[target].setup(dotfiles)


def setup_targets(targets, dotfiles):
    for target in targets:
        setup_target(target, dotfiles)


if __name__ == '__main__':
    args = parse_args()
    setup_logging()
    dotfiles = os.path.abspath('./dotfiles')
    get_dotfiles(args.repo, dotfiles)
    setup_targets(args.targets, dotfiles)
