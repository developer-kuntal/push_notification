import time
import pymongo
from datetime import datetime
from pushbullet import PushBullet
import pywifi_status as pc
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

API_KEY = os.environ.get("API_KEY")

# print("API_KEY: ",API_KEY)

load_dotenv()

# API_KEY = "o.N4KmL9XRnbLeVVDmu8IEOSLtvwlxo3e5"

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["login_status"]
mycol = mydb["status"]

# previous_login_time = mycol.find_one("last_login", sort=[( '_id', pymongo.DESCENDING )])
wr = mycol.find({}).sort("_id",-1).limit(1)
for login in wr:
    previous_login = login['last_login']
    break
# print(previous_login)
# print(previous_login_time)
#Inserting document into a collection


now = datetime.now() # current date and time

format = '%d-%b-%Y %I:%M %p'
date_time = now.strftime(format)
# print("date and time:",date_time)

doc1 = {"last_login": date_time}
mycol.insert_one(doc1)

sendMessage = f" [From PushBullet] - Your PC has been started at {date_time}.\n\nLast login at: {previous_login}"

appendMessage = f'Windows is starting at {date_time}'
appendFile = open(r'C:\Users\kunta\Desktop\statusLog.txt', 'a')
appendFile.write(appendMessage)
appendFile.write('\n')
appendFile.close()

while True:
    
    if pc.hasconnection():
        pb = PushBullet(API_KEY)
        push = pb.push_note("Hello Shivarul (শিবারুল)", sendMessage)
        break
    else:
        time.sleep(3*60)