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
        
jika user memilih [1] maka akan masuk ke proses input data.

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

Khusus untuk input [jarak] mengunakan while True, jika user menginput jarak < 0 atau menginput variabel user akan diminta untuk input ulang hingga datanya valid.
