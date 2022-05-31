# File Name: MainClient.py
# Summary: This file consists of the function getSistemParameters.
# Description: The system parameters are obtained and the client 
# information is sent to the server.
# Author: David Saraguro Fárez.
# Last Modified: 06-05-2022

'''MIT License

Copyright (c) 2022 David Saraguro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

from RB import RB
from SFV import SFV
import requests
import json

myRB=RB()
mySFV=SFV()

class Cliente():
    def __init__(self) -> None:
        self.myRB=RB()
        self.mySFV=SFV()



    # Function Name: getSystemParameters
    # Description: Get system parameters.
    # Parameters: None
    # Returns: Radiobase and photovoltaic system parameters.

    def getSystemParameters(self):
        response=self.myRB.getRBParameters()
        response=self.mySFV.getSFVParameters()
        return response
    

client_dict={}
c_list=[]

a= (myRB.getRBParameters())
b= (mySFV.getSFVParameters())

c_list.append(a)
c_list.append(b)
client_id="rb15"
client_dict[client_id]=c_list
headers = {'Content-type': 'application/json', 'Accept': '*/*'}
url="http://127.0.0.1:5000/"+str(client_id)
response_gotten = requests.post(url, data=json.dumps(client_dict),headers=headers)
#The data stored on the server is printed
print (client_dict)
print ("Response from server: ", response_gotten)
#response_json=response_gotten.json()
#response=response_json
            
print(client_dict)

