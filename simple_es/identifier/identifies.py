class Identifies():
    _id = None
    _secondary_id = None

    def __init__(self, primary_key, secondary_key=None):
        self._id = primary_key

        if secondary_key:
            self._secondary_id = secondary_key

    @property
    def id(self):
        return self._id

    @property
    def partition_key(self):
        return self._id

    @property
    def sort_key(self):
        return self._secondary_id
