# Muchammad Fahd Ishamuddin DTI DS24 #21
#HOSPITAL SYSTEM
# Admin Menu Choose meaning on admin() fill 0 until change to be "fill your role!: to reset"
patient = {
    1: {"name": "Zainal", "room_id": 1,"patient_id":"Zai01","disease":"Stomach","status":"Good"},
    2: {"name": "Abidin", "room_id": 1,"patient_id":"Abi02","disease":"Gerd","status":"Bad"},
    3: {"name": "Daniel", "room_id": 1,"patient_id":"Dan03","disease":"DBD","status":"Normal"},
    4: {"name": "David", "room_id": 1,"patient_id":"Dav04","disease":"Influenza","status":"Good"},
    5: {"name": "Ridwan", "room_id": 1,"patient_id":"Rid05","disease":"Kidney","status":"Normal"},
    6: {"name": "Raihan", "room_id": 1,"patient_id":"Rai06","disease":"Diabetes","status":"Bad"},
    7: {"name": "Rizz", "room_id": 2,"patient_id":"Riz07","disease":"Kolesterol","status":"Bad"},
    8: {"name": "Sigit", "room_id": 2,"patient_id":"Sig08","disease":"Anemia","status":"Normal"},
    9: {"name": "Stevi", "room_id": 2,"patient_id":"Ste09","disease":"Diare","status":"Good"},
    10: {"name": "Jack", "room_id": 2,"patient_id":"Jac10","disease":"Diabetes","status":"Good"},
}
rooms = {
    1: {"class":"regular","max_capacity": 6, "occupants": ['Zainal','Abidin','Daniel','David','Ridwan','Raihan']},
    2: {"class":"vip","max_capacity": 4, "occupants": ['Rizz','Sigit','Stevi','Jack']},
    3: {"class":"vvip","max_capacity": 2, "occupants": []}
}
def show_patient():
    print('Index\tName\tRoom\tPatid\tDisease\tStatus\t')
    for index ,info in patient.items():
        name = info['name']
        room = info['room_id']
        patientid = info['patient_id']
        disease = info['disease']
        status = info['status']
        print(f'{index}\t{name}\t{room}\t{patientid}\t{disease:>10}\t{status}\t')
    print('------------------------------------------------------')

def show_room():
    print('Index\tClass\tMax_capacity\tOccupants\t')
    for index ,room_info in rooms.items():
        room_name = room_info['class']
        rom_max = room_info['max_capacity']
        room_fill = room_info['occupants']
        print(f'{index}\t{room_name}\t{rom_max:>10}\t{room_fill}\t')
    print('------------------------------------------------------')

def find_patient():
    print('YOU ONLY CAN FILTER NAME OF THE PATIENT')
    print('Patient Name : ')
    patient_nama=input('Patient name:')
    print(patient_nama)
    print('Index\tNama\truangan\tpatid\tpenyakit\tstatus\t')
    for index ,info in patient.items():
        if info['name'].lower()==patient_nama.lower():
            print(index,'\t', info['name'],'\t',info['room_id'],'\t',info['patient_id'],'\t',info['disease'],'\t',info['status'])
            break
    else:
        print(f'No data have name : {patient_nama}')
    print('------------------------------------------------------')

def sorted_patient():
    print('you wanna sort by? name/disease/room_id/status')
    sort_dcd = input('sorted!')
    sorted_patient = dict(sorted(patient.items(), key=lambda item: item[1][sort_dcd]))
    for index, info in sorted_patient.items():
        name = info['name']
        room = info['room_id']
        patientid = info['patient_id']
        disease = info['disease']
        status = info['status']
        print(f'{index}\t{name}\t{room}\t{patientid}\t{disease:>10}\t{status}\t')
    print('------------------------------------------------------')

def add_patient():
    pat_id = len(patient)+1
    name = input('nama patient : ')
    patient_id = name[:3] + str(pat_id)
    penyakit = input('disease :')
    kondisi = input('status patient :')
    patient[pat_id] = {"name": name.capitalize(), "room_id": 0,"patient_id":patient_id.capitalize(),"disease":penyakit.capitalize(),"status":kondisi.capitalize()}
    print(f"Patient {name} with ID {pat_id} Success added.")
    show_patient()

def add_room():
    room_id = len(rooms)+1
    room_class = input('nama kelas : ')
    kapasitas = 0
    if room_class == 'vvip':
        kapasitas+=2
    elif room_class == 'vip':
        kapasitas += 4
    else:
        kapasitas+=6
    rooms[room_id] = {"class":room_class,"max_capacity": kapasitas, "occupants": []}
    print(f"New Room with class {room_class} with ID {room_id} Success added.")
    show_room()

def admin_1():
    print('What you wanna add?')
    print('1. ADD patient')
    print('2. ADD Room')
    print('0. Back')
    menu_add = int(input('choose menu add :'))
    while menu_add != 0:
        if menu_add == 1:
            add_patient()
        elif menu_add == 2:
            add_room()
        menu_add = int(input('choose menu add : '))
    admin()
    
def admin_2():
    print('Show data')
    print('1. Data Patient')
    print('2. Data Room')
    print('3. Find Patient')
    print('4. Sorted Patient')
    print('0. Back')
    menu_admin = int(input('menu read admin : '))
    while menu_admin!=0:
        if menu_admin==1:
            show_patient()
        elif menu_admin == 2:
            show_room()
        elif menu_admin ==3:
            find_patient()
        elif menu_admin ==4:
            sorted_patient()
        menu_admin = int(input('menu read admin : '))
    admin()
    
def update_name():
    show_patient()
    index = int(input('Input Index you want edit: '))
    if index in patient:
        name = input('New Name of patients :')
        old_name = patient[index]['name']
        patient[index]['name'] = name.capitalize()
        if index < 10:
            patient_id = name[:3] + str(0) + str(index)
        else:
            patient_id = name[:3] + str(index)
        patient[index]['patient_id'] = patient_id.capitalize()
        room_id = patient[index]['room_id']
        if room_id and old_name in rooms[room_id]['occupants']:
            occupant_index = rooms[room_id]['occupants'].index(old_name)
            rooms[room_id]['occupants'][occupant_index] = name.capitalize()
        print(f"Patient Name with ID {index} Updated to be {name}.")
        show_patient()
    else:
        print(f'{index} Not Found')
    

def update_room():
    show_patient()
    show_room()
    index = int(input('Input Index you want edit: '))
    if index in patient:
        room_id = int(input('Update room ID: '))
        current_room_id = patient[index]['room_id']

        if room_id in rooms:
            if len(rooms[room_id]['occupants']) < rooms[room_id]['max_capacity']:
                if current_room_id:
                    rooms[current_room_id]['occupants'].remove(patient[index]['name'])
                patient[index]['room_id'] = room_id
                rooms[room_id]['occupants'].append(patient[index]['name'])
                print(f"Patient {patient[index]['name']} moved to Room {room_id}.")
            else:
                print(f"Room {room_id} is full. Patient remains in Room {current_room_id}.")
        else:
            print(f"Room {room_id} does not exist.")
        
        show_room()
    else:
        print(f"Patient with index {index} not found.")
    

def update_status():
    show_patient()
    index = int(input('Input Index you want edit: '))
    if index in patient:
        status = input('New Status of patients :')
        patient[index]['status'] = status.capitalize()
        print(f"status patient with Name {patient[index]['name']} Updated to be {status}.")
        show_patient()
    else:
        print(f'{index} Not Found')
    

def update_disease():
    show_patient()
    index = int(input('Input Index you want edit: '))
    if index in patient:
        disease = input('New Disease of patients :')
        patient[index]['disease'] = disease.capitalize()
        print(f"disease patient with Nama {patient[index]['name']} Updated to be {disease}.")
        show_patient()
    else:
        print(f'{index} not found')
    

def update_class():
    show_room()
    index = int(input('index room: '))
    if index in rooms:
        if rooms[index]['occupants']:
                print(f"can\'t update class Room {index}, still any occupants.")
        else:
            room_class_up = input('nama kelas : ')
            rooms[index]['class'] = room_class_up
            kapasitas = 0
            if room_class_up == 'vvip':
                kapasitas+=2
            elif room_class_up == 'vip':
                kapasitas += 4
            else:
                kapasitas+=6
            rooms[index]['max_capacity'] = kapasitas
            print(f"Class Room {index} Success Updated to be {room_class_up} and The capacity is {kapasitas}.")
            show_room()
    else:
        print(f'{index} Not Found')
    


def admin_3():
    print('menu update')
    print('FOR PATIENT')
    print('--------------------------')
    print('1. update name')
    print('2. update room')
    print('3. update status')
    print('4. update disease')
    print('--------------------------')
    print('FOR ROOOMS')
    print('5. Update Class')
    print('--------------------------')
    print('0. Back')
    update_menu = int(input('Update menu:'))
    while update_menu != 0:
        if update_menu == 1:
            update_name()
        elif update_menu == 2:
            update_room()
        elif update_menu == 3:
            update_status()
        elif update_menu == 4:
            update_disease()
        elif update_menu == 5:
            update_class()
        update_menu = int(input('Update menu:'))
    admin()
    
def reset_patient_index():
    global patient
    patient = {i+1: info for i, (idx, info) in enumerate(patient.items())}
    print("Index pasien telah diatur ulang.")
    show_patient()

def reset_rooms_index():
    global rooms
    rooms = {i+1: info for i, (idx, info) in enumerate(rooms.items())}
    print("Index rooms telah diatur ulang.")
    show_room()

def delete_patient():
    show_patient()
    index = int(input('index patient : '))
    if index in patient:
        room_id = patient[index]['room_id']
        if room_id != 0:
            if patient[index]['name'] in rooms[room_id]['occupants']:
                rooms[room_id]['occupants'].remove(patient[index]['name'])
        del patient[index]
        print(f"Patient with ID {index} Deleted.")
        reset_patient_index()
    else:
        print("Patient tidak ditemukan.")

def delete_rooms():
    show_room()
    index = int(input('index room : '))
    if rooms[index]['occupants']:
        print(f"Can\'t delete Room {index}, still any occupants.")
    else:
        del rooms[index]
        print(f"Room with ID {index} deleted.")
    reset_rooms_index()

def admin_4():
    print('Delete Menu')
    print('1. Delete Patient')
    print('2. Delete Rooms')
    delete_menu = int(input('which menu to delete: '))
    while delete_menu != 0:
        if delete_menu == 1:
            delete_patient()
        elif delete_menu == 2:
            delete_rooms()
        delete_menu = int(input('which menu to delete: '))
    admin()

def admin():
    print('HI ADMIN! Welcome to ADMIN DASHBOARD')
    print('You\'Re Super User Here')
    print('1. Add Data')
    print('2. Read Data')
    print('3. Update Data')
    print('4. Delete Data')
    print('0. Main Menu')
    admin_menu = int(input('Admin Menu Choose: '))
    while admin_menu!=0:
        if admin_menu == 1:
            admin_1()
        elif admin_menu == 2:
            admin_2()
        elif admin_menu == 3:
            admin_3()
        elif admin_menu == 4:
            admin_4()
        admin_menu = int(input('Admin Menu Choose: '))
def patient_fam():
    print('WELCOME TO HOSPITAL DASHBOARD')
    print('YOU ONLY CAN FILTER NAME OF THE PATIENT')
    print('Patient Name : ')
    patient_id=input('Patient id:')
    print(patient_id)
    print('Name\tROOM\tStatus')
    for index ,info in patient.items():
        if info['patient_id'].lower()==patient_id.lower():
            print(info['name'],'\t',info['room_id'],'\t',info['status'])
            break
    else:
        print(f'No data have name : {patient_id}')
def main_menu():
    print('What\'s Your Role?')
    print('1. ADMIN')
    print('2. Patient Family')
    print('0. Exit')
    
main_menu()
role = int(input('Fill your Role! : '))
while role !=0:
    if role == 1:
        admin()
    if role == 2:
        patient_fam()
    role = int(input('Fill your Role!: '))

# Admin Menu Choose meaning on admin() fill 0 until change to be "fill your role!: to reset"