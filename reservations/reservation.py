class Reservation:
    def __init__(self, nom, place, status, event):
        self.__nom = nom
        self.__place = place
        self.__status = status
        self.__event = event

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

    @property
    def event(self):
        return self.__event

    @event.setter
    def event(self, value):
        self.__event = value