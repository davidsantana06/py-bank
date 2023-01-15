from datetime import datetime


class Person:
    DATE_FORMAT = '%m/%d/%Y'

    def __init__(self, name, document, birthdate: datetime):
        self.__name = name
        self.__document = document
        self.__birthdate = birthdate

    # NAME ------------------
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    # -----------------------

    # DOCUMENT ----------------------
    def set_document(self, document):
        self.__document = document

    def get_document(self):
        return self.__document
    # -------------------------------

    # BIRTHDATE -----------------------
    def set_birthdate(self, birthdate):
        self.__birthdate = birthdate

    def get_birthdate(self):
        return self.__birthdate
    # ---------------------------------

    def __str__(self):
        string = '> Name: ' + self.__name + '\n' \
            + '> Document: ' + str(self.__document) + '\n' \
            + '> Birthdate: ' + self.__birthdate.strftime(str(self.DATE_FORMAT))

        return string
