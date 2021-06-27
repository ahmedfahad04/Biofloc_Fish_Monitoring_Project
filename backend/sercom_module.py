from serial import Serial
import time

class sercom_manager:

    def __init__(self, tank_num) -> None:
        self.tank_com = Serial('/dev/ttyS0', baudrate = 9600, timeout = 2)
        self.lab_com = Serial('/dev/ttyUSB0', baudrate = 9600, timeout = 1.6)
        self.module_code = int(str(tank_num).removeprefix('TANK_'))
        self.set_code = 1000
        self.call_code = str(self.module_code+self.set_code)
        self.tank_command_dict = {'MasterCheck':1, 'PreCultureSample':2, 'CultureMonitoring':3,
                                  'HalfLevelFiller':4, 'FullLevelFiller':5}
        self.lab_command_dict = {'SamplePresence':1, 'pH':2, 'TDS':3, 'Clear':4}

    def __writer(self, content, module='TANK') -> None:
        #This private method will be used for serial writing to tank and lab module
        if module == 'TANK':
            self.tank_com.write(str(content).encode('utf-8'))
        elif module == 'LAB':
            self.lab_com.write(str(content).encode('utf-8'))

    def __reader(self, module='TANK') -> str:
        #This private method will be used for serial reading to tank and lab module
        if module == 'TANK':
            return self.tank_com.readline().decode('utf-8')
        elif module == 'LAB':
            return self.lab_com.readline().decode('utf-8')

    def __lab_report(self, temperature=False) -> list[float]:
        #This private method will return water quality report

        if temperature == False: #This operation will occur during pre culture when temperature is not necessary       
            self.__writer(self.lab_command_dict['pH'], module='LAB')
            pH = self.__reader(module = 'LAB')
            self.__writer(self.lab_command_dict['TDS'], module='LAB')
            tds = self.__reader(module = 'LAB')
            self.__writer(self.lab_command_dict['Clear'], module='LAB')

            return [float(pH), int(tds)]

        else: #This operation will occur during culture when temperature is a necessary factor         
            self.__writer(self.lab_command_dict['pH'], module='LAB')
            pH = self.__reader(module = 'LAB')            
            self.__writer(self.lab_command_dict['TDS'], module='LAB')
            tds = self.__reader(module = 'LAB')
            self.__writer(self.lab_command_dict['Clear'], module='LAB')

            return [float(pH), int(tds), float(temperature)]

    def __broker(self) -> bool:
        #This private method will prepare a tank module for instructions
        while True:
            self.__writer(self.call_code)
            if self.__reader() == 'G'+str(self.call_code):
                return True
            else:
                continue
    
    def __masterCheck(self) -> bool:
        #This private method will check if a module is a master module
        while self.__broker() is True:
            self.__writer(self.tank_command_dict['MasterCheck'])
            if self.__reader() == '0':                
                return True
            else:                
                return False

    def preCultureTest(self) -> list:
        '''Returns [pH, TDS]'''
        while self.__broker() is True:
            self.__writer(self.tank_command_dict['PreCultureSample'])
            if self.__reader() == 'SPSW':
                self.__writer(self.call_code)
                while True:
                    self.__writer(self.lab_command_dict['SamplePresence'], module='LAB')
                    if self.__reader(module='LAB') == '0':
                        self.__writer(self.call_code)
                        break
                    else:
                        continue
                return self.__lab_report()

    def cultureTest(self) -> list:
        '''Returns [pH, TDS, Temperature]'''
        while self.__broker() is True:
            self.__writer(self.tank_command_dict['CultureMonitoring'])
            if self.__reader() == 'TR':
                self.__writer(self.call_code)
                reply = self.__reader()
                thermoRead = reply.removesuffix('SCSW')
                con_call = reply.removeprefix(thermoRead)
                if con_call == 'SCSW':
                    self.__writer(self.call_code)
                    while True:
                        self.__writer(self.lab_command_dict['SamplePresence'], module='LAB')
                        if self.__reader(module='LAB') == '0':                      
                            self.__writer(self.call_code)
                            break
                        else:
                            continue

                    return self.__lab_report(temperature=thermoRead)

    def halfLevelFiller(self) -> bool:
        '''Fills water to half level of the tank'''
        if self.__masterCheck() is True:
            if self.__broker() is True:
                self.__writer(self.tank_command_dict['HalfLevelFiller'])
                return True
        else:
            return False

    def fullLevelFiller(self) -> bool:
        '''Fills water to full level of the tank'''
        if self.__masterCheck() is True:
            if self.__broker() is True:
                self.__writer(self.tank_command_dict['FullLevelFiller'])
                return True
        else:
            return False
    
    def waterFillFollowUp(self) -> bool:
        '''Follows up during fillup of water. Applicable only for master module.
        First the water fillup activity needs to be executed and then follow up'''
        time.sleep(1)
        self.__writer(self.call_code)
        if self.__reader() == '1':
            return True
        else:
            return False

    def halfLevelCheck(self) -> bool:
        '''Checks if there is already water up to half level of the tank'''
        if self.__masterCheck() is True:
            if self.__broker() is True:
                self.__writer(6)
                if self.__reader() == '0':
                    return True
                else:
                    return False
    
    def fullLevelCheck(self) -> bool:
        '''Checks if there is already water up to full level of the tank'''
        if self.__masterCheck() is True:
            if self.__broker() is True:
                self.__writer(7)
                if self.__reader() == '0':
                    return True
                else:
                    return False