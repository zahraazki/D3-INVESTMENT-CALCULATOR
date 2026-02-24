# Menghitung tabungan dengan setoran rutin per bulan
def tabungan_setoran(a, bunga, bulan):
    return a * ((1 + bunga) ** bulan - 1) / bunga

# Fungsi untuk input jumlah bulan 
def input_bulan(prompt) :
    while True:
        try:
            val = int(input(prompt))
            if val < 1:
                print("  [!] Bulan harus >=1")
                continue
            return val
        except ValueError:
            print("  [!] Masukkan angka bulat!")

# Menampilkan detail pertumbuhan investasi tanpa setoran rutin per bulan
def detail_pertumbuhan_tanpa_setoran(modal, bunga_bulanan, total_bulan):
    print()
    garis("-")
    print("  DETAIL PERUMBUHAN (RANGE BULAN)".center(W))
    garis("-")
    print(f"  Total bulan investasi: {total_bulan} bulan")
    bulan_awal = input_bulan(" Tampilkan dari bulan ke : ")
    bulan_akhir = input_bulan(" Tampilkan sampai bulan ke: ")

    if bulan_awal > bulan_akhir:
        print("  [!] Bulan awal tidak boleh lebih besar dari bulan akhir.")
        return
    if bulan_akhir > total_bulan:
        print(f"  [!] Melebihi batas investasi ({total_bulan}) bulan), disesuaikan otomatis.")
        bulan_akhir = total_bulan

    print()
    garis("=")
    print("  TABEL PERTUMBUHAN UANG PER BULAN".center(W))
    print(f"  Modal Awal: {rp_short(modal)}   |   Bunga: {bunga_bulanan*12*100:.2f}%/tahun".center(W))
    garis("=")
    header = f"  {'Bulan':^6} | {'Modal':^20} | {'Total Uang':^20} | {'Keuntungan Bulan Ini':^22}"
    print(header)
    garis("-")  

    for b in range(bulan_awal, bulan_akhir + 1):
        saldo_bulan  = tabungan_tanpa_setoran(modal, bunga_bulanan, b)
        saldo_prev   = tabungan_tanpa_setoran(modal, bunga_bulanan, b - 1) if b > 1 else modal
        untung_bulan = saldo_bulan - saldo_prev
        print(f"  {b:^6} | {rp_short(modal):^20} | {rp_short(saldo_bulan):^20} | {rp_short(untung_bulan):^22}")

    garis("-")
    saldo_akhir  = tabungan_tanpa_setoran(modal, bunga_bulanan, bulan_akhir)
    untung_total = tabungan_tanpa_setoran(modal, bunga_bulanan, bulan_akhir) - modal
    print(f"  {'TOTAL s/d bulan ' + str(bulan_akhir):<30}  {rp_short(saldo_akhir):^20}   {'Akum. Untung: ' + rp_short(untung_total)}")
    garis("=")
    input("\n  Tekan Enter untuk lanjut...")

#Format Rupiah
def rp_short(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

#Menu Tanpa Setoran Rutin
def menu_tanpa_setoran():
    print()
    garis("=")
    print(" TABUNGAN INVESTASI TANPA SETORAN RUTIN ")
    garis ("=")
    modal            = input_angka(" Modal awal (Rp)                : ",1)
    bunga_tahunan    = input_angka(" Bunga/return per tahun (%)     : ", 0)
    total_bulan      = input_bulan(" Lama investasi (bulan)         : ")
    bunga_bulanan    = (bunga_tahunan / 100) / 12
    sub_menu_tanpa_setoran(modal, bunga_bulanan, bunga_tahunan, toal_bulan)

#Sub Menu Setoran Rutin
def sub_menu_setoran_rutin(setoran, bulanan, bunga_tahunan, total_bulan):
    saldo_skrg     = tabungan_setoran(setoran, bunga_bulanan, total_bulan)
    untung_skrg    = tabungan_setoran(setoran, bunga_bulanan, total_bulan) - setoran * total_bulan
    modal_total    = setoran * total_bulan

    while True:
        print()
        garis("-")
        print("HASIL INVESTASI DENGAN SETORAN RUTIN".center(W))
        garis("-")
        print(f" {'Setoran per bulan':<30}: {rp_short(setoran)}")
        print(f"  {'Bunga per tahun':<30}: {bunga_tahunan}%")
        print(f"  {'Lama investasi':<30}: {total_bulan} bulan")
        print(f"  {'Total uang disetor':<30}: {rp_short(modal_total)}")
        garis("-")
        print(f"  {'Total uang saat ini':<30}: {rp_short(saldo_skrg)}")
        print(f"  {'Total keuntungan (bunga)':<30}: {rp_short(untung_skrg)}")
        garis("=")
        print()
        print("  SUB-MENU:")
        print("  [1] Lihat detail pertumbuhan uang")
        print("  [2] Lihat berapa bulan target tabungan tercapai")
        print("  [0] Kembali ke menu utama")
        print()
        pilihan = input("  Pilih: ").strip()

        if pilihan == "1":
            detail_pertumbuhan_setoran(setoran, bunga_bulanan, bunga_tahunan, total_bulan)
        elif pilihan == "2":
            cari_target_setoran(setoran, bunga_bulanan)
        elif pilihan == "0":
            break
        else:
            print(" [!] Pilihan tidak valid.")

