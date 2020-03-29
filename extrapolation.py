import openpyxl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

dates = []
totals = []

extrapolation = 1000

def plot_values(filepath):

    try:
        wb = openpyxl.load_workbook(filepath)
        print(filepath)
    except openpyxl.utils.exceptions.InvalidFileException:
        print("Invalid file name!")

        return

    sheet = wb.get_sheet_by_name('Sheet1')

    for i in range(2, sheet.max_row):
        temp = sheet.cell(row=i, column=1).value
        print(temp)
        dates.append(temp.date())
        totals.append(sheet.cell(row=i, column=2).value)

    print(totals)
    x = mdates.date2num(dates)
    y = totals

    poly_degree = 2
    z4 = np.polyfit(x, totals, poly_degree)
    p4 = np.poly1d(z4)

    print(p4)

    fig, cx = plt.subplots()

    xx = np.linspace(x.min(), x.max()+extrapolation, 1000)
    dd = mdates.num2date(xx)

    cx.plot(dd, p4(xx), '-g')
    cx.plot(dates, y, '+', color='b', label='blub')

    cx.grid()
    cx.set_ylim(0, 100000)
    plt.show()
