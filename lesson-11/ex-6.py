from termcolor import colored

class OfficeEquipment:
    office_equipment = {}

class Description:

    @staticmethod
    def add_equipment(equipment, num): # вот здесь происходит проверка аргументов
        print('\n2 аргумент должен быть числом или словарём')
        if type(num) == dict:
            for n in num.values():
                if type(n) != int:
                    num = 'ErorArgument'
                    print(colored('ErorType 2 аргумент не цифра', 'red'))

        elif type(num) != int:
            num = 'ErorEquipment'
        OfficeEquipment.office_equipment[equipment] = num
        return OfficeEquipment.office_equipment

    @staticmethod
    def delet_equipment(equipment):
        del OfficeEquipment.office_equipment[equipment]
        return OfficeEquipment.office_equipment


dn = Description()
print(dn.add_equipment('computer', 1))
print(dn.delet_equipment('computer'), colored('deleted', 'red'))
print(dn.add_equipment('computer', {'apple': 3, 'Philips': 4}))
print(dn.add_equipment('computer', {'apple': 'iPad', 'Philips': 4}))
print(dn.add_equipment('computer', 'apple'))




