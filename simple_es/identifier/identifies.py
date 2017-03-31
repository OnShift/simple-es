class Identifies():
    _primary_key = None
    _secondary_key = None

    key_schema = None

    def __init__(self, primary_key, secondary_key=None):
        if self.key_schema is None:
            raise AttributeError('Event identifiers require a key schema containing at least one attribute name',
                                 self.key_schema)

        # Zip the key names and values together
        keys = zip(self.key_schema, [primary_key, secondary_key])

        # Generate the event key mapping(s)
        self._primary_key, self._secondary_key = [{k: v} for k, v in keys]

    @property
    def key(self):
        if self._secondary_key:
            return dict(**self._primary_key, **self._secondary_key)

        return self._primary_key

    @property
    def partition_key(self):
        return self._primary_key

    @property
    def sort_key(self):
        return self._secondary_key
