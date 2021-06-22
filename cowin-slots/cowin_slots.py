#!/usr/bin/env python3

# uses public cowin app api's
from cowin_config import *
import requests
import datetime
from hashlib import sha256


def generate_otp(phone_number):
    url = "https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP"
    headers = {'.authority': 'cdn-api.co-vin.in', 'accept-Language': 'en_US', 'accept': 'application/json',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    body = {"mobile": "%s" % phone_number}

    response_object = requests.post(url, json=body, headers=headers)
    response = response_object.json()
    return response['txnId']


myDate = (datetime.date.today()).strftime('%d-%m-%Y')
# myDate = datetime.date(2021, 6, 3).strftime('%d-%m-%Y')
dataDict = ()
handle = ""

def openFile():
    try:
        handle = open(
            file_name, "a")
    except Exception as e:
        print("File Error")
        quit()
    return handle

records = 0
content = ""

for code in DISTRICT_ID:
    resp = requests.get(district_api, params={
                        'district_id': code, 'date': myDate}, headers=headers)

    if (resp.status_code != 200):
        handle.write("Bad Response: "+resp.status_code)
        continue  # NOT OK

    # OK to carry On
    dataDict = resp.json()
    center_list = dataDict["centers"]

    for center in center_list:
        
        name = center["name"]
        # id = center['center_id']
        # if (id not in center_ids):
        #     continue

        district = center["district_name"]
        pincode = center["pincode"]
        fee_type = center["fee_type"]
        session_list = center["sessions"]
        fee = 0
        try:
            fee = center["vaccine_fees"][0]["fee"]
        except:
            pass

        for session in session_list:
            min_age = int(session['min_age_limit'])
            vaccine = session['vaccine']

            availability_d1 = session['available_capacity_dose1']
            availability_d2 = session['available_capacity_dose2']
            
            if (min_age != MIN_AGE or vaccine != VACCINE_REQ or availability_d2 < 1):
                continue

            av_date = session['date']

            content += str(vaccine)+delimit+str(name)+delimit+str(district)+delimit+str(pincode) + \
                delimit+str(fee_type)+delimit+str(fee)+delimit+str(min_age) + \
                delimit+str(availability_d1)+delimit+str(availability_d2)+delimit+str(av_date)+"\n"
            records += availability_d2

if (records < 1):
    quit()

handle = openFile()
handle.write(header)
handle.write(content)
handle.close()
