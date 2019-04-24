#!/usr/bin/env python3
import argparse
import logging
import os
import sys
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
        self.logger.info(f'Clonning {self.repo} to {self.dotfiles}')
        os.system(f'git clone {self.repo} {self.dotfiles}')

    def pull_dotfiles_repo(self):
        self.logger.info('Pulling existing dotfiles')
        os.system(f'cd {self.dotfiles} && git pull && cd -')

    def run_targets(self):
        for target in self.targets:
            self.run_target(target)

    def run_target(self, target):
        if target not in TARGETS:
            self.logger.error(f'{target} is not a target, skipping')
            return

        self.logger.info(f'Running {target}')
        TARGETS[target].run(self.dotfiles)


if __name__ == '__main__':
    args = parse_args()
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    app = App(args, log_fmt)
    app.run()
