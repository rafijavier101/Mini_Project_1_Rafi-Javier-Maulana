# Mini_Project_1_Rafi Javier Maulana

<img width="1280" height="800" alt="iCK0W6ihM7" src="https://github.com/user-attachments/assets/90b18803-7662-4837-b3af-b59bfccb0f22" />


<img width="1280" height="800" alt="code menu 1" src="https://github.com/user-attachments/assets/102c4fa0-fe8c-47f9-8a51-183f75045a1e" />

rlog = [] adalah wadah list

while True untuk mengloop semua code yang ada setelahnya


baris ke 3-12 adalah tampilan menu utama

<img width="413" height="146" alt="menu ter" src="https://github.com/user-attachments/assets/7cfeec24-9ba1-47c7-886e-4e08f9a5d0a3" />


baris ke 13-29 adalah kode untuk menginput data running log. 

 if pilih == "1":
 
        hari = input("Berlari di hari apa? : ")
        lokasi = input("Berlari dimana? : ")
        
jika user memilih [1] pada menu, maka akan masuk ke proses input data.

while True:

            try:
                jarak = float(input("Berapa kilometer kamu berlari? : "))                
                if jarak < 0:             
                    print("JARAK LARI TIDAK VALID")          
                    continue      
                break               
            except ValueError:            
                print("="*60)             
                print("JARAK LARI HARUS BERUPA ANGKA")
        print("="*60)
        print("RUNNING LOG + 1")
        rdata = (hari, lokasi, jarak)
        rlog.append(rdata)

Khusus untuk input [jarak] mengunakan while True, jika user menginput jarak < 0 atau menginput variabel user akan diminta untuk input ulang hingga datanya valid. Sedangkan jika user menginput semua data dengan benar, maka running log akan bertambah 1

<img width="418" height="707" alt="terminal menu 1" src="https://github.com/user-attachments/assets/e39d7b6d-f8d7-47e8-9b9e-f1e476747897" />


<img width="1280" height="800" alt="code 2 3" src="https://github.com/user-attachments/assets/2ac59c53-406f-41ec-9a7c-87540b849688" />

baris ke 30-52 adalah kode untuk mengubah data running log yang sudah ada.

 elif pilih == "2":
 
        if not rlog:
            print("TIDAK ADA DATA YANG BISA DI UBAH")
        else:
            print("DAFTAR RUNNIG LOG")
            for idx, data in enumerate(rlog, 1):
                print(f"{idx}. Hari : {data[0]}, Lokasi : {data[1]}, Jarak : {data[2]} km")

jika user memilih [2] pada menu, maka akan masuk ke proses mengubah data yang diawali dengan mengecek apakh ada data yang bisa diubah. Jika ada data yang bisa diubah maka seluruh data akan ditampilkan.

try:

                pili = int(input("pilih data yang mau di ubah : ")) - 1
                if 0 <= pili < len(rlog):
                    hari = input("Masukkan hari baru :")
                    lokasi = input("Masukkan lokasi baru :")
                    jarak = float(input("Masukkan jarak baru :"))
                    rlog[pili] = (hari, lokasi, jarak)
                    print("="*60)
                    print(" DATA BERHASIL DI UPDATE")
                    print("="*60)
                else:   
                    print("="*60)
                    print("DATA TIDAK ADA")
            except ValueError:
                print("="*60)
                print("MASUKKAN ANGKA YANG BENAR")
jika ada data yang bisa diubah, user bisa memilih data mana yang mau diubah, setelah memilih user harus memasukkan data baru.

<img width="441" height="322" alt="terminal 2 1" src="https://github.com/user-attachments/assets/477f6814-b3b7-46c4-b722-98bb3ba04cd8" />
<img width="414" height="546" alt="terminal 2 2" src="https://github.com/user-attachments/assets/d5254552-817e-4e98-afa5-7c8eab19775f" />

baris ke 53-68 kode untuk menghapus data running log yang sudah ada.
 
 elif pilih == "3":
 
        if not rlog:
            print("TIDAK ADA DATA YANG BISA DIHAPUS")
        else:
            print("Daftar Running Log")
            for idx, data in enumerate(rlog, 1):
                print(f"{idx}. Hari : {data[0]}, Lokasi : {data[1]}, Jarak : {data[2]} km")

jika user memilih [3] pada menu, maka akan masuk ke proses menghapus data yang diawali dengan mengecek apakh ada data yang bisa dihapus. Jika ada data yang bisa dihapus maka seluruh data akan ditampilkan.

try:

                hapus = int(input("pilih data yang mau dihapus : ")) - 1
                if 0 <= hapus < len(rlog):
                    rlog.pop(hapus)
                else:
                    print("="*60)
                    print("DATA TIDAK ADA")
            except ValueError:
                print("MASUKKAN ANGKA YANG BENAR")


Jika ada data yang bisa dihapus, user harus memilih data mana yang mau di hapus.

<img width="434" height="350" alt="terminal 3" src="https://github.com/user-attachments/assets/6eb73265-40e8-469c-82c0-9f1ea46e1e80" />
<img width="414" height="603" alt="terminal 3 2" src="https://github.com/user-attachments/assets/81139d98-cade-4103-b21f-828a6e29fb98" />

<img width="1280" height="800" alt="code 4 5" src="https://github.com/user-attachments/assets/8a40f20c-d72d-48a3-8854-1e5a988587e9" />

baris ke 69-75 adalah kode untuk emlihat semua data yang sudah diinput.
 
 elif pilih == "4":
 
        if not rlog:
            print("TIDAK ADA DATA")
        else: 
            print("DAFTAR RUNNING LOG")
            for idx, data in enumerate(rlog, 1):
                print(f"{idx}. Hari : {data[0]}, Lokasi : {data[1]}, Jarak : {data[2]} km")
 
jika user memilih [4] pada menu, maka akan dicek apakah ada data running log, jika ada semua data akan ditampilkan.

<img width="421" height="385" alt="terminal 4" src="https://github.com/user-attachments/assets/fa338e62-057f-4d8a-8e5d-8e37a5cb2d25" />
<img width="421" height="321" alt="terminal 4 2 " src="https://github.com/user-attachments/assets/782a5048-4b1f-40d5-ae01-92f5a54b8ff7" />

jika user memilih [5] pada menu, maka program akan berhenti.

<img width="419" height="189" alt="terminal 5" src="https://github.com/user-attachments/assets/35a53f1e-13ee-4777-8061-7450c6db7fa5" />



