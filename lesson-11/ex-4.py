class Description:
    @classmethod
    def descript(cls):
        print(f'На складе оргтехники есть:'
              f'\n{OfficeEquipment.num_printer} принтера ({Printer.black_white} черно-белых и {Printer.multicolored} разноцветных)'
              f'\n{OfficeEquipment.num_scanner} сканера ({Scanner.manual} ручной и {Scanner.flatbed} планшетных)'
              f'\n{OfficeEquipment.num_copier} ксерокс ({Copier.classik} классический и {Copier.laser} лазерных)')

class OfficeEquipment:
    num_printer = 3
    num_scanner = 5
    num_copier = 1

class Printer(OfficeEquipment):
    black_white = 2
    multicolored = 1

class Scanner(OfficeEquipment):
    manual = 1
    flatbed = 4

class Copier(OfficeEquipment):
    classik = 1
    laser = 0

e = Description.descript()
