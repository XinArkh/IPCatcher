import json
from urllib.request import urlopen

def pretreatment(ipAddress):
    priUrl = "http://freegeoip.net/json/"
    response = urlopen(priUrl + ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson