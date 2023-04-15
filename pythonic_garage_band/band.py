from abc import ABC, abstractmethod

class Musician(ABC):
    """Abstract base class for musicians."""

    def __init__(self, name: str):
        """Initialize a Musician with a name."""
        self.name = name

    def __str__(self) -> str:
        """Return a string representation of a Musician."""
        return f'Musician Name: {self.name}'

    def __repr__(self) -> str:
        """Return a string representation of a Musician for debugging."""
        return f'I\'m representation of Musician: {self.name}'

    @abstractmethod
    def get_instrument(self) -> str:
        """Return the name of the instrument the Musician plays."""
        pass

    @abstractmethod
    def play_solo(self) -> str:
        """Return a string representation of the Musician's solo."""
        pass


class Guitarist(Musician):
    """A musician who plays the guitar."""

    def __init__(self, name: str):
        """Initialize a Guitarist with a name."""
        super().__init__(name)

    def __repr__(self) -> str:
        """Return a string representation of a Guitarist for debugging."""
        return f'Guitarist instance. Name = {self.name}'

    def __str__(self) -> str:
        """Return a string representation of a Guitarist."""
        return f'My name is {self.name} and I play guitar'

    def get_instrument(self) -> str:
        """Return the name of the instrument the Guitarist plays."""
        return 'guitar'

    def play_solo(self) -> str:
        """Return a string representation of the Guitarist's solo."""
        return "face melting guitar solo"


class Bassist(Musician):
    """A musician who plays the bass."""

    def __init__(self, name: str):
        """Initialize a Bassist with a name."""
        super().__init__(name)

    def __repr__(self) -> str:
        """Return a string representation of a Bassist for debugging."""
        return f'Bassist instance. Name = {self.name}'

    def __str__(self) -> str:
        """Return a string representation of a Bassist."""
        return f'My name is {self.name} and I play bass'

    def get_instrument(self) -> str:
        """Return the name of the instrument the Bassist plays."""
        return 'bass'

    def play_solo(self) -> str:
        """Return a string representation of the Bassist's solo."""
        return "bom bom buh bom"


class Drummer(Musician):
    """A musician who plays the drums."""

    def __init__(self, name: str):
        """Initialize a Drummer with a name."""
        super().__init__(name)

    def __repr__(self) -> str:
        """Return a string representation of a Drummer for debugging."""
        return f'Drummer instance. Name = {self.name}'

    def __str__(self) -> str:
        """Return a string representation of a Drummer."""
        return f'My name is {self.name} and I play drums'

    def get_instrument(self) -> str:
        """Return the name of the instrument the Drummer plays."""
        return 'drums'

    def play_solo(self) -> str:
        """Return a string representation of the Drummer's solo."""
        return 'rattle boom crash'


class Band:
    """ A band with a name and a list of members. """
    instances = []

    def __init__(self, name, members):
        """Initialize a new Band object with a name and list of members"""
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __repr__(self):
        """Return a string representation of a Band object"""
        return f'Band instance. Name = {self.name}'

    def __str__(self):
        """Return a string representation of a Band object"""
        return f'{self.name} band'

    @classmethod
    def to_list(cls):
        """Return a list of all Band instances"""
        return cls.instances

    def play_solos(self):
        """Have each band member play a solo and return a list of the results"""
        return [member.play_solo() for member in self.members]
