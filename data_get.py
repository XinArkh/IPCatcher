def getcountry(responseJson):
    return responseJson.get("country_name")

def getcountry_code(responseJson):
    return responseJson.get("country_code")

def getlatitude(responseJson):
    return responseJson.get("latitude")

def getlongitude(responseJson):
    return responseJson.get("longitude")

# print(getlatitude("183.186.4.197"))