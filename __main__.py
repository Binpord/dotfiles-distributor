#!/usr/bin/env python3
import argparse
import logging
import os
import sys
import git
from targets import TARGETS


def parse_args():
    ap = argparse.ArgumentParser(description='Set up my config files')
    ap.add_argument('targets', metavar='T', type=str,
                    nargs='+', help='Targets to setup')
    ap.add_argument('--repo', type=str,
                    default='https://github.com/Binpord/dotfiles.git',
                    help='Repository with dotfiles')
    ap.add_argument('--dotfiles', type=str,
                    default='./dotfiles',
                    help='Directory to clone/pull repo')
    return ap.parse_args()


class App:
    def __init__(self, args, log_fmt):
        self.targets = args.targets
        self.repo = args.repo
        self.dotfiles = os.path.abspath(args.dotfiles)

        self.setup_logging(log_fmt)
        self.logger = logging.getLogger(__name__)

    def setup_logging(self, log_fmt):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(log_fmt)
        handler.setFormatter(formatter)

        root.addHandler(handler)
        root.info('Logging is set')

    def run(self):
        self.get_dotfiles()
        self.run_targets()

    def get_dotfiles(self):
        self.logger.info('Getting dotfiles')
        if not os.path.exists(self.dotfiles):
            self.clone_dotfiles_repo()
        else:
            self.pull_dotfiles_repo()

    def clone_dotfiles_repo(self):
        self.logger.info('Clonning {} to {}'.format(self.repo, self.dotfiles))
        git.Repo.clone_from(self.repo, self.dotfiles)

    def pull_dotfiles_repo(self):
        self.logger.info('Pulling existing dotfiles')
        git.Repo(self.dotfiles).remotes.origin.pull()

    def run_targets(self):
        for target in self.targets:
            self.run_target(target)

    def run_target(self, target):
        if target not in TARGETS:
            self.logger.error('{} is not a target, skipping'.format(target))
            return

        self.logger.info('Running {}'.format(target))
        TARGETS[target].run(self.dotfiles)


if __name__ == '__main__':
    args = parse_args()
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    app = App(args, log_fmt)
    app.run()
