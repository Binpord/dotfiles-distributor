import os
import sys
import logging


class Setuper:
    def __init__(self, srcs, dst=os.getenv('HOME')):
        self.srcs = srcs
        self.dst = dst

    def setup(self, dotfiles):
        for src in self.srcs:
            dotfile = os.path.join(dotfiles, src)
            dst = os.path.join(self.dst, src)
            self.link_dotfile(dotfile, dst)

    def link_dotfile(self, dotfile, dst):
        logger = logging.getLogger()
        if not os.path.exists(dotfile):
            logger.critical('Failed to find {} dotfile'.format(dotfile))
            sys.exit(1)

        self.prepare_dst(dst)
        logger.info('Linking dotfile {} to {}'.format(dotfile, dst))
        os.link(dotfile, dst)

    def prepare_dst(self, dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.exists(dst):
            self.replace_dst(dst)

    def replace_dst(self, dst):
        logger = logging.getLogger()
        logger.info(
            '{} file already exists. Moving it to {}.pre-setup'.format(
                dst, dst
            )
        )
        os.replace(dst, '{}.pre-setup'.format(dst))
