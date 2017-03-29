from simple_es.identifier.identifies import Identifies


class DomainEvent():
    """
    Base class for all domain driven events
    """
    identifier = None

    def __init__(self, identifier=None):
        if not isinstance(identifier, Identifies):
            raise TypeError('Event identifier must be an instance of the Identifies class', identifier)

        self.identifier = identifier
