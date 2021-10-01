import time;

localtime = time.asctime( time.localtime(time.time()) )
appendMessage = f'Windows is starting at {localtime}'

appendFile = open(r'C:\Users\kunta\Desktop\statusLog.txt', 'a')

appendFile.write(appendMessage)
appendFile.write('\n')