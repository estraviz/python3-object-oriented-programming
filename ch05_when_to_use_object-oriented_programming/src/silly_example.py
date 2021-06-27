class Silly:
    def _get_silly(self):
        print("You are getting silly")
        return self._silly

    def _set_silly(self, value):
        print(f"You are making silly {value}")
        self._silly = value

    def _del_silly(self):
        print("Silly has been deleted!")
        del self._silly

    silly = property(_get_silly, _set_silly, _del_silly, "This is a silly property")


class DecoratedSilly:
    @property
    def silly(self):
        """This is a silly property, but using decorators"""
        print("You are getting silly")
        return self._silly

    @silly.setter
    def silly(self, value):
        print(f"You are making silly {value}")
        self._silly = value

    @silly.deleter
    def silly(self):
        print("Silly has been deleted!")
        del self._silly
