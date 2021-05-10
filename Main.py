import requests
from requests.structures import CaseInsensitiveDict
from datetime import date
from time import sleep 



browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
today = date.today()
date = today.strftime("%d-%m-2021")

URL =('https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByPin?pincode=786602&date='+date)
response = requests.get(URL, headers=browser_header)
doc=response.text
count=0
while True:

    
        for data in response.json()['centers']:
            for datac in data ['sessions']:
                lm=(datac['available_capacity']),
                pin=(data['pincode']),
                name=(data['name'])
                dk=(data['center_id'])
                # if available_
                x= lm[0]
                count += 1
                if x >0:
                    print(str(dk) + " " + 'Vaccine Slot  Available' + " at" + name )
                    sendmessage('8638257752',"Slot Available")
                elif x == 0:
                     print("Tracked " + str(count)+ " time of center id " +str(dk) + " " + 'Vaccine slot Not  available' + " " + name )
                     sleep(2)
                else:
                     print('not found')




