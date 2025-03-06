class Address:
    def __init__(self, street, zipcode, city):
        self.street = street
        self.zipcode = zipcode
        self.city = city

class Person:
    def __init__(self, name, lastName, birthDate, pesel, street, zipCode, city):
        self.name = name
        self.lastname = lastName
        self.birthDate = birthDate
        self.pesel = pesel
        self.address = Address(street, zipCode, city)

    def validate_pesel(self):
        if not (self.pesel.isdigit() and len(self.pesel) == 11):
            raise ValueError("Invalid PESEL: PESEL musi składać się z 11 cyfr")

        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        checksum = sum(int(self.pesel[i]) * weights[i] for i in range(10))
        control_digit = (10 - (checksum % 10)) % 10

        if control_digit != int(self.pesel[10]):
            raise ValueError("Invalid PESEL: Cyfra kontrolna jest nieprawidłowa")
        return True