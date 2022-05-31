# File Name: app.py
# Summary: This file consists of the following functions:
# validate_data, setAalarm, storeStatus, index, base, base_info.
# Description: This file documents the validation of each parameter that is monitored in 
# the radiobase and the photovoltaic system.
# Author: David Saraguro Fárez.
# Last Modified: 06-05-2022

'''
MIT License

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
SOFTWARE.
'''


from flask import Flask, jsonify, request
from Alarm import Alarm
from StorangeController import StatusSC


class ServerEngine():

    def __init__(self) -> None:
        self.myAlarm=Alarm()
        self.mysc=StatusSC()



    # Function Name: Validate_data
    # Description: Each of the monitored parameters is validated according to its operating range.
    # Parameters: radiobase information, id of each radiobase.
    # Returns: validate data.

    def validate_data(self,radiobase_info,client_id ):
        #validation
        #failures={component:[{faulty sensor} :value]}
        #split radiobase information into individual variables 
        failures={}
        radiobase_dcdutemp=radiobase_info[client_id][0]["RB"]["DCDU"]["temp"]
        radiobase_dcduvolt=radiobase_info[client_id][0]["RB"]["DCDU"]["voltage"]
        radiobase_dcducurr=radiobase_info[client_id][0]["RB"]["DCDU"]["current"]
        radiobase_dcduhum=radiobase_info[client_id][0]["RB"]["DCDU"]["humidity"]
        radiobase_dcdupress=radiobase_info[client_id][0]["RB"]["DCDU"]["pressure"]
        radiobase_bbutemp=radiobase_info[client_id][0]["RB"]["BBU"]["temp"]
        radiobase_bbuvolt=radiobase_info[client_id][0]["RB"]["BBU"]["voltage"]
        radiobase_bbucurr=radiobase_info[client_id][0]["RB"]["BBU"]["current"]
        radiobase_bbuhum=radiobase_info[client_id][0]["RB"]["BBU"]["humidity"]
        radiobase_bbupress=radiobase_info[client_id][0]["RB"]["BBU"]["pressure"]
        radiobase_rrutemp=radiobase_info[client_id][0]["RB"]["RRU"]["temp"]
        radiobase_rruvolt=radiobase_info[client_id][0]["RB"]["RRU"]["voltage"]
        radiobase_rrucurr=radiobase_info[client_id][0]["RB"]["RRU"]["current"]
        radiobase_rruhum=radiobase_info[client_id][0]["RB"]["RRU"]["humidity"]
        radiobase_rrupress=radiobase_info[client_id][0]["RB"]["RRU"]["pressure"]

        sfv_paneltemp=radiobase_info[client_id][1]["SFV"]["Panel"]["temp"]
        sfv_panelvolt=radiobase_info[client_id][1]["SFV"]["Panel"]["voltage"]
        sfv_panelcurr=radiobase_info[client_id][1]["SFV"]["Panel"]["current"]
        sfv_batterytemp=radiobase_info[client_id][1]["SFV"]["Battery"]["temp"]
        sfv_batteryvolt=radiobase_info[client_id][1]["SFV"]["Battery"]["voltage"]
        sfv_batterycurr=radiobase_info[client_id][1]["SFV"]["Battery"]["current"]
        sfv_controllertemp=radiobase_info[client_id][1]["SFV"]["Controller"]["temp"]
        sfv_controllervolt=radiobase_info[client_id][1]["SFV"]["Controller"]["voltage"]
        sfv_controllercurr=radiobase_info[client_id][1]["SFV"]["Controller"]["current"]

        #Validation ranges for each variable
        print("*********************************************************************************")
        print(" ")
        print("                         RADIOBASE PARAMETERS")
        print("DCDU:")
        print ("   Temperature:", radiobase_dcdutemp,"oC")
        print ("   Voltage:", radiobase_dcduvolt,"V")
        print ("   Current:", radiobase_dcducurr,"A")
        print ("   Humidity:", radiobase_dcduhum,"%RH")
        print ("   Pressure:", radiobase_dcdupress,"kPa")
        #DCDU PARAMETERS
        if radiobase_dcdutemp>55 or radiobase_dcdutemp<-20:
            failures["DCDU"]={"temperature":radiobase_dcdutemp}
        if radiobase_dcduvolt>-38 or radiobase_dcduvolt<-57:   
            failures["DCDU"]={"voltage":radiobase_dcduvolt} 
        if radiobase_dcducurr>10 or radiobase_dcducurr<8: 
            failures["DCDU"]={"current":radiobase_dcducurr} 
        if radiobase_dcduhum>95 or radiobase_dcduhum<5:
            failures["DCDU"]={"humidity":radiobase_dcduhum} 
        if radiobase_dcdupress>106 or radiobase_dcdupress<70:    
            failures["DCDU"]={"preasure":radiobase_dcdupress} 
   

        print("BBU:")
        print ("   Temperature:", radiobase_bbutemp,"oC")
        print ("   Voltage:", radiobase_bbuvolt,"V")
        print ("   Current:", radiobase_bbucurr,"A")
        print ("   Humidity:", radiobase_bbuhum,"%RH")
        print ("   Pressure:", radiobase_bbupress,"kPa")
        #BBU PARAMETERS
        if radiobase_bbutemp>55 or radiobase_bbutemp<-20:
            failures["BBU"]={"temperature":radiobase_bbutemp}
        if radiobase_bbuvolt>-38 or radiobase_bbuvolt<-57:
            failures["BBU"]={"voltage":radiobase_bbuvolt}   
        if radiobase_bbucurr>10 or radiobase_bbucurr<8: 
            failures["BBU"]={"current":radiobase_bbucurr}   
        if radiobase_bbuhum>95 or radiobase_bbuhum<5:
            failures["BBU"]={"humidity":radiobase_bbuhum}    
        if radiobase_bbupress>106 or radiobase_bbupress<70:
            failures["BBU"]={"pressure":radiobase_bbupress}   
            

        print("RRU:")
        print ("   Temperature:", radiobase_rrutemp,"oC")
        print ("   Voltage:", radiobase_rruvolt,"V")
        print ("   Current:", radiobase_rrucurr,"A")
        print ("   Humidity:", radiobase_rruhum,"%RH")
        print ("   Pressure:", radiobase_rrupress,"kPa")
        #RRU PARAMETERS
        if radiobase_rrutemp>50 or radiobase_rrutemp<-40:
            failures["RRU"]={"temperature":radiobase_rrutemp}
        if radiobase_rruvolt>-36 or radiobase_rruvolt<-57: 
            failures["RRU"]={"voltage":radiobase_rruvolt}   
        if radiobase_rrucurr>10 or radiobase_rrucurr<8: 
            failures["RRU"]={"current":radiobase_rrucurr}   
        if radiobase_rruhum>100 or radiobase_rruhum<5:  
            failures["RRU"]={"humidity":radiobase_rruhum}  
        if radiobase_rrupress>106 or radiobase_rrupress<70:  
            failures["RRU"]={"pressure":radiobase_rrupress}  
                
        
        print("*********************************************************************************")
        print("")
        print("                         PHOTOVOLTAIC SYSTEM PARAMETERS")
        print("PANEL:")
        print ("   Temperature:", sfv_paneltemp,"oC")
        print ("   Voltage:", sfv_panelvolt,"V")
        print ("   Current:", sfv_panelcurr,"A")
        #PANEL PARAMETERS
        if sfv_paneltemp>85 or sfv_paneltemp<-40:
            failures["PANEL"]={"temperature":sfv_paneltemp}
        if sfv_panelvolt>-47 or sfv_panelvolt<-51:
            failures["PANEL"]={"voltage":sfv_panelvolt}    
        if sfv_panelcurr>9 or sfv_panelcurr<8: 
            failures["PANEL"]={"current":sfv_panelcurr}   
            

        print("Battery:")
        print ("   Temperature:", sfv_batterytemp,"oC")
        print ("   Voltage:", sfv_batteryvolt,"V")
        print ("   Current:", sfv_batterycurr,"A")
        #BATTERY PARAMETERS
        if sfv_batterytemp>45 or sfv_batterytemp<-20:
            failures["BATTERY"]={"temperature":sfv_batterytemp}
        if sfv_batteryvolt>-46 or sfv_batteryvolt<-51: 
            failures["BATTERY"]={"voltage":sfv_batteryvolt}   
        if sfv_batterycurr>9 or sfv_batterycurr<8:  
            failures["BATTERY"]={"current":sfv_batterycurr}  
            

        print("CONTROLLER:")
        print ("   Temperature:", sfv_controllertemp,"oC")
        print ("   Voltage:", sfv_controllervolt,"V")
        print ("   Current:", sfv_controllercurr,"A")
        #CONTROLLER PARAMETERS
        if sfv_controllertemp>40 or sfv_controllertemp<0:
            failures["CONTROLLER"]={"temparature":sfv_controllertemp}
        if sfv_controllervolt>-46 or sfv_controllervolt<-49:  
            failures["CONTROLLER"]={"voltage":sfv_controllervolt}  
        if sfv_controllercurr>10 or sfv_controllercurr<0: 
            failures["CONTROLLER"]={"current":sfv_controllercurr}    
                    
        self.setAlarm(failures,client_id) #set alarm based on detected failures
        self.storeStatus(radiobase_info,client_id) #store radiobase status irrespective of failures

   
   
    # Function Name: setAlarm
    # Description: configuration of generated alarms.
    # Parameters: generated failures, id of each radiobase.
    # Returns: None

    def setAlarm(self, failures,client_id):
        self.myAlarm.set_alarm(failures,client_id)
       
    
    
    # Function Name: storeStatus
    # Description: storage of radiobase status
    # Parameters: radiobase information, id of each radiobase.
    # Returns: None

    def storeStatus(self, radio_base_info,client_id):
        self.mysc.storeStatus(radio_base_info,client_id)
        

mySE=ServerEngine()
app = Flask(__name__)

#Home
@app.route("/")



# Function Name: index
# Description: a welcome message is generated.
# Parameters: None
# Returns: Welcome message.

def index():
    return "Welcome to monitorsystem!"
#Endpoint behavior
@app.route("/<client_id>")



# Function Name: base
# Description: get the radiobase id to generate a message.
# Parameters: id of each radiobase.
# Returns: message to register a client.

def base(client_id):
    return "To register client "+str(client_id) +" use a POST method."
#http://127.0.0.1/rbxx

#Endpoint behavior when the user does a POST
@app.route("/<client_id>" , methods=['POST'])



# Function Name: base_info
# Description: a message is generated.
# Parameters: id of each radiobase.
# Returns: message.

def base_info(client_id):

    radiobase_info=request.get_json()
    #print (radiobase_info)
    
    mySE.validate_data(radiobase_info,client_id)


    return "Request for "+str(client_id)+" succesful"

if __name__ == '__main__':
    app.run(debug=True)    


    