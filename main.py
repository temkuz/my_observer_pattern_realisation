from dataclasses import dataclass
from event_system import Event, Publisher, Subscriber


@dataclass
class TestEvent1(Event):
    field1: str
    field2: int


@dataclass
class TestEvent2(Event):
    foo: str
    bar: str


class TestPublisher(Publisher):
    def __init__(self, name):
        self.name = name


class TestSubscriber(Subscriber):
    def __init__(self, name):
        self.name = name

    def test_event_handler1(self, event: TestEvent1):
        print(f'{self.name} handle TestEvent1: {event}')

    def test_event_handler2(self, event: TestEvent2):
        print(f'{self.name} handle TestEvent2: {event}')

    def notify(self, event: Event):
        if isinstance(event, TestEvent1):
            self.test_event_handler1(event)
        elif isinstance(event, TestEvent2):
            self.test_event_handler2(event)
        else:
            raise f'Unknown event {event}'


event1 = TestEvent1('foo', 1)
event2 = TestEvent2('bar', 'buzz')

publisher = TestPublisher('publisher')

subscriber1 = TestSubscriber('sub1')
subscriber2 = TestSubscriber('sub2')

publisher.subscribe(subscriber1)
publisher.send_event(event1)

publisher.subscribe(subscriber2)
publisher.send_event(event2)
