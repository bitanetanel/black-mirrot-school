from InvalidMessageException import InvalidMessageException
import struct


class RequestParser(object):
    # Message format, for the struct object:
    # i -> int (integer)
    # b -> signed char (integer)
    # s -> char[] (string)
    # See https://docs.python.org/2/library/struct.html#format-characters
    MESSAGE_FORMAT = "ibis"

    def __init__(self, message):
        self._message = message
        self.is_valid = False
        self._REQ_NUMBER = None
        self._OP_CODE = None
        self._SIZE = None
        self._PAYLOAD = None

    def parse(self):
        try:
            self._REQ_NUMBER, self._OP_CODE, self._SIZE, self._PAYLOAD = \
                struct.unpack(self.MESSAGE_FORMAT, self._message)
            self.is_valid = True
        except Exception:
            self.is_valid = False
        return self