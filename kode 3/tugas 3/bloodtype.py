import random
class Father :
    def __init__(self, bloodtype):
        self.bloodtype = bloodtype
        self.alleles = self.getAllels()
    def getAllels(self):
        blood_map = {
            "A" : ["A", "O"],
            "B" : ["B", "O"],
            "AB" : ["A", "B"],
            "O" : ["O", "O"]
        }
        return blood_map[self.bloodtype]
class Mother :
    def __init__(self, bloodtype):
        self.bloodtype = bloodtype
        self.alleles = self.getAllels()
    def getAllels(self):
        blood_map = {
        "A" : ["A", "O"],
        "B" : ["B", "O"],
        "AB" : ["A", "B"],
        "O" : ["O", "O"]
        }
        return blood_map[self.bloodtype]

class Child :
    def __init__(self, father : Father, mother : Mother):
        self.father_alleles = father.alleles
        self.mother_alleles = mother.alleles

        self.inherited_alleles = [random.choice(self.father_alleles), random.choice(self.mother_alleles)]

        # Tentukan golongan darah berdasarkan alel yang diwarisi
        self.blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        """Menentukan golongan darah berdasarkan kombinasi alel."""
        alleles = sorted(self.inherited_alleles)  # Urutkan agar lebih mudah dipetakan
        if alleles == ["A", "A"] or alleles == ["A", "O"]:
            return "A"
        elif alleles == ["B", "B"] or alleles == ["B", "O"]:
            return "B"
        elif alleles == ["A", "B"]:
            return "AB"
        elif alleles == ["O", "O"]:
            return "O"

# Contoh penggunaan

bld_typF = input("Masukkan tipe darah ayah : ").upper()
bld_typM = input("Masukkan tipe darah ibu : ").upper()
father = Father(bld_typF)
mother = Mother(bld_typM)
child = Child(father, mother)

print(f"Ayah: {father.bloodtype} ({father.alleles})")
print(f"Ibu: {mother.bloodtype} ({mother.alleles})")
print(f"Anak mewarisi alel: {child.inherited_alleles}")
print(f"Golongan darah anak: {child.blood_type}")

