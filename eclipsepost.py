

#  Class to manage requests
import requests
#  Class to decode string
import base64
#  Class required to convert text retrieved into a dic
import json

url='http://localhost/bridgelink'

# INIT VARIABLES  MACHINE REGISTRATION

myjson = { "func":"session_connect",
"licenseid":"ADHC344427554",
"machineid":"344427554",
"passhash":"Sb2/wYHIHhsgEAPKOdibBD4u1gP2z8S",
"sessionid":"LANTEST",
"email":"",
"username":"" }

conn = requests.post(url, json = myjson)
print(f"*****Operation Result:  {conn.text}")



# INIT VARIABLES  FOR SESSION

myjasonsess = {"func":"update",
"licenseid":"ADHC344427554",
"machineid":"344427554",
"sessionid":" LANTEST ",
"streampos":"795",
"email":"",
"username":""}


# Polled  string encode base64
connsess = requests.post(url, json = myjasonsess)
#print(f"******Encoded String:  {connsess.text}")
#print("The type of resulted string is: "  type(connsess.text))



# Decode base64 string --  Check if encode ascii is required ..if not use directly
#  b64dcode method

#base64_string = conn.text
#base64_bytes = base64_string.encode("ascii")
#decoded_frameset = base64.b64decode(base64_bytes)


decoded_frameset = base64.b64decode(conn.text)
sample_string = decoded_frameset.decode("ascii").encode("utf-8")

print(f"Decoded string: {sample_string}")
