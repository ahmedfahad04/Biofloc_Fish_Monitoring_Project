from database_module import database_manager
from random import uniform, randrange

for i in range(1, 21):

    print(database_manager().tank_basic_entry(i, randrange(15000, 20000)))

availables = database_manager().available_tank_reporting()

for i in availables:

    print(database_manager().tank_basic_report(i))

print(availables)

culture_time = {'Koi':3, 'Gojar':4, 'Pangash':5}
cultures = ['Koi', 'Gojar', 'Pangash']

for i in availables[0:11]:

    fish = cultures[randrange(0, 3)]

    print(database_manager().pre_culture_entry(i, fish, (culture_time.get(fish)*30)))

pre_cults = database_manager().pre_culture_tank_list()
print(pre_cults)

for j in pre_cults:

    print(j[0])

    print(database_manager().pre_culture_report_entry(j[0], round(uniform(0, 14.1), 2), randrange(1000, 1500)))

for k in pre_cults:

    print(database_manager().pre_culture_water_report(k[0]))

for l in pre_cults[0:8]:

    print(database_manager().active_tank_entry(l[0]))

act_tanks = database_manager().active_tank_reporting()
print(act_tanks)

for tm in range(0, 11):
    for i in act_tanks:

        print(database_manager().report_entry(i, round(uniform(0, 14.1), 2), randrange(1000, 1600), round(uniform(0, 25), 2)))

for i in act_tanks:

    print(database_manager().latest_water_report(i))

for i in act_tanks:

    print(database_manager().tank_status_report(i))

for i in act_tanks:

    print(database_manager().all_water_report(i))

for i in act_tanks[0:2]:

    print(database_manager().available_tank_relisting(i))


print(database_manager().tank_data_unregister('TANK_{}'.format(randrange(1, 21))))