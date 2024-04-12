class Reservation:
    def __init__(self, nom, place, status):
        self.__nom = nom
        self.__place = place
        self.__status = status

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        self.__place = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value