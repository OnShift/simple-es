from simple_es.identifier.identifies import Identifies
from simple_es.utils import camelize


class DomainEvent():
    """
    Base class for all domain driven events

    TODO: Split logic around saving to a data store into a separate class
    TODO: Restrict the ability to toggle recorded
    """
    event_type = None
    _identifier = None
    _recorded = False

    def __init__(self, identifier=None, event_type=None):
        # Validate that identifier is an instance of an event Identifier
        if not isinstance(identifier, Identifies):
            raise TypeError('Event identifier must be an instance of the Identifies class',
                            identifier,
                            type(identifier))

        # Validate that event type was set in a child
        if event_type is None:
            raise TypeError('Event type must be a string', event_type, type(event_type))

        # Assign the identifier to the event
        self._identifier = identifier

        # Assign the type to the event
        self.event_type = event_type

    @property
    def attributes(self):
        """
        Filter out private member variables (names prefixed with an underscore)
        """
        return camelize({
            k: v for k, v
            in self.__dict__.items()
            if k.startswith('_') is False
        })
