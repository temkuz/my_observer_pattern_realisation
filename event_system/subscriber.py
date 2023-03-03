from abc import ABC, abstractmethod

from event_system.event import Event


class Subscriber(ABC):
    """The class that will subscribe to events"""

    @abstractmethod
    def notify(self, event: Event):
        """Handle event here"""
        ...
