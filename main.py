import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog

from person import Person


class MyForm(QDialog):
    def __init__(self):
        self.ui = Ui_Dialog()
        super().__init__()
        self.ui.setupUi(self)
        self.ui.saveButton.clicked.connect(self.save_to_file)
        self.show()

    def save_to_file(self):
        name = self.ui.nameEdit.text()
        lastName = self.ui.lastNameEdit.text()
        birthDate = self.ui.birthDateEdit.text()
        pesel = self.ui.peselEdit.text()
        street = self.ui.streetEdit.text()
        zipCode = self.ui.zipCodeEdit.text()
        city = self.ui.cityEdit.text()
        with open("plik.txt","w+") as file:
            file.write(name + "-")
            file.write(lastName + "-")
            file.write(birthDate + "-")
            file.write(pesel + "-")
            file.write(street + "-")
            file.write(zipCode + "-")
            file.write(city)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())

