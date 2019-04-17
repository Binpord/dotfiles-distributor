import os
import logging


class Setuper:
    def __init__(self, sources, destination=os.getenv('HOME')):
        self.sources = sources
        self.sources = destination

    def setup(self, dotfiles):
        for source in self.sources:
            dotfile = os.path.join(dotfiles, source)
            destination = os.path.join(self.destination, source)
            self.link_dotfile(dotfile, destination)

    def link_source(self, dotfile, destination):
        assert os.path.exists(
            dotfile
        ), 'File {} should be in dotfiles repo'.format(dotfile)

        logger = logging.getLogger()
        logger.info('Linking dotfile {} to {}'.format(dotfile, destination))
        os.makedirs(destination, exist_ok=True)
        if os.path.exists(destination):
            logger.info(
                '{} file already exists; renaming it to {}.pre-setup'.format(
                    destination, destination
                )
            )
            os.rename(destination, '{}.pre-setup')

        os.link(dotfile, destination)
