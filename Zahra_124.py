#Format Rupiah
def rp_short(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

#Menu Tanpa Setoran Rutin
def menu_tanpa_setoran():
    from Irham_104 import garis, W
    from Abdilla_094 import input_angka
    from Ghevira_103 import input_bulan
    from Kayla_108 import sub_menu_tanpa_setoran
    print()
    garis("=")
    print(" TABUNGAN INVESTASI TANPA SETORAN RUTIN ".center(W))
    garis("=")
    modal         = input_angka(" Modal awal (Rp)                : ", 1)
    bunga_tahunan = input_angka(" Bunga/return per tahun (%)     : ", 0)
    total_bulan   = input_bulan(" Lama investasi (bulan)         : ")
    bunga_bulanan = (bunga_tahunan / 100) / 12
    sub_menu_tanpa_setoran(modal, bunga_bulanan, bunga_tahunan, total_bulan)

#Sub Menu Setoran Rutin
def sub_menu_setoran_rutin(setoran, bunga_bulanan, bunga_tahunan, total_bulan):
    from Irham_104 import garis, W, detail_pertumbuhan_setoran
    from Ghevira_103 import tabungan_setoran
    from Kayla_108 import cari_target_setoran
    saldo_skrg  = tabungan_setoran(setoran, bunga_bulanan, total_bulan)
    untung_skrg = tabungan_setoran(setoran, bunga_bulanan, total_bulan) - setoran * total_bulan
    modal_total = setoran * total_bulan

    while True:
        print()
        garis("-")
        print("HASIL INVESTASI DENGAN SETORAN RUTIN".center(W))
        garis("-")
        print(f"  {'Setoran per bulan':<30}: {rp_short(setoran)}")
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
            print("  [!] Pilihan tidak valid.")
