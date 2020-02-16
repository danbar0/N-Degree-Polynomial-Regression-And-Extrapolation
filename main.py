import openpyxl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

filename = "Savings.xlsx"
dates = []
totals = []

extrapolation = 2000


def main():
    wb = openpyxl.load_workbook(filename)
    sheet = wb.get_sheet_by_name('Sheet1')

    for i in range(3, sheet.max_row-1):
        temp = sheet.cell(row=i, column=1).value
        dates.append(temp.date())
        totals.append(sheet.cell(row=i, column=2).value)

    x = mdates.date2num(dates)
    y = totals

    poly_degree = 3
    z4 = np.polyfit(x, totals, poly_degree)
    p4 = np.poly1d(z4)

    print(p4)

    fig, cx = plt.subplots()

    xx = np.linspace(x.min(), x.max()+extrapolation, 1000)
    dd = mdates.num2date(xx)

    cx.plot(dd, p4(xx), '-g')
    cx.plot(dates, y, '+', color='b', label='blub')

    cx.grid()
    cx.set_ylim(0, 1000000)
    plt.show()


if __name__ == "__main__":
    main()