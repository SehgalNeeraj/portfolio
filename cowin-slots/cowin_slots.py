# uses public cowin app api's
# https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict
# Outputs : Puts slots in csv for entire Delhi (next 7 days) for 18+ age vaccination

import json
import requests
from datetime import *
myDate = date.today().strftime('%d-%m-%Y')
delhiDistricts = ['140', '141', '142', '143',
                  '144', '145', '146', '147', '148', '149', '150']

public_api = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict'
delimit = ","
dataDict = ()

header = "Vaccine"+delimit+"Hospital"+delimit+"Location"+delimit + \
    "Pin Code"+delimit+"Fees"+delimit+"Age"+delimit+"Av. Slots"+delimit+"Date"+"\n"
handle = open("cowin_slots.csv", "w+")
handle.write(header)

for district in delhiDistricts:
    resp = requests.get(public_api, params={
                        'district_id': district, 'date': myDate})
    if (resp.status_code == 200):  # OK
        dataDict = resp.json()
        center_list = dataDict["centers"]

        for center in center_list:
            name = center["name"]
            district = center["district_name"]
            pincode = center["pincode"]
            fee_type = center["fee_type"]
            session_list = center["sessions"]
            for session in session_list:
                min_age = session['min_age_limit']
                capacity = session['available_capacity']
                av_date = session['date']
                vaccine = session['vaccine']

            if (min_age == 18):  # and capacity > 0):
                content = str(vaccine)+delimit+str(name)+delimit+str(district)+delimit+str(pincode) + \
                    delimit+str(fee_type)+delimit+str(min_age) + \
                    delimit+str(capacity)+delimit+str(av_date)+"\n"
                handle.write(content)
    else:
        continue  # NOT OK

handle.close()    
