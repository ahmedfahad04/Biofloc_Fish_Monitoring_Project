from database_module import database_manager
from sercom_module import sercom_manager
from datetime import date, datetime

fillUpList = list() #Lists which tanks needs water
followUpList = list() #Lists the master modules for follow up

act_tanks_fill = database_manager().active_tank_reporting() #List all the active tanks for water fill up

for tank1 in act_tanks_fill: #Iterates to find which tanks need full level water
    if sercom_manager(tank1).fullLevelCheck() is False: #If water is not available up to full level of the tank
        fillUpList.append(tank1)

for empty in fillUpList: #Iterates and enlists master modules for follow up
    if sercom_manager(tank1).fullLevelFiller() is True: #If the module is a master module
        followUpList.append(tank1)

while len(followUpList) != 0: #While the tanks do not fill up to full level
    for followUp in followUpList: #Iterates through evey master module, removes from the follow up list if the water is up to full level
        if sercom_manager(followUp).waterFillFollowUp() is True:
            followUpList.remove(followUp)

while True: #Loops until no tank is active
    act_tanks_check = database_manager().active_tank_reporting() #List all the active tanks for water monitoring
   
    if len(act_tanks_check) != 0: #If there is any tank remaining for culture then this operation will execute
        for tank in act_tanks_check: #Iterates through every pre culture tanks and checks water parameter

            #Bring out the list of the current status of the tank
            status = database_manager().tank_status_report(tank)

            #If the culture period is not over
            if(date.today()-datetime.strptime(status[3], '%Y-%m-%d').date()).days < status[4]:

                report = sercom_manager(tank).cultureTest()
                database_manager().report_entry(tank, report[0], report[1], report[2])

            #If the culture period is over
            else:

                report = sercom_manager(tank).cultureTest()
                database_manager().report_entry(tank, report[0], report[1], report[2], complete=True)
    else: #If there is no tank remaining for culture then this operation will execute
        break