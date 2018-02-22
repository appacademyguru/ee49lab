import json

# on esp32
def data2string(**args): # ** converts args to dict
    string = json.dumps(args) #json.dumps converts dict to string
    return string

#on host
def string2data(string):
    data = json.loads(string) #convert back to dict
    return data

msg = data2string(t=1.5, v=3, i=2)

#mqtt.publish('data', msg)
data = string2data(msg) #send string from esp32 to host with mqtt
