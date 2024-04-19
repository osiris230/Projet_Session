class Paiement:
    def __init__(self, nom_complet, telephone, email, carte_credit):
        self.__nom_complet = nom_complet
        self.__telephone = telephone
        self.__email = email
        self.__carte_credit = carte_credit

    @property
    def nom_complet(self):
        return self.__nom_complet

    @nom_complet.setter
    def nom_complet(self, value):
        self.__nom_complet = value

    @property
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, value):
        self.__telephone = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def carte_credit(self):
        return self.__carte_credit

    @carte_credit.setter
    def carte_credit(self, value):
        self.__carte_credit = value
