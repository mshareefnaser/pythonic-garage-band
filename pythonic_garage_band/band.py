from abc import ABC, abstractmethod


class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Musician Name: {self.name}'

    def __repr__(self):
        return f'I\'m representation of Musician: {self.name}'

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return 'rattle boom crash'


class Band(Musician):
    def __init__(self, name,members):
        self.name = name
        self.members = members
        super().__init__(name)

    def __repr__(self):
        return f''

    def __str__(self):
        return f''
    
    def to_list (self): #returns a list of previously created Band instances
        pass

    def play_solos (self): # asks each member musician to play a solo, in the order they were added to band
        pass
