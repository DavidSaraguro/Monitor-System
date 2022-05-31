# File Name: StorageController.py
# Summary: This file contains the functions storeStatus, put_status, storeAlarm, put_alarm.
# Description: In this file, the storage of information on the status and alarms of the RBs is managed. 
# Author: David Saraguro Fárez.
# Last Modified: 06-05-2022

import DBManager

class StatusSC():
    def __init__(self) -> None:
        self._mydbmanager_=DBManager
        self._latest_status_={}



    # Function Name: storeStatus
    # Description: storage of system state information.
    # Parameters: radiobase_info, client_id.
    # Returns: None

    def storeStatus(self, radiobase_info, client_id):
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
        

        self.put_status(client_id,radiobase_dcdutemp, radiobase_dcduvolt, radiobase_dcducurr, radiobase_dcduhum, radiobase_dcdupress, radiobase_bbutemp, radiobase_bbuvolt, radiobase_bbucurr, radiobase_bbuhum, radiobase_bbupress, 
        radiobase_rrutemp, radiobase_rruvolt,  radiobase_rrucurr, radiobase_rruhum, radiobase_rrupress, sfv_paneltemp, sfv_panelvolt, sfv_panelcurr, sfv_batterytemp, sfv_batteryvolt, sfv_batterycurr, sfv_controllertemp, 
        sfv_controllervolt, sfv_controllercurr)



    # Function Name: put_status
    # Description: puts the generated status.
    # Parameters: RB_ID, DCDU_temp, DCDU_volt, DCDU_curr, DCDU_hum, 
    # DCDU_press, BBU_temp, BBU_volt, BBU_curr, BBU_hum, BBU_press, 
    # RRU_temp, RRU_volt, RRU_curr, RRU_hum, RRU_press, PANEL_temp, 
    # PANEL_volt, PANEL_curr, BATTERY_temp, BATTERY_volt, BATTERY_curr, 
    # CONTROLLER_temp, CONTROLLER_volt, CONTROLLER_curr.
    # Returns: None

    def put_status(self, RB_ID, DCDU_temp, DCDU_volt, DCDU_curr, DCDU_hum, DCDU_press, BBU_temp, BBU_volt, BBU_curr, BBU_hum, BBU_press, RRU_temp, RRU_volt, RRU_curr, RRU_hum, RRU_press, PANEL_temp, PANEL_volt, PANEL_curr, BATTERY_temp, BATTERY_volt, BATTERY_curr, CONTROLLER_temp, CONTROLLER_volt, CONTROLLER_curr): 
        self._mydbmanager_.put_status(RB_ID, DCDU_temp, DCDU_volt, DCDU_curr, DCDU_hum, DCDU_press, BBU_temp, BBU_volt, BBU_curr, BBU_hum, BBU_press, RRU_temp, RRU_volt, RRU_curr, RRU_hum, RRU_press, PANEL_temp, PANEL_volt, PANEL_curr, BATTERY_temp, BATTERY_volt, BATTERY_curr, CONTROLLER_temp, CONTROLLER_volt, CONTROLLER_curr)
    
class AlarmSC():
    def __init__(self) -> None:
        self._mydbmanager_=DBManager



    # Function Name: storeAlarm
    # Description: stores generated alarms.
    # Parameters: RB_ID,alarm_data
    # Returns: None

    def storeAlarm(self,RB_ID,alarm_data):
        self.put_alarm(RB_ID, alarm_data)



    # Function Name: put_alarm
    # Description: puts the generated alarms.
    # Parameters: RB_ID, error_data
    # Returns: None
    
    def put_alarm(self,RB_ID, error_data):
        self._mydbmanager_.put_alarm(RB_ID, error_data)