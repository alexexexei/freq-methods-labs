import csv
from datetime import datetime
import numpy as np

import build_func as bf
from task2 import W_1f, fft_flt


file = 'fm_lab4/data/SBER_180321_190321.csv'
find_date = 'DATE'
find_price = 'CLOSE'
dates = []
prices = []
with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    header = next(csv_reader)
    date_i = 0
    price_i = 0
    for i in range(len(header)):
        if find_date in header[i]:
            date_i = i
        if find_price in header[i]:
            price_i = i

    for row in csv_reader:
        dates.append(row[date_i])
        prices.append(float(row[price_i]))

date_step = 1
n = len(dates)
v = np.fft.fftfreq(n, d=date_step)
w = 2 * np.pi * v

T = 1
W = W_1f(w, T)
flt_u, flt_U, U = fft_flt(prices, W, False)

bf.build_fs(dates, [prices, flt_u.real], ticks=range(0, len(dates), 7),
            rot=45, xlab='Dates', ylab='Prices (close)',
            ttl=f'First order linear filter, date_step={date_step}, T={T}', fz2=8,
            legend=True, labels=['Original prices', 'Smoothed prices'])