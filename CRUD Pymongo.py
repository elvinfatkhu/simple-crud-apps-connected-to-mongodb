#CRUD DATABASE ELVIN FATKHUNNUHA
import pymongo as p




status = True
while status == True:
    input_menu = input('Selamat Datang di Aplikasi Database:\nPilihan Menu:\n1. Login\n2. Exit\nPilihan anda: ')
    if input_menu.isalpha() == True:
        print('Menu tidak boleh alphabet')
    elif input_menu > '2':
        print('Menu diluar jangkauan')
    elif input_menu < '1':
        print('Menu diluar jangkauan')
    elif input_menu == '2':
            print('selamat tinggal')
            status = False

    else:
        print('Menu login')

        status2 = True
        while status2 == True:
            input_user = input('Masukkan UserID: ')
            input_pass = input('Masukkan Password: ')
            try:
                myMongo = p.MongoClient('mongodb://localhost:27017', username= input_user, password= input_pass,authSource='Kampus',authMechanism='SCRAM-SHA-256') 
                dbs = myMongo.list_database_names()

                print('Authentication Granted')
                status2 = False
                
            except:
                print('Authentication Failed')
        
        
        
        print('===== MENU DATABASE KAMPUS =====')
        kampusdb = myMongo['Kampus']
        dosen = kampusdb['Dosen']
        mahasiswa = kampusdb['Mahasiswa']   
        status3 = True
        while status3 == True:
            try:
                input_sub = int(input('Database yang ingin dipilih :\n1. Dosen\n2. Mahasiswa\n3. Buat database baru\nPilihan anda: '))
                if input_sub < 1: 
                    print('Menu diluar jangkauan')
                elif input_sub > 3:
                    print('Menu diluar jangkauan')
                else:
                    status3 = False
            except:
                print('Tidak menerima huruf alfabet')

        if input_sub == 1:
            print('=================Database Dosen=================')
            statusdosen = True
            while statusdosen == True:
                try:
                    menu_dosen = int(input('Sub Menu Dosen\n1. Lihat database dosen \n2. input data baru \n3. Update data dosen\n4. Delete data dosen\n5. Keluar dari Database(harus login kembali)\n Pilihan anda: '))
                    if menu_dosen == 1:
                        for i in dosen.find():
                            print(i)
                    elif menu_dosen == 2:
                        nama = input('Masukkan nama: ')
                        usia = int(input('Masukkan usia: '))
                        asal = input('Masukkan asal kota: ')
                        bidang = input('Masukkan bidang: ')
                        titel = input('Masukkan titel: ')
                        dostatus = input('Masukkan status')
                        nip= int(input('Masukkan nip: '))
                        matkul = input('Masukkan matkul (jika lebih dari 1 gunakan koma): ')
                        if ',' in matkul:
                            matkul2 = matkul.split(',')
                        else:
                            matkul2 = [matkul]
                        
                        new_data = {
                            'nama': nama,
                            'usia': usia,
                            'asal' : asal,
                            'bidang' : bidang,
                            'titel' : titel,
                            'status' : dostatus,
                            'nip' : nip,
                            'matkul' : matkul2

                        }
                        dosen.insert_one(new_data)
                        for i in dosen.find():
                            print(i)
                    elif menu_dosen == 3:

            
                        input_value = input('Masukkan nama dosen yang ingin diubah datanya: ')
                        kondisi = {'nama' : input_value}
                        input_property= input('Masukkan kategori yang ingin diubah datanya ')
                        input_value2 = input('Masukkan isi kategori: ')  
                        new_val = {"$set" : {input_property : input_value2}}
                        dosen.update_one(kondisi, new_val)
                        z = []
                        for i in dosen.find(kondisi):
                            print(i)
                            z.append(i)
                        if bool(z) == False:
                            print('nama dosen salah')
                        else:
                            print('tersimpan')
                    
                    elif menu_dosen == 4:
                        ask = input('masukkan input: \n1. Hapus 1 data \n2. Hapus banyak data\n Pilihan anda: ')
                        if ask == '1':
                            delete = input('tentukan kategori yang ingin dihapus seluruh data nya (contoh: nama) : ')
                            delete2 = input('tentukan isi kategori yang ingin dihapus seluruh data nya (contoh: joni): ')

                            Kondisi = {delete : delete2}
                            dosen.delete_one(Kondisi)
                            
                        elif ask == '2':
                            delete = input('tentukan kategori yang ingin dihapus seluruh data nya (contoh: nama) : ')
                            delete2 = input('tentukan isi kategori yang ingin dihapus seluruh data nya (contoh: joni): ')
                            Kondisi = {delete : delete2}
                            dosen.delete_many(Kondisi)
                            print('berhasil dihapus')
                except:
                    print('Tidak menerima alfabet')


        elif input_sub == 2:
            print('=================Database Mahasiswa=================')
            statusmahasiswa = True
            while statusmahasiswa == True:
                try:
                    menu_mahasiswa = int(input('Sub Menu Mahasiswa\n1. Lihat database mahasiswa \n2. input data baru \n3. Update data Mahasiswa\n4. Delete data Mahasiswa\n5. Keluar dari Database(harus login kembali)\n Pilihan anda: '))
                    if menu_mahasiswa == 1:
                        for i in mahasiswa.find():
                            print(i)
                    elif menu_mahasiswa == 2:
                        nama = input('Masukkan nama: ')
                        usia = int(input('Masukkan usia: '))
                        Kota_asal = input('Masukkan asal kota: ')
                        prodi = input('Masukkan prodi: ')
                        angkatan = input('Masukkan angkatan: ')
                        nim = input('Masukkan nim')
                       
                        new_data = {
                            'nama': nama,
                            'usia': usia,
                            'Kota_asal' : Kota_asal,
                            'prodi' : prodi,
                            'angkatan' : angkatan,
                            'nim' : nim,
                        }
                        mahasiswa.insert_one(new_data)
                        for i in mahasiswa.find():
                            print(i)
                    elif menu_mahasiswa == 3:
            
                        input_value = input('Masukkan nama mahasiswa yang ingin diubah datanya: ')
                        kondisi = {'nama' : input_value}
                        input_property= input('Masukkan kategori yang ingin diubah datanya ')
                        input_value2 = input('Masukkan isi kategori: ')  
                        new_val = {"$set" : {input_property : input_value2}}
                        mahasiswa.update_one(kondisi, new_val)
                        z = []
                        for i in mahasiswa.find(kondisi):
                            print(i)
                            z.append(i)
                        if bool(z) == False:
                            print('nama mahasiswa salah')
                        else:
                            print('tersimpan')
                    
                    elif menu_mahasiswa == 4:
                        ask = input('masukkan input: \n1. Hapus 1 data \n2. Hapus banyak data\n Pilihan anda: ')
                        if ask == '1':
                            delete = input('tentukan kategori yang ingin dihapus seluruh data nya (contoh: nama) : ')
                            delete2 = input('tentukan isi kategori yang ingin dihapus seluruh data nya (contoh: joni): ')

                            Kondisi = {delete : delete2}
                            mahasiswa.delete_one(Kondisi)
                            
                        elif ask == '2':
                            delete = input('tentukan kategori yang ingin dihapus seluruh data nya (contoh: nama) : ')
                            delete2 = input('tentukan isi kategori yang ingin dihapus seluruh data nya (contoh: joni): ')
                            Kondisi = {delete : delete2}
                            mahasiswa.delete_many(Kondisi)
                            print('berhasil dihapus')



                    
                                        
                        
                    
                    elif menu_mahasiswa < 1:
                        print('Menu diluar jangkauan')
                    elif menu_mahasiswa > 5 : 
                        print('Menu diluar jangkauan')
                    elif menu_mahasiswa == 5:
                        statusmahasiswa = False
            
                except:
                    print('Tidak menerima alfabet')


                        

                    




