#This is the code for the executable which will run in the background
#for executing the pre culture phase

from database_module import database_manager
from sercom_module import sercom_manager
from datetime import datetime, date

fillUpList = list() #Lists which tanks needs water
followUpList = list() #Lists the master modules for follow up

pre_cults_fill = database_manager().pre_culture_tank_list() #List all the pre culture tanks for water fill up

for tank in pre_cults_fill: #Iterates and finds which tanks need half level water
    if sercom_manager(tank[0]).halfLevelCheck() is False: #If water is not available up to half level of the tank
        fillUpList.append(tank[0])

for empty in fillUpList: #Iterates and enlists the master modules for follow up
    if sercom_manager(empty).halfLevelFiller() is True: #If the module is a master module
        followUpList.append(empty)            
    fillUpList.remove(empty)

while len(followUpList) != 0: #While the tanks do not fill up to half level
    for followUp in followUpList: #Iterates through evey master module, removes from the follow up list if the water is up to half level
        if sercom_manager(followUp).waterFillFollowUp() is True:
            followUpList.remove(followUp)

#Water Fillup ends here
#Execute aeration program

while True: #Loops until all pre cultures are over
    
    pre_cults_check = database_manager().pre_culture_tank_list() #List all the pre culture tanks for water monitoring
    
    if len(pre_cults_check) != 0: #If there is any tank remaining for pre culture then this operation will execute
        for test in pre_cults_check: #Iterates through every pre culture tanks and checks water parameter
            if (date.today() - datetime.strptime(test[1], '%Y-%m-%d').date()).days == test[2]: #Will test the water if it is a checking day
                report = sercom_manager(test).preCultureTest()
                database_manager().pre_culture_report_entry(test, report[0], report[1])
            else:
                continue
    else: #If there is no tank remaining for pre culture then this operation will execute
        break