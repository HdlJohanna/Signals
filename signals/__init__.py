class Pointer:
    def __init__(self, name, content=None):
        self.name = name
        self.content = content

    def emit(self, *args, **kwargs):
        self.content(*args, **kwargs)

    def connect_signal(self, master:"Signal"):
        master.connect(self.name)(self.content)

    def connect(self, function):
        self.content = function

def sigverif(signal_sender, secret_key):
    """
    Verify a Signal's Origin.

    Upon creating the Signal, you specify a name for it.
    This name MUST BE equal to :param: secret_key

    >>> s = Signal('my-signal')
    >>> sigverif(s, 'my-signal')
    True
    >>> sigverif(s, 'not-my-signal')
    False
    """
    return str(signal_sender) == str(secret_key)

class Signal:
    def __init__(self, name):
        self.pointers = []
        self.name = name

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name

    def emit(self, pointer_name, *, sender = None, **kwargs):
        for p in self.pointers:
            if p.name == pointer_name:
                return p.emit(sender or self, **kwargs)

        return None

    def connect(self, name):
        def append(funct):
            self.pointers.append(Pointer(name, funct))
            return Pointer(name, funct)

        return append
