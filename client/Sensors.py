# File Name: Sensors.py
# Summary: This file contains the functions printValue, formatValue, getTemperature, 
# getVoltage, getCurrent, getHumidity, getPressure.
# Description: This file obtains formated values of each component of the system. 
# Author: David Saraguro Fárez.
# Last Modified: 06-05-2022
import random

# Main Class:
class Sensors():
    def __init__(self, sensor_id) -> None:
        self.name=sensor_id



    # Function Name: printValue
    # Description: print the values.
    # Parameters: None
    # Returns: None

    def printValue(self):
        print ("printing info of", self.name)



    # Function Name: formatValue
    # Description: Assign a format to the value.
    # Parameters: value
    # Returns: formated values
    def formatValue(self,value):
        formatted_value= round(value, 2)
        return formatted_value

#Each of the following classes extends from the main class.
#Also returns a value within a specified range.

#RADIOBASE SENSORS
class SensorTemperatureRB(Sensors):



    # Function Name: getTemperature
    # Description: Generates values for temperature.
    # Parameters: None
    # Returns: Value

    def getTemperature(self):
        random_temp=random.randint(0, 56)
        val=self.formatValue(random_temp)
        return val


class SensorVoltageRB(Sensors):



    # Function Name: getVoltage
    # Description: Generates values for voltage.
    # Parameters: None
    # Returns: Value

    def getVoltage(self):
        random_voltage=random.randint(-58, -47)
        val=self.formatValue(random_voltage)
        return val


class SensorCurrentRB(Sensors):
    


    # Function Name: getCurrent
    # Description: Generates values for current.
    # Parameters: None
    # Returns: Value

    def getCurrent(self):
        random_current=random.randint(7, 11)
        val=self.formatValue(random_current)
        return val


class SensorHumidityRB(Sensors):
    


    # Function Name: getHumidity
    # Description: Generates values for humidity
    # Parameters: None
    # Returns: Value

    def getHumidity(self):
        random_humidity=random.randint(4, 101)
        val=self.formatValue(random_humidity)
        return val


class SensorPressureRB(Sensors):
    


    # Function Name: getPressure
    # Description: Generates values for pressure.
    # Parameters: None
    # Returns: Value

    def getPressure(self):
        random_pressure=random.randint(69, 107)
        val=self.formatValue(random_pressure)
        return val

#PVS SENSORS
class SensorTemperatureSFV(Sensors):



    # Function Name: getTemperature
    # Description: Generates values for temperature.
    # Parameters: None
    # Returns: Value

    def getTemperature(self):
        random_temp=random.randint(0, 45)
        val=self.formatValue(random_temp)
        return val


class SensorVoltageSFV(Sensors):
    


    # Function Name: getVoltage
    # Description: Generates values for voltage.
    # Parameters: None
    # Returns: Value

    def getVoltage(self):
        random_voltage=random.randint(-58, -47)
        val=self.formatValue(random_voltage)
        return val


class SensorCurrentSFV(Sensors):
    


    # Function Name: getCurrent
    # Description: Generates values for current.
    # Parameters: None
    # Returns: Value
    
    def getCurrent(self):
        random_current=random.randint(7, 11)
        val=self.formatValue(random_current)
        return val


if __name__ == '__main__':
    print ("hola de sensores")