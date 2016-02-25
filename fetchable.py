from abc import ABCMeta, abstractmethod


class fetchable():
    """
    base class for all drawable classes
    """
    __metaclass__ = ABCMeta
    fontYoffset = -2  # Move up a couple lines so descenders aren't cropped

    @abstractmethod
    def fetch(self):
        pass
