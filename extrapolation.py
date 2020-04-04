import openpyxl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import sys

dates = []
totals = []

extrapolation = 1000

error_string = {
    "bad_file_name":    "Invalid file name",
    "bad_file_format":  "File is incorrectly formatted",
    "bad_interp":       "Interpolation processing error",
    "pyplot_failure":   "Pyplot failed to run properly",

    "unknown_error":    "Unknown error: "
}

def plot_values(file_path):
    try:
        wb = openpyxl.load_workbook(file_path)
    except openpyxl.utils.exceptions.InvalidFileException:
        raise Exception(error_string["bad_file_name"])

    sheet = wb.get_sheet_by_name('Sheet1')

    try:
        for i in range(2, sheet.max_row):
            temp = sheet.cell(row=i, column=1).value
            dates.append(temp.date())
            totals.append(sheet.cell(row=i, column=2).value)

    except TypeError:
        raise Exception(error_string["bad_file_format"])

    else:
        e = sys.exc_info()[0]
        raise Exception(error_string["unknown_error"] + str(e))

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
        raise Exception(error_string["bad_interp"])

    try:
        cx.plot(dd, p4(xx), '-g')
        cx.plot(dates, y, '+', color='b', label='blub')

        cx.grid()
        cx.set_ylim(0, 100000)
        plt.show()

    except:
        e = sys.exc_info()[0]
        print("Error: " + str(e))
        raise Exception(error_string["pyplot_failure"])

