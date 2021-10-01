import pywifi
import time
from pywifi import const

def hasconnection():
    status = False
    wifi = pywifi.PyWiFi() # Create a Object

    Iface = wifi.interfaces()[0]
    Name = Iface.name()

    Iface.scan()
    time.sleep(1)

    results = Iface.scan_results()
    for data in results:
        # print(data.ssid) # AndroidAP
        if Iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE] :
            # print("network card disconected...")
            break
        else:
            # print("network card is connected...")
            status = True
            break
    return status

if __name__ == "__main__":
    print(hasconnection())