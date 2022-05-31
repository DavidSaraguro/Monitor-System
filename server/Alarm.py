# File Name: Alarm.py
# Summary: This file consists of the function set_alarm
# Description: In this file the Alarm class is created, where 
# the format of the message is defined.
# Author: David Saraguro Fárez.
# Last Modified: 06-05-2022

from NotificationManager import EmailNotifier
from StorangeController import AlarmSC

class Alarm():
    def __init__(self) -> None:
        self.email_notifier=EmailNotifier()
        self.failure_rb={}
        self.storageController=AlarmSC()



    # Function Name: set_alarm
    # Description: configure, send and store failures.
    # Parameters: failures and client id.
    # Returns: None

    def set_alarm(self,failures,client_id):

        if failures:
            print("----------------------------------------------------------------------------------")
            print("")
            print ("FAILURES IN SYSTEM: ", client_id, "--> ", failures)
            # for failure in failures:
            #     print(failures[failure])
        self.failure_rb[client_id]=failures
        #store in DB
        #notify email
        self.email_notifier.send_email(self.failure_rb)
        self.store_alarm(client_id, failures)



    # Function Name: store_alarm
    # Description: Obtains the id of the radiobase and the failure data.
    # Parameters: RB_ID and data_failures.
    # Returns: None

    def store_alarm(self,RB_ID,data_failures):
        self.storageController.storeAlarm(RB_ID,data_failures)


if __name__ == '__main__':
    myAlarm=Alarm()
    failures={'DCDU': {'current': 0, "voltage":0}, 'BBU': {'humidity': 99}, 
                'RRU': {'current': 11}, 'PANEL': {'voltage': -57}, 
                'BATTERY': {'current': 7}, 'CONTROLLER': {'voltage': -56}}
    myAlarm.set_alarm(failures, "rb01")     
