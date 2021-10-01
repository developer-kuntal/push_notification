from datetime import datetime
from pushbullet import PushBullet
import pywifi_status as pc

API_KEY = "o.N4KmL9XRnbLeVVDmu8IEOSLtvwlxo3e5"

now = datetime.now() # current date and time

format = '%d-%b-%Y %I:%M %p'
date_time = now.strftime(format)
# print("date and time:",date_time)

sendMessage = f" from pushBullet your PC has been started at {date_time}"

appendMessage = f'Windows is starting at {date_time}'
appendFile = open(r'C:\Users\kunta\Desktop\statusLog.txt', 'a')
appendFile.write(appendMessage)
appendFile.write('\n')
appendFile.close()

while True:
    if pc.hasconnection():
        pb = PushBullet(API_KEY)
        push = pb.push_note("Hello Shivarul", sendMessage)
        break