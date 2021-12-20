from termcolor import colored


class Date:

    @classmethod
    def day(cls, data):
        dmf = []
        df = int(data[:2])
        mf = int(data[3:-5])
        yf = int(data[-4:])
        dmf.append(df)
        dmf.append(mf)
        dmf.append(yf)
        return dmf

    @staticmethod
    def valid(dat):
        dd = Date.day(dat)
        if dd[0] <= 0 or dd[0] > 31:
            dd = colored('ErorDateDay', 'red')
        elif dd[1] <= 0 or dd[1] > 12:
            dd = colored('ErorDateMonth', 'red')
        elif dd[2] != 2021:
            dd = colored('ErorDateYear', 'red')
        return colored(dd, 'yellow')


print(Date.valid('31-12-2021'))