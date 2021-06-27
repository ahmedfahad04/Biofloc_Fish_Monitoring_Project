from database_module import database_manager as db
from datetime import date, datetime

class gui_bg:

    def __init__(self, tank_number) -> None:

        self.tank_num = tank_number

    def monitoring_reporter(self) -> list:

        '''Will return a list of [tank number, tank volume, fish, culture start date, culture days remaining, 
        last check, pH, TDS, temperature] during culture'''

        report = db().latest_water_report(self.tank_num)
        status = db().tank_status_report(self.tank_num)

        days_remain = status[3]-(date.today()-datetime.strptime(status[2], '%Y-%m-%d').date()).days

        result = [self.tank_num]

        for s in status:

            result.append(s)

        for r in report:

            result.append(r)

        result[4] = days_remain

        return result

    def pre_culture_report(self) -> list:

        '''Will return list of [tank number, pH, TDS] during pre culture'''

        quality = db().pre_culture_water_report(self.tank_num) # (ph, tds)

        result = [self.tank_num]

        for i in quality:

            result.append(i)

        return result


