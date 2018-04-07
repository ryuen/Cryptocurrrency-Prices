import time
import datetime
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import pandas as pd 

howFarBack = 10000

def rsiFunc(prices, n=14):
        deltas = np.diff(prices)
        
        seed = deltas[:n+1]

        up = seed[seed>=0].sum()/n

        down = -seed[seed<0].sum()/n

        rs = up/down
        rsi = np.zeros_like(prices)
        rsi[:n] = 100. - 100./(1.+rs)
        #print(rsi[:n])
        for i in range(n, len(prices)-1):
                delta = deltas[i-1]
                #print('delta:',delta)
                if delta > 0:
                        upval = delta
                        downval = 0.
                else:
                        upval = 0.
                        downval =-delta
                up = (up*(n-1)+upval)/n
                down = (down*(n-1)+downval)/n

                rs = up/down
                rsi[i] = 100. - 100./(1.+rs)     
                         
        return rsi      

def ExpMovingAverage(values, window):
        weights = np.exp(np.linspace(-1.,0., window))
        weights /= weights.sum()
        a = np.convolve(values, weights, mode='full')[:len(values)]
        a[:window] = a[window]
        return a

def chartData():
	Datear = []
	Pricear = []
	Volumear = []

	df = pd.read_csv('Data\BitfinexBTCUSD.csv', parse_dates = True, names=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

	df['Date'] = pd.to_datetime(df['Date'], unit='s')

	Datear = df['Date'][-howFarBack:]
	Pricear = df['Close'][-howFarBack:]
	Volumear = df['Volume'][-howFarBack:]

	ax1 = plt.subplot2grid((6,4),(2,0), rowspan=4, colspan=4)
	ax1.plot(Datear, Pricear)
	ax1.grid(True)

	rsiLine = rsiFunc(Pricear, n=50)

	ax2 = plt.subplot2grid((6,4),(0,0), rowspan=2, colspan=4)
	ax2.plot(Datear, rsiLine)	
	ax2.grid(True)
	ax2.axhline(70, color='r')
	ax2.axhline(30, color='g')
	ax2.set_yticks([70, 30])
	plt.show()

chartData()



