import geocoder
import socket
from whatsmyip.ip import get_ip
from whatsmyip.providers import GoogleDnsProvider
import netifaces as ni


def getMyComputerAddress():
    try:
        hostname = socket.gethostname()
        IPAddress = get_ip(GoogleDnsProvider)
        interfaces = ni.interfaces()
        #ni.ifaddresses('en0')
        ip1 = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']
        ip2 = ni.ifaddresses('lo0')[ni.AF_INET][0]['addr']
        g = geocoder.ip('me')
        location = g.latlng
        print(interfaces)

        print(
            "-----------------------------------------------------------------------------------------------------------")

        print("Your Computer name is:", hostname, " And Localhost Address is:", ip2)
        print("Your local IP Address is:", ip1)
        print("Your External IP Address is:", IPAddress)
        print("Your location is(Latitude, Longitude:)", location)
    except:
        print("Unable to fetch details")


getMyComputerAddress()
