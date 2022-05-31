# File Name: SFV.py
# Summary: This file contains the functions getPanelParameters, getControllerParameters, 
# getBatteryParameters, getSFVParameters, getParameters.
# Description: This file obtains the parameters of each component of the photovoltaic system. 
# Author: David Saraguro Fárez.
# Last Modified: 03-05-2022
import Sensors

#Communication of each component with the getParameters method to obtain the information:
class SFV():
    def __init__(self) -> None:
        self.panel=Panel()
        self.battery=Battery()
        self.controller=Controller()



    # Function Name: getPanelParameters
    # Description: Obtains the information of all parameters monitored in the panel.
    # Parameters: None
    # Returns: data of panel.

    def getPanelParameters(self):
        response=self.panel.getParameters()
        return response



    # Function Name: getControllerParameters
    # Description: Obtains the information of all parameters monitored in the controller.
    # Parameters: None
    # Returns: data of controller.

    def getControllerParameters(self):
        response=self.controller.getParameters()
        return response



    # Function Name: getBatteryParameters
    # Description: Obtains the information of all parameters monitored in the battery.
    # Parameters: None
    # Returns: data of battery

    def getBatteryParameters(self):
        response=self.battery.getParameters()
        return response



    # Function Name: getSFVParameters
    # Description: Obtains the information of all parameters monitored in the photovoltaic system.
    # Parameters: None
    # Returns: data of photovoltaic system.

    def getSFVParameters(self):
        parameters={}
        SFV={}
        responsePanel=self.getPanelParameters()
        responseBattery=self.getBatteryParameters()
        responseController=self.getControllerParameters()
    
    #JSON format: key and value
        parameters["Panel"]=responsePanel
        parameters["Battery"]=responseBattery
        parameters["Controller"]=responseController
        SFV["SFV"]=parameters
        return SFV


#In the following classes the methods of each variable implemented in the file Sensors are called.
class Panel():
    def __init__(self) -> None:
        self.temperature=Sensors.SensorTemperatureSFV("tp1")
        self.voltage=Sensors.SensorVoltageSFV("vp1")
        self.current=Sensors.SensorCurrentSFV("cp1")



    # Function Name: getParameters
    # Description: Obtains the information of all parameters monitored in the Radiobase and photovoltaic system.
    # Parameters: None
    # Returns: Return a dictionary.

    def getParameters(self):
       # print ("Calling from Panel")
        
        return {"temp":self.temperature.getTemperature(), "voltage": self.voltage.getVoltage(), "current": self.current.getCurrent()}




class Battery():
    def __init__(self) -> None:
        self.temperature=Sensors.SensorTemperatureSFV("tb1")
        self.voltage=Sensors.SensorVoltageSFV("vb1")
        self.current=Sensors.SensorCurrentSFV("cb1")



    # Function Name: getParameters
    # Description: Obtains the information of all parameters monitored in the Radiobase and photovoltaic system.
    # Parameters: None
    # Returns: Return a dictionary.

    def getParameters(self):
       # print ("Calling from Battery")
        return {"temp":self.temperature.getTemperature(), "voltage": self.voltage.getVoltage(), "current": self.current.getCurrent()}




class Controller():
    def __init__(self) -> None:
        self.temperature=Sensors.SensorTemperatureSFV("tc1")
        self.voltage=Sensors.SensorVoltageSFV("vc1")
        self.current=Sensors.SensorCurrentSFV("cc1")




    # Function Name: getParameters
    # Description: Obtains the information of all parameters monitored in the Radiobase and photovoltaic system.
    # Parameters: None
    # Returns: Return a dictionary.

    def getParameters(self):
       # print ("Calling from Controller")
        return {"temp":self.temperature.getTemperature(), "voltage": self.voltage.getVoltage(), "current": self.current.getCurrent()}



if __name__ == '__main__':

    obj= SFV()
    print(obj.getSFVParameters())

