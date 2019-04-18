import os
import sys
import logging


class Setuper:
    def __init__(self, sources, destination=os.getenv('HOME')):
        self.sources = sources
        self.destination = destination

    def setup(self, dotfiles):
        for source in self.sources:
            dotfile = os.path.join(dotfiles, source)
            destination = os.path.join(self.destination, source)
            self.link_dotfile(dotfile, destination)

    def link_dotfile(self, dotfile, destination):
        logger = logging.getLogger()
        if not os.path.exists(dotfile):
            logger.critical('Failed to find {} dotfile'.format(dotfile))
            sys.exit(1)

        self.prepare_destination(destination)
        logger.info('Linking dotfile {} to {}'.format(dotfile, destination))
        os.link(dotfile, destination)

    def prepare_destination(self, destination):
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        if os.path.exists(destination):
            self.replace_destination(destination)

    def replace_destination(self, destination):
        logger = logging.getLogger()
        logger.info(
            '{} file already exists. Moving it to {}.pre-setup'.format(
                destination, destination
            )
        )
        os.replace(destination, '{}.pre-setup'.format(destination))
