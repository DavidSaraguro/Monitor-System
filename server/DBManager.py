# File Name: Alarm.py
# Summary: This file consists of the function set_alarm.
# Description: This file command the storage in  DynamoDB. 
# Author: David Saraguro Fárez.
# Last Modified: 06-05-2022


import boto3
from datetime import datetime



# Function Name: put_status
# Description: Items and information contained in the STATUS table are generated.
# Parameters: RB_ID, radiobase_dcdutemp, radiobase_dcduvolt, radiobase_dcducurr, 
# radiobase_dcduhum, radiobase_dcdupress, radiobase_bbutemp, radiobase_bbuvolt, 
# radiobase_bbucurr, radiobase_bbuhum, radiobase_bbupress, radiobase_rrutemp, 
# radiobase_rruvolt,  radiobase_rrucurr, radiobase_rruhum, radiobase_rrupress, 
# sfv_paneltemp, sfv_panelvolt, sfv_panelcurr, sfv_batterytemp, sfv_batteryvolt, 
# sfv_batterycurr, sfv_controllertemp, sfv_controllervolt, sfv_controllercurr.
# Returns: table items

def put_status(RB_ID, radiobase_dcdutemp, radiobase_dcduvolt, radiobase_dcducurr, radiobase_dcduhum, radiobase_dcdupress, radiobase_bbutemp, radiobase_bbuvolt, radiobase_bbucurr, radiobase_bbuhum, radiobase_bbupress, radiobase_rrutemp, radiobase_rruvolt,  radiobase_rrucurr, radiobase_rruhum, radiobase_rrupress, sfv_paneltemp, sfv_panelvolt, sfv_panelcurr, sfv_batterytemp, sfv_batteryvolt, sfv_batterycurr, sfv_controllertemp, sfv_controllervolt, sfv_controllercurr, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

        table = dynamodb.Table('STATUS')
        now= datetime.now()
        response = table.put_item(
        Item={
            
            'ID': str(now),
            'DCDU_temp': radiobase_dcdutemp,
            'DCDU_volt': radiobase_dcduvolt,
            'RB_ID': RB_ID,
            'DCDU_curr': radiobase_dcducurr,
            'DCDU_hum': radiobase_dcduhum,
            'DCDU_press': radiobase_dcdupress,
            'BBU_temp': radiobase_bbutemp,
            'BBU_volt': radiobase_bbuvolt,
            'BBU_curr': radiobase_bbucurr,
            'BBU_hum': radiobase_bbuhum,
            'BBU_press': radiobase_bbupress,
            'RRU_temp': radiobase_rrutemp,
            'RRU_volt': radiobase_rruvolt,
            'RRU_curr': radiobase_rrucurr,
            'RRU_hum': radiobase_rruhum,
            'RRU_press': radiobase_rrupress,
            'PANEL_temp': sfv_paneltemp,
            'PANEL_volt': sfv_panelvolt,
            'PANEL_curr': sfv_panelcurr,
            'BATTERY_temp': sfv_batterytemp,
            'BATTERY_volt': sfv_batteryvolt,
            'BATTERY_curr':sfv_batterycurr,
            'CONTROLLER_temp': sfv_controllertemp,
            'CONTROLLER_volt': sfv_controllervolt,
            'CONTROLLER_curr': sfv_controllercurr,
        }    
    )
    
    return response



# Function Name: put_alarm
# Description: Items and information contained in the ALARMS table are generated.
# Parameters: RB_ID, error_data, dynamodb=None
# Returns: organuzed errors

def put_alarm(RB_ID, error_data, dynamodb=None):
    organized_errors={}
    for component in error_data:
        for sensor in error_data[component]:
            column_name=str(component)+"_"+str(sensor)
            organized_errors[column_name]=error_data[component][sensor]
    

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

        table = dynamodb.Table('ALARM')
        now= datetime.now()
        organized_errors["RB_ID"]=RB_ID
        organized_errors["time_stamp"]=str(now)

        response = table.put_item(
        Item=organized_errors  )   
        return response 



if __name__ == '__main__':
    status_resp = put_status('RB18',10,20,30,40,50,60,70,80,90,10,20,30,40,50,60,70,80,90,10,10,20,30,40,50)
    print("Status response:")
    print(status_resp)
