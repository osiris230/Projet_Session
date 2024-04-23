class Event:
    def __init__(self, nom, date, emplacement, prix, images, description):
        self.__nom = nom
        self.__date = date
        self.__emplacement = emplacement
        self.__prix = prix

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def emplacement(self):
        return self.__emplacement

    @emplacement.setter
    def emplacement(self, value):
        self.__emplacement = value

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, value):
        self.__prix = value

    @property
    def images(self):
        return self.__images

    @images.setter
    def images(self, value):
        self.__images = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value