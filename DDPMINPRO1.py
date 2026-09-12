rlog = []
while True:
    print("="*60)
    print("PERSONAL RUNNING LOG")
    print("1. Tambahkan Running Log")
    print("2. Ubah Running Log")
    print("3. Hapus Running Log")
    print("4. Tampilkan Semua Running Log")
    print("5. Keluar")
    print("="*60)
    pilih = input("Pilih antara [1-5] : ")
    print("="*60)
    if pilih == "1":
        hari = input("Berlari di hari apa? : ")
        lokasi = input("Berlari dimana? : ")
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
    elif pilih == "2":
        if not rlog:
            print("TIDAK ADA DATA YANG BISA DI UBAH")
        else:
            print("DAFTAR RUNNIG LOG")
            for idx, data in enumerate(rlog, 1):
                print(f"{idx}. Hari : {data[0]}, Lokasi : {data[1]}, Jarak : {data[2]} km")
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
    elif pilih == "3":
        if not rlog:
            print("TIDAK ADA DATA YANG BISA DIHAPUS")
        else:
            print("Daftar Running Log")
            for idx, data in enumerate(rlog, 1):
                print(f"{idx}. Hari : {data[0]}, Lokasi : {data[1]}, Jarak : {data[2]} km")
            try:
                hapus = int(input("pilih data yang mau dihapus : ")) - 1
                if 0 <= hapus < len(rlog):
                    rlog.pop(hapus)
                else:
                    print("="*60)
                    print("DATA TIDAK ADA")
            except ValueError:
                print("MASUKKAN ANGKA YANG BENAR")
    elif pilih == "4":
        if not rlog:
            print("TIDAK ADA DATA")
        else: 
            print("DAFTAR RUNNING LOG")
            for idx, data in enumerate(rlog, 1):
                print(f"{idx}. Hari : {data[0]}, Lokasi : {data[1]}, Jarak : {data[2]} km")
    elif pilih == "5":
        print("GOODBYE")
        break