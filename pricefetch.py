import requests
import json
import csv
from collections import deque
import time
import datetime

def getsince(csv_file):
    with open(csv_file,'r') as f:
        return deque(csv.reader(f),1)[0][0]


def getprices():
        
        #urlbfx='https://api.bitfinex.com/v2/candles/trade:1m:tLTCBTC/hist'
        #file='Bitfinex1minLTCBTC.csv'

        urlbfx='https://api.bitfinex.com/v2/candles/trade:1m:tBTCUSD/hist'
        file='Data\BitfinexBTCUSD.csv'
        
        
        params = {'limit':1000, 'sort':1}
        response = requests.get(urlbfx, params=params)

        bfxjson = json.loads(response.text)
        bfxohlc = []

        for i in range(0, len(bfxjson)):
                appendline=bfxjson[i][0]/1000,bfxjson[i][1],bfxjson[i][3],bfxjson[i][4],bfxjson[i][2],bfxjson[i][5]
                bfxohlc.append(appendline)
        with open(file,'a',newline='') as f:
                writer = csv.writer(f)
                writer.writerows(bfxohlc)

        #print(bfxohlc)
        


        '''
        start = (float(getsince(file))+60)*1000
        now = int(datetime.datetime.timestamp(datetime.datetime.now()))
        datevalue = datetime.datetime.utcfromtimestamp(start/1000).replace(tzinfo=datetime.timezone.utc)
        print('last:', datevalue)
        
        limit = 10000
        count = 0
        
        while count < limit:
                params = {'limit':1000, 'start':start, 'sort':1}

                try:
                    response = requests.get(urlbfx, params=params)

                    bfxjson = json.loads(response.text)
                    bfxohlc = []

                    for i in range(0, len(bfxjson)):
                            appendline=bfxjson[i][0]/1000,bfxjson[i][1],bfxjson[i][3],bfxjson[i][4],bfxjson[i][2],bfxjson[i][5]
                            bfxohlc.append(appendline)
                    with open(file,'a',newline='') as f:
                            writer = csv.writer(f)
                            writer.writerows(bfxohlc)
                    start = (float(getsince(file))+60)*1000
                    datevalue = datetime.datetime.utcfromtimestamp(start/1000).replace(tzinfo=datetime.timezone.utc)
                    print(count+1)
                    print('last:', datevalue)
                    count += 1
                    time.sleep(5)    
                except Exception as e:
                    continue
                if start/1000 >= now:
                    break  
        '''          
        
getprices()
