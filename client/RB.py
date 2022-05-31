# File Name: RB.py
# Summary: This file contains the functions getdcduParameters, getbbuParameters, 
# getrruParameters, getRBParameters, getParameters.
# Description:  In this file the information of each component of the RB is obtained.
# Author: David Saraguro Fárez.
# Last Modified: 06-05-2022

import Sensors

class RB():

    def __init__(self) -> None:
        self.dcdu=dcdu()
        self.bbu=bbu()
        self.rru=rru()



    # Function Name: getdcduParameters
    # Description: Obtains the information of all parameters monitored in the DCDU.
    # Parameters: None
    # Returns: data of DCDU.

    def getdcduParameters(self):
        response=self.dcdu.getParameters()
        return response



    # Function Name: getbbuParameters
    # Description: Obtains the information of all parameters monitored in the BBU.
    # Parameters: None
    # Returns: data of BBU.

    def getbbuParameters(self):
        response=self.bbu.getParameters()
        return response



    # Function Name: getrruParameters
    # Description: Obtains the information of all parameters monitored in the RRU.
    # Parameters: None
    # Returns:data of RRU.

    def getrruParameters(self):
        response=self.rru.getParameters()
        return response



    # Function Name: getRBParameters
    # Description: Obtains the information of all parameters monitored in the radiobase.
    # Parameters: None
    # Returns: data of radiobase.

    def getRBParameters(self):
        parameters={}
        RB={}
        responsedcdu=self.getdcduParameters()
        responsebbu=self.getbbuParameters()
        responserru=self.getrruParameters()


        parameters["DCDU"]=responsedcdu
        parameters["BBU"]=responsebbu
        parameters["RRU"]=responserru
        RB["RB"]=parameters
        return RB


class dcdu():
    def __init__(self) -> None:
        self.temperature=Sensors.SensorTemperatureRB("tdcdu1")
        self.voltage=Sensors.SensorVoltageRB("vdcdu1")
        self.current=Sensors.SensorCurrentRB("cdcdu1")
        self.humidity=Sensors.SensorHumidityRB("hdcdu1")
        self.pressure=Sensors.SensorPressureRB("pdcdu1")



    # Function Name: getParameters
    # Description: Obtains the information of all parameters monitored in the Radiobase and photovoltaic system.
    # Parameters: None
    # Returns: Return a dictionary.

    def getParameters(self):
       # print ("Calling from DCDU")
        
        return {"temp":self.temperature.getTemperature(), "voltage": self.voltage.getVoltage(), "current": self.current.getCurrent(), "humidity": self.humidity.getHumidity(), "pressure": self.pressure.getPressure()}



class bbu():
    def __init__(self) -> None:
        self.temperature=Sensors.SensorTemperatureRB("tbbu1")
        self.voltage=Sensors.SensorVoltageRB("vbbu1")
        self.current=Sensors.SensorCurrentRB("cbbu1")
        self.humidity=Sensors.SensorHumidityRB("hbbu1")
        self.pressure=Sensors.SensorPressureRB("pbbu1")



    # Function Name: getParameters
    # Description: Obtains the information of all parameters monitored in the Radiobase and photovoltaic system.
    # Parameters: None
    # Returns: Return a dictionary.

    def getParameters(self):
       # print ("Calling from BBU")
        
        return {"temp":self.temperature.getTemperature(), "voltage": self.voltage.getVoltage(), "current": self.current.getCurrent(), "humidity": self.humidity.getHumidity(), "pressure": self.pressure.getPressure()}        



class rru():
    def __init__(self) -> None:
        self.temperature=Sensors.SensorTemperatureRB("trru1")
        self.voltage=Sensors.SensorVoltageRB("vrru1")
        self.current=Sensors.SensorCurrentRB("crru1")
        self.humidity=Sensors.SensorHumidityRB("hrru1")
        self.pressure=Sensors.SensorPressureRB("prru1")



    # Function Name: getParameters
    # Description: Obtains the information of all parameters monitored in the Radiobase and photovoltaic system.
    # Parameters: None
    # Returns: Return a dictionary.
    
    def getParameters(self):
       # print ("Calling from RRU")
        
        return {"temp":self.temperature.getTemperature(), "voltage": self.voltage.getVoltage(), "current": self.current.getCurrent(), "humidity": self.humidity.getHumidity(), "pressure": self.pressure.getPressure()}




if __name__ == '__main__':

    obj= RB()
    print(obj.getRBParameters())
