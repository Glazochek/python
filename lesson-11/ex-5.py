class OfficeEquipment:
    office_equipment = {}
    office_equipment['printer'] = None
    office_equipment['scanner'] = None
    office_equipment['copier'] = None


class Printer(OfficeEquipment):
    printer = {}
    printer['black_white'] = 2
    printer['multicolored'] = 1


class Scanner(OfficeEquipment):
    scanner = {}
    scanner['manual'] = 1
    scanner['flatbed'] = 4


class Copier(OfficeEquipment):
    copier = {}
    copier['classik'] = 1
    copier['laser'] = 0


class Printed:
    @staticmethod
    def slov():
        OfficeEquipment.office_equipment['printer'] = Printer.printer
        OfficeEquipment.office_equipment['scanner'] = Scanner.scanner
        OfficeEquipment.office_equipment['copier'] = Copier.copier
        print(OfficeEquipment.office_equipment)


class Description:
    @staticmethod
    def add_equipment(equipment, num):
        OfficeEquipment.office_equipment[equipment] = num

    @staticmethod
    def delet_equipment(equipment):
        del OfficeEquipment.office_equipment[equipment]


comp_type = {'apple': 1,  'Philips': 4}
re = Printed()
ry = Description()
ry.add_equipment('computer', 4)
ry.add_equipment('computer', comp_type)
re.slov()
ry.delet_equipment('computer')
re.slov()
