# Muchammad Fahd Ishamuddin DTI DS24 #21
#HOSPITAL SYSTEM
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
    print('Index\tNama\truangan\tpatid\tpenyakit\tstatus\t')
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
    print(f"Patient {name} dengan ID {pat_id} berhasil ditambahkan.")
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
    print(f"Ruangan baru dengan kelas {room_class} dengan ID {room_id} berhasil ditambahkan.")
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
    
def update_name():
    show_patient()
    index = int(input('Input Index you want edit: '))
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
    print(f"Nama patient dengan ID {index} diperbarui menjadi {name}.")
def update_room():
    show_patient()
    show_room()
    index = int(input('Input Index you want edit: '))
    room_id = int(input('update room id : '))
    current_room_id = patient[index]['room_id']
    if current_room_id:
        rooms[current_room_id]['occupants'].remove(patient[index]['name'])
    if len(rooms[room_id]['occupants']) < rooms[room_id]['max_capacity']:
        patient[index]['room_id'] = room_id
        rooms[room_id]['occupants'].append(patient[index]['name'])
        print(f"Patient {patient[index]['name']} dipindahkan ke Room {room_id}.")
    else:
        print(f"Room {room_id} sudah penuh.")
def update_status():
    show_patient()
    index = int(input('Input Index you want edit: '))
    status = input('New Status of patients :')
    patient[index]['status'] = status.capitalize()
    print(f"status patient dengan Nama {patient[index]['name']} diperbarui menjadi {status}.")
def update_disease():
    show_patient()
    index = int(input('Input Index you want edit: '))
    disease = input('New Disease of patients :')
    patient[index]['disease'] = disease.capitalize()
    print(f"disease patient dengan Nama {patient[index]['name']} diperbarui menjadi {disease}.")
def update_class():
    show_room()
    index = int(input('index room: '))
    if rooms[index]['occupants']:
            print(f"Tidak bisa mengubah class Room {index}, masih ada occupants.")
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
        print(f"Class Room {index} berhasil diubah menjadi {room_class_up} dan kapasitas menjadi {kapasitas}.")


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
    
def reset_patient_index():
    global patient
    patient = {i+1: info for i, (idx, info) in enumerate(patient.items())}
    print("Index pasien telah diatur ulang.")
    show_patient()
def delete_patient():
    show_patient()
    index = int(input('index patient : '))
    room_id = patient[index]['room_id']
    if room_id:
        rooms[room_id]['occupants'].remove(patient[index]['name'])
        del patient[index]
        print(f"Patient dengan ID {index} berhasil dihapus.")
    else:
        print("Patient tidak ditemukan.")
    reset_patient_index()
def delete_rooms():
    show_room()
    index = int(input('index room : '))
    if rooms[index]['occupants']:
        print(f"Tidak bisa menghapus Room {index}, masih ada occupant.")
    else:
        del rooms[index]
        print(f"Room dengan ID {index} berhasil dihapus.")

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
    # main_menu()
def patient_fam():
    print('WELCOME TO HOSPITAL DASHBOARD')
    print('YOU ONLY CAN FILTER NAME OF THE PATIENT')
    print('Patient Name : ')
    patient_id=input('Patient id:')
    print(patient_id)
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