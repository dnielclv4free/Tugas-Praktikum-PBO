

import math

class NegativeError(Exception):
    pass

class ZeroError(Exception):
    pass

class Square:
    def __init__(self, number):
        self.number = number

    def count(self):
        if self.number < 0:
            raise NegativeError("Input tidak valid. Harap masukkan angka positif.")

        if self.number == 0:
            raise ZeroError("Akar kuadrat dari nol tidak diperbolehkan.")

        print(f"Akar kuadrat dari {self.number} adalah {math.sqrt(self.number)}")

while True:
    user_input = input("Masukkan angka: ")
    try:
        number = float(user_input)
        calc = Square(number)
        calc.count()
        break
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang valid.")
    except NegativeError as e:
        print(e)
    except ZeroError as e:
        print(e)

