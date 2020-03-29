import openpyxl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys

dates = []
totals = []

extrapolation = 1000


def plot_values(filepath):
    try:
        wb = openpyxl.load_workbook(filepath)
    except openpyxl.utils.exceptions.InvalidFileException:
        print("Invalid file name...")
        return

    sheet = wb.get_sheet_by_name('Sheet1')

    try:
        for i in range(2, sheet.max_row):
            temp = sheet.cell(row=i, column=1).value
            dates.append(temp.date())
            totals.append(sheet.cell(row=i, column=2).value)

    except TypeError:
        print("File is incorrectly formatted...")
        return
    except:
        e = sys.exc_info()[0]
        print("Error: " + str(e))
        print("Unknown error...")
        return


    print(totals)

    try:
        x = mdates.date2num(dates)
        y = totals

        poly_degree = 2
        z4 = np.polyfit(x, totals, poly_degree)
        p4 = np.poly1d(z4)

        print(p4)

        fig, cx = plt.subplots()
        xx = np.linspace(x.min(), x.max(), 1000)
        dd = mdates.num2date(xx)

    except:
        print("Interpolation processing failure...")
        return

    try:
        cx.plot(dd, p4(xx), '-g')
        cx.plot(dates, y, '+', color='b', label='blub')

        cx.grid()
        cx.set_ylim(0, 100000)
        plt.show()

    except:
        e = sys.exc_info()[0]
        print("Error: " + str(e))
        print("Pyplot failure, unable to plot data...")
        return
