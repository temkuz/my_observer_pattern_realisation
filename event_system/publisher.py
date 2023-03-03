from abc import ABC

from event_system.subscriber import Subscriber
from event_system.event import Event


class Publisher(ABC):
    """The class that will send the events"""
    __subscribers: set[Subscriber] = set()

    def subscribe(self, subscriber: Subscriber):
        """Register subscriber to event"""
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        """Unregister subscriber to event"""
        self.__subscribers.remove(subscriber)

    def send_event(self, event: Event):
        """Send event to all subscribers"""
        for subscriber in self.__subscribers:
            subscriber.notify(event)
