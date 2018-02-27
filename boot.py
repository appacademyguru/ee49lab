from network import WLAN, STA_IF
from network import mDNS, telnet
import time
from machine import RTC

wlan = WLAN(STA_IF)
wlan.active(True)

# wlan.connect('DESKTOP-F42IOJR 8967', '285F>6e3', 5000)
# wlan.connect('EECS-PSK', 'Thequickbrown', 5000)
wlan.connect('NETGEAR84', 'pr@ba6u2hka~', 5000)
while not wlan.isconnected():
    print("Waiting for wlan connection")
    time.sleep(1)

print("WiFi connected at", wlan.ifconfig()[0])

try:
    hostname = 'wigglesby'
    mdns = mDNS(wlan)
    mdns.start(hostname, "MicroPython REPL")
    mdns.addService('_repl', '_tcp', 23, hostname)
    print("Advertised locally as {}.local".format(hostname))
except OSError:
    print("Failed starting mDNS server - already started?")

print("start telnet server")
telnet.start(user='bam', password='cowabunga')

print("inquire RTC time")
rtc = RTC()
rtc.ntp_sync(server="pool.ntp.org")

timeout = 5
for _ in range(5):
    if rtc.synced():
        break
    time.sleep(1)

if rtc.synced():
    print(time.strftime("%c", time.localtime()))
else:
    print("cannot get NTP time")
