from abc import ABCMeta, abstractmethod


class drawable():
    """
    base class for all drawable classes
    """
    __metaclass__ = ABCMeta
    fontYoffset = -2  # Move up a couple lines so descenders aren't cropped

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def update(self):
        pass
