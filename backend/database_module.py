import sqlite3
from sqlite3.dbapi2 import IntegrityError, OperationalError
from datetime import date, datetime
from os import makedirs

class database_manager:

    def __init__(self) -> None:

        try:

            makedirs('operational data')

        except FileExistsError:

            pass

        self.tank_database = sqlite3.connect('operational data/tank.db')
        self.tank_cursor = self.tank_database.cursor()
        
        self.report_database = sqlite3.connect('operational data/reports.db')
        self.report_cursor = self.report_database.cursor()

        self.date = date.today().strftime('%d-%m-%Y')
        self.datetime = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')

    def __tank_basic_table(self) -> bool:
        #This private method will generate a table to add tank number and corresponding volume and also the date it was added.
        #The method will return True in every case.

        self.tank_cursor.execute('''CREATE TABLE IF NOT EXISTS tank_basic_table (
	        date_added	TEXT NOT NULL,
	        tank_number	TEXT NOT NULL UNIQUE,
	        tank_volume	INTEGER NOT NULL
            )''')
        
        self.tank_database.commit()

        return True

    def __available_tank_table(self) -> bool:

        #This private method will generate a table which will list all the available tanks for cultivation. 
        # If everything goes right this tank will return True.
        
        self.tank_cursor.execute('''CREATE TABLE IF NOT EXISTS available_tanks (
            tank_number TEXT UNIQUE NOT NULL
        )''')

        self.tank_database.commit()

        return True

    def __pre_culture_tank_table(self) -> bool:

        #This private method will generate a table which will list all the tables currently in pre culture phase. 
        #If everythong goes right it will return True.

        self.tank_cursor.execute('''CREATE TABLE IF NOT EXISTS pre_culture_tanks (
                tank_number TEXT UNIQUE NOT NULL,
                tank_volume INTEGER NOT NULL,
                start_date TEXT NOT NULL,
                check_days INTEGER NOT NULL,
                culture TEXT NOT NULL,
                culture_time_days INTEGER NOT NULL,
                pH REAL,
                TDS INTEGER)''')

        self.tank_database.commit()
        
        return True

    def __report_table(self) -> bool:

        #This private method will generate seperate tables for every tanks being used for cultivation to contain pH, TDS and temperature
        #data along with the time when these were tested. 
        #If everything goes fine it will return True.

        self.__tank_basic_table()

        enlisted_tanks = self.tank_cursor.execute('SELECT tank_number FROM active_cultivation_tank').fetchall()

        for enlisted_tank in enlisted_tanks:

            self.report_cursor.execute('''CREATE TABLE IF NOT EXISTS {} (
                serial INTEGER PRIMARY KEY,
                timestamp TEXT NOT NULL,
                pH REAL NOT NULL,
                TDS INTEGER NOT NULL,
                temperature REAL NOT NULL,
                complete INTEGER NOT NULL
            )'''.format(enlisted_tank[0]))

            self.report_database.commit()

        return True

    def __active_tank_table(self) -> bool:

        #This method will generate a table to store the data of the tank which is currently being used for cultivation.
        #It will return true after the query is completed.

        self.tank_cursor.execute('''CREATE TABLE IF NOT EXISTS active_cultivation_tank (
            tank_number TEXT NOT NULL UNIQUE,
            tank_volume INTEGER NOT NULL,
            culture TEXT NOT NULL,
            culture_begin TEXT NOT NULL,
            culture_time_days INTEGER NOT NULL
        )''')    

        self.tank_database.commit()

        return True

    def tank_basic_entry(self, tank_num, tank_vol) -> bool:

        '''This method will enter data in the tank_basic_table. The required parameters to be provided by the user are
        tank number and tank volume. The tank number needs to be unique. If everything goes right the method will return
        True. But if the tank number is not unique it will return False.'''

        while self.__tank_basic_table() is True and self.__available_tank_table() is True:

            tank_id = 'TANK_'+str(tank_num)

            try:

                self.tank_cursor.execute('''INSERT INTO tank_basic_table 
                VALUES (?, ?, ?)''',(self.date, tank_id, int(tank_vol)))

                self.tank_cursor.execute('''INSERT INTO available_tanks
                VALUES (?)''',(tank_id,))

                self.tank_database.commit()                

                return True                

            except IntegrityError:

                return False

    def tank_basic_report(self, tank_num) -> tuple:

        '''Will return the date of addition, tank number and volume of the tank in
        (date, tank number, tank volume) format'''

        while self.__tank_basic_table() is True:

            try:

                return self.tank_cursor.execute('''SELECT * FROM tank_basic_table WHERE tank_number = ?''',(tank_num,)).fetchone()

            except IntegrityError:

                pass

    def available_tank_reporting(self) -> list:

        '''This method will show all the tanks available for cultivation. If everything goes fine it will return a list of
        available tanks. If no tank is available for cultivation it will return an empty list.'''

        report_list = list()
        try:
            elements = self.tank_cursor.execute('SELECT tank_number FROM available_tanks').fetchall()
            
            for element in elements:
                report_list.append(element[0])
        except:
            pass
     

        return report_list

    def available_tank_relisting(self, tank_num) -> bool:

        '''This method will again enlist the tanks which were used for cultivation after those are finished using.
        It will also remove the tank from the active_cultivation_tank table.It will return True.'''

        while self.__available_tank_table() is True:
            try:
                self.tank_cursor.execute('''DELETE FROM active_cultivation_tank WHERE tank_number = ?''',(tank_num,))

                self.tank_cursor.execute('''INSERT INTO available_tanks
                VALUES (?)''',(tank_num,))

                self.report_cursor.execute('DROP TABLE {}'.format(tank_num))

                self.tank_database.commit()
                self.report_database.commit()

                return True

            except IntegrityError:

                pass

    def pre_culture_entry(self, tank, culture, culture_time, check_days=2):

        '''This method will enter the tank and number of days for pre culturing. This method is for safety if by any
        chance power goes out'''
        # print(tank, culture, culture_time)

        while self.__pre_culture_tank_table() is True:

            try:

                vol = self.tank_cursor.execute('''SELECT tank_volume FROM tank_basic_table
                WHERE tank_number = ?''',(tank,)).fetchone()[0]

                self.tank_cursor.execute('''INSERT INTO pre_culture_tanks
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',(tank, float(vol), date.today(), check_days, culture, int(culture_time), None, None))

                self.tank_cursor.execute('''DELETE FROM available_tanks WHERE tank_number = ?''',(tank,))

                self.tank_database.commit()

                return True
                

            except IntegrityError:

                pass

    def pre_culture_report_entry(self, tank, ph, tds):

        '''This method will enter the pH and TDS value of pre culture phase.'''
        while self.__pre_culture_tank_table() is True:

            self.tank_cursor.execute('''UPDATE pre_culture_tanks
            SET
            pH = ?, TDS = ?
            WHERE
            tank_number = ?''',(ph, tds, tank))

            self.tank_database.commit()

            return True

    def pre_culture_water_report(self, tank_num) -> tuple:

        '''This method will return the latest water quality report of every pre_culture tank.
        If everything goes right, this method will return a tuple of ph and TDS data.
        The tuple will store information in (pH, TDS) order.'''

        return self.tank_cursor.execute('''
        SELECT pH, TDS 
        FROM pre_culture_tanks
        WHERE tank_number = ?''',(tank_num,)).fetchone()

    def pre_culture_tank_list(self) -> list:

        '''Will return a list of tuples of all tanks in pre culture in (tank_number, start_date, check_days, volume) format'''

        return self.tank_cursor.execute('''SELECT tank_number, start_date, check_days, tank_volume FROM pre_culture_tanks''').fetchall()

    def pre_culture_change_check_date(self, tank_num, check_days) -> bool:

        'Will change the date of last check in case the water does not meet the standards'

        self.tank_cursor.execute('''UPTADE pre_culture_tanks
        SET start_date = ?, check_days = ?
        WHERE tank_number = ?''',(date.today(), check_days, tank_num))

        self.tank_database.commit()

        return True

    def report_entry(self, tank, ph, tds, temp, complete=False) -> bool:

        '''This method will enter ph, tds and temperature data in the appropirate report table. If the method becomes successful then 
        it will return True.'''

        while self.__report_table() is True:

            self.report_cursor.execute('''INSERT INTO '''+str(tank)+'''(timestamp, pH, TDS, temperature, complete) 
            VALUES (
                ?, ?, ?, ?, ?
            )''',(self.datetime, ph, tds, temp, complete))

            self.report_database.commit()

            return True

            break

    def active_tank_entry(self, tank_num) -> bool:

        '''This method will register the tanks used for cultivation in the active_cultivation_tank table under the tank database.
        If everything goes right it will return True.'''

        while self.__active_tank_table() is True:

            try:

                culture_data = self.tank_cursor.execute('''SELECT tank_volume, culture, culture_time_days FROM pre_culture_tanks
                WHERE tank_number = ?''',(tank_num,)).fetchone()

                self.tank_cursor.execute('''INSERT INTO active_cultivation_tank VALUES (
                    ?, ?, ?, ?, ?
                )''',(tank_num, culture_data[0], culture_data[1], date.today(), culture_data[2]))

                self.tank_cursor.execute('''DELETE FROM pre_culture_tanks WHERE tank_number = ?''',(tank_num,))

                self.tank_database.commit()

                return True

            except IntegrityError:

                return False

    def active_tank_reporting(self) -> list:

        '''This method will show all the active cultivation tanks. If everything goes fine it will return a list of
        active tanks. If no tank is active then it will return an empty list.'''

        report_list = list()

        while self.__active_tank_table() is True:

            elements = self.tank_cursor.execute('SELECT tank_number FROM active_cultivation_tank').fetchall()

            for element in elements:

                report_list.append(element[0])

            return report_list  
    
    def latest_water_report(self, tank_num) -> tuple:

        '''This method will return the latest water quality report from the __report_table of every active tank.
        If everything goes right, this method will return a tuple of ph, tds and temperature data.
        The tuple will store information in (pH, TDS, temperature) order.'''

        return self.report_cursor.execute('''SELECT pH, TDS, temperature 
        FROM {} 
        ORDER BY serial DESC 
        LIMIT 1'''.format(tank_num)).fetchone()

    def all_water_report(self, tank_num) -> list:

        '''This method will return all pH, TDS and temperature data whenever needed to generate report. It will return
        a list of tuples. The tuples will store information in (pH, TDS, temperature) order.'''

        return self.report_cursor.execute('SELECT pH, TDS, temperature FROM {}'.format(tank_num)).fetchall()

    def analysis_water_report(self, tank_num) -> list:

        '''This method will return timestamp, ph, tds and temperature for plotting and analysis purpose. If everything goes fine,
        it will return a list of tuples. The tuples will contain the data in (timestamp, ph, tds, temperature) order.'''

        return self.report_cursor.execute('SELECT timestamp, pH, TDS, temperature FROM {}'.format(tank_num)).fetchall()

    def tank_status_report(self, tank_num) -> tuple:

        '''This method will return a tuple of the current status of a particular tank. If the tank is being used for cultivation then
        it will return a tuple of (tank_number, tank_volume, culture, culture_begin, culture_time_days) format. Else if it is empty it 
        will return an empty tuple.'''
        
        while self.__active_tank_table() is True:
            data =  self.tank_cursor.execute('''
            SELECT tank_number, tank_volume, culture, culture_begin, culture_time_days
            FROM active_cultivation_tank 
            WHERE tank_number = ?''',(tank_num,)).fetchone()
            if data == None:
                return tuple()
            else:
                return data

    def tank_data_unregister(self, tank_num) -> bool:

        '''This method will delete all the data of a registered tank. If the tank is being used for culture
        it will return False, else True.'''

        if tank_num not in self.active_tank_reporting():

            self.tank_cursor.execute('''DELETE FROM tank_basic_table WHERE tank_number = ?''',(tank_num,))
            self.tank_database.commit()

            try:
                self.tank_cursor.execute('''DELETE FROM available_tanks WHERE tank_number = ?''',(tank_num,))
                self.tank_database.commit()            
            except:            
                pass

            try:
                self.tank_cursor.execute('''DELETE FROM pre_culture_tanks WHERE tank_number = ?''',(tank_num,))
                self.tank_database.commit()            
            except:            
                pass

            try:
                self.tank_cursor.execute('''DELETE FROM active_cultivation_tank WHERE tank_number = ?''',(tank_num,))
                self.tank_database.commit()            
            except:            
                pass

            try:
                self.report_cursor.execute('''DROP TABLE {}'''.format(tank_num))
                self.report_database.commit()
            except OperationalError:
                pass

            return True

        else:

            return False