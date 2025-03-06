class Adress:
    def __init__(self,street,zipcode,city):
        self.street = street
        self.zipcode = zipcode
        self.city = city

class Person:
    def __init__(self,name,lastName,birthDate,pesel,street,zipCode,city):
        self.name = name
        self.lastname = lastName
        self.birthDate = birthDate
        self.pesel = pesel
        self.address = Adress(street,zipCode,city)

    def validate_pesel(self):
        z=0
        wynik = 0
        if self.pesel.isdigit() and len(self.pesel) == 11:

            # obliczanie wagi
            for i in range(len(self.pesel)):
                if z == 0:
                    wynik += int(self.pesel[i]) * 1
                    z = z+1
                elif z == 1:
                    wynik += int(self.pesel[i]) * 3
                    z = z+1
                elif z == 2:
                    wynik += int(self.pesel[i]) * 7
                    z = z+1
                elif z==3:
                    wynik += int(self.pesel[i]) * 9
                    z = 0

            #reszta
            wynikWyniku = (wynik%10)-10

            if wynikWyniku == 10:
                wynikWyniku = 0

            return wynikWyniku

        raise ValueError("Invalid pesel")