from simple_es.identifier.identifies import Identifies


class DomainEvent():
    """
    Base class for all domain driven events

    TODO: Split logic around saving to a data store into a separate class
    TODO: Restrict the ability to toggle recorded
    """
    event_type = None
    _identifier = None
    _recorded = False

    def __init__(self, identifier=None):
        if not isinstance(identifier, Identifies):
            raise TypeError('Event identifier must be an instance of the Identifies class', identifier)

        self._identifier = identifier

    @property
    def attributes(self):
        """
        Filter out private member variables (names prefixed with an underscore)
        """
        return {key: value for key, value
                in self.__dict__.items()
                if key.startswith('_') is False}
