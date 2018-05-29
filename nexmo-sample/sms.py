import nexmo
from djexmo import send_message
import random
import  firebase_admin
# import time
import json
import pyrebase
from firebase_admin import credentials
import pytz
from datetime import datetime, timezone
import base64


config = {
  "apiKey": "AIzaSyCwy2DSVWgniTi2PRbHlDKvF58dzE5LhmY",
  "authDomain": "thesisbpms-af272.firebaseapp.com",
  "databaseURL": "https://thesisbpms-af272.firebaseio.com",
  "projectId": "thesisbpms-af272",
  "storageBucket": "thesisbpms-af272.appspot.com",
  "messagingSenderId": "789763107091",
  }

firebase = pyrebase.initialize_app(config)

print("firebase initialized")
db= firebase.database()



def sendSMS(bplevel):
  print("in send sms")
  if (bplevel==2):
      print("pre-hypertensive")
      response = client.send_message({'from': 'Python', 'to': +639239744710, 'text': 'pre-hypertensive state'})

  elif(bplevel==3):
      print("critical")
      response = client.send_message({'from': 'Python', 'to': +639239744710, 'text': 'critical state'})

    # this part just prints in console
  # response = response['messages'][0]
  # if response['status'] == '0':
  #   print ('Sent message')
  # else:
  #   print ('Error:')
  pass

def values(age, syst, dias):
  print("inside values")
    # syst = db.child("users").child("patient").child("docID").child("pID").child("BP_Measurements").child("bpDateTime").child("syst").get().val();
    # dias =  db.child("users").child("patient").child("docID").child("pID").child("BP_Measurements").child("bpDateTime").child("dias").get().val();

  if (20<=age<=24):
    print("20 to 24")
    if(((syst)<=119)):
        if(((dias)<=78)):
            print("normal bp level")
            bpLevel = 1
        elif((79<=(dias)<=81)):
            print("borderline bp level")
            bpLevel = 2
        elif((82<=(dias)<=100)):
            print("critical bp level")
            bpLevel = 3
    elif((120<=(syst)<=124)):
        if((79<=(dias)<=81)):
            print("borderline bp level")
            bpLevel = 2
        elif((82<=(dias)<=100)):
            print("critical bp level")
            bpLevel = 3
    elif((125<=(syst)<=150)):
        print("critical bp level")
        bpLevel = 3

  elif (25<=age<=29):
    print("25 to 29")
    if(((syst)<=120)):
        if(((dias)<=79)):
            print("normal bp level")
            bpLevel = 1
        elif((80<=(dias)<=82)):
            print("borderline bp level")
            bpLevel = 2
        elif((83<=(dias)<=100)):
            print("critical bp level")
            bpLevel = 3
    elif((121<=(syst)<=131)):
        if((80<=(dias)<=82)):
            print("borderline bp level")
            bpLevel = 2
        elif((83<=(dias)<=100)):
            print("critical bp level")
            bpLevel = 3
    elif((132<=(syst)<=150)):
        print("critical bp level")
        bpLevel = 3

  elif (30<=age<=34):
    print("30 to 34")
    if(((syst)<=121)):
        if(((dias)<=80)):
            print("normal bp level")
            bpLevel = 1
        elif((81<=(dias)<=84)):
            print("borderline bp level")
            bpLevel = 2
        elif((85<=(dias)<=100)):
            print("critical bp level")
            bpLevel = 3
    elif((122<=(syst)<=133)):
        if((81<=(dias)<=84)):
            print("borderline bp level")
            bpLevel = 2
        elif((85<=(dias)<=100)):
            print("critical bp level")
            bpLevel = 3
    elif((134<=(syst)<=160)):
        print("critical bp level")
        bpLevel = 3

  elif (35<=age<=39):
    print("35 to 39")
    if(((syst)<=122)):
        if((float(dias)<=81)):
            print("normal bp level")
            bpLevel = 1
        elif((82<=(dias)<=95)):
            print("borderline bp level")
            bpLevel = 2
        elif((86<=(dias)<=101)):
            print("critical bp level")
            bpLevel = 3
    elif((123<=(syst)<=134)):
        if((82<=(dias)<=85)):
            print("borderline bp level")
            bpLevel = 2
        elif((86<=(dias)<=101)):
            print("critical bp level")
            bpLevel = 3
    elif((135<=(syst)<=162)):
        print("critical bp level")
        bpLevel = 3

  elif (40<=age<=44):
    print("40 to 44")
    if(((syst)<=124)):
        if(((dias)<=82)):
            print("normal bp level")
            bpLevel = 1
        elif((83<=(dias)<=86)):
            print("borderline bp level")
            bpLevel = 2
        elif((87<=(dias)<=102)):
            print("critical bp level")
            bpLevel = 3
    elif((125<=(syst)<=136)):
        if((83<=(dias)<=86)):
            print("borderline bp level")
            bpLevel = 2
        elif((87<=(dias)<=102)):
            print("critical bp level")
            bpLevel = 3
    elif((137<=(syst)<=164)):
        print("critical bp level")
        bpLevel = 3

  elif (45<=age<=49):
    print("45 to 49")
    if(((syst)<=126)):
        if(((dias)<=83)):
            print("normal bp level")
            bpLevel = 1
        elif((84<=(dias)<=87)):
            print("borderline bp level")
            bpLevel = 2
        elif((88<=(dias)<=103)):
            print("critical bp level")
            bpLevel = 3
    elif((127<=(syst)<=138)):
        if((84<=(dias)<=87)):
            print("borderline bp level")
            bpLevel = 2
        elif((88<=(dias)<=103)):
            print("critical bp level")
            bpLevel = 3
    elif((139<=(syst)<=166)):
        print("critical bp level")
        bpLevel = 3

  elif (50<=age<=54):
    print("50 to 54")
    if(((syst)<=128)):
        if(((dias)<=84)):
            print("normal bp level")
            bpLevel = 1
        elif((85<=(dias)<=88)):
            print("borderline bp level")
            bpLevel = 2
        elif((89<=(dias)<=104)):
            print("critical bp level")
            bpLevel = 3
    elif((129<=(syst)<=140)):
        if((85<=(dias)<=88)):
            print("borderline bp level")
            bpLevel = 2
        elif((89<=(dias)<=104)):
            print("critical bp level")
            bpLevel = 3
    elif((141<=(syst)<=168)):
        print("critical bp level")
        bpLevel = 3

  elif (55<=age<=59):
    print("55 to 59")
    if(((syst)<=130)):
        if(((dias)<=85)):
            print("normal bp level")
            bpLevel = 1
        elif((86<=(dias)<=89)):
            print("borderline bp level")
            bpLevel = 2
        elif((90<=(dias)<=105)):
            print("critical bp level")
            bpLevel = 3
    elif((131<=(syst)<=142)):
        if((86<=(dias)<=89)):
            print("borderline bp level")
            bpLevel = 2
        elif((90<=(dias)<=105)):
            print("critical bp level")
            bpLevel = 3
    elif((143<=(syst)<=170)):
        print("critical bp level")
        bpLevel = 3

  elif (age>=60):
    print("above 60")
    if(((syst)<=133)):
        if(((dias)<=86)):
            print("normal bp level")
            bpLevel = 1
        elif((87<=(dias)<=90)):
            print("borderline bp level")
            bpLevel = 2
        elif((91<=(dias)<=106)):
            print("critical bp level")
            bpLevel = 3
    elif((134<=(syst)<=145)):
        if((87<=(dias)<=90)):
            print("borderline bp level")
            bpLevel = 2
        elif((91<=(dias)<=106)):
            print("critical bp level")
            bpLevel = 3
    elif((146<=(syst)<=173)):
        print("critical bp level")
        bpLevel = 3

  sendSMS(bpLevel);


client = nexmo.Client(key='bf084840', secret='xph8KbjJTslVDXs4')
age = random.randint(20,80)
print("age: ", age)
syst = random.randint(50,150)
print("systolic: ", syst)
dias = random.randint(50,80)
print ("diastolic", dias)

values(age, syst, dias);


