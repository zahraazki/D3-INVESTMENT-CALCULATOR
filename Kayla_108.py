<<<<<<< 108_Kayla
def tabungan_tanpa_setoran(a, bunga, bulan):
    return a * (1 + bunga) ** bulan

def sub_menu_tanpa_setoran(modal, bunga_bulanan, bunga_tahunan, total_bulan):
    from Irham_104 import garis, W
    from Zahra_124 import rp_short
    from Ghevira_103 import detail_pertumbuhan_tanpa_setoran
    from Abdilla_094 import cari_target_tanpa_setoran
=======
#menu tabungan tanpa setoran
def tabungan_tanpa_setoran(a, bunga, bulan):
    return a * (1 + bunga) ** bulan

#menu hasil investasi tanpa setoran
def sub_menu_tanpa_setoran(modal, bunga_bulanan, bunga_tahunan, total_bulan):
    """Sub-menu lanjutan setelah input menu 1"""
>>>>>>> main
    saldo_skrg  = tabungan_tanpa_setoran(modal, bunga_bulanan, total_bulan)
    untung_skrg = tabungan_tanpa_setoran(modal, bunga_bulanan, total_bulan) - modal

    while True:
        print()
        garis("-")
        print("  HASIL INVESTASI TANPA SETORAN RUTIN".center(W))
        garis("-")
        print(f"  {'Modal awal':<30}: {rp_short(modal)}")
        print(f"  {'Bunga per tahun':<30}: {bunga_tahunan}%")
        print(f"  {'Lama investasi':<30}: {total_bulan} bulan")
        garis("-")
        print(f"  {'Total uang saat ini':<30}: {rp_short(saldo_skrg)}")
        print(f"  {'Total keuntungan (bunga)':<30}: {rp_short(untung_skrg)}")
        garis("=")
        print()
        print("  SUB-MENU:")
        print("  [1] Lihat detail pertumbuhan uang (range bulan)")
        print("  [2] Lihat berapa bulan target tabungan tercapai")
        print("  [0] Kembali ke menu utama")
        print()
        pilihan = input("  Pilih: ").strip()

        if pilihan == "1":
            detail_pertumbuhan_tanpa_setoran(modal, bunga_bulanan, total_bulan)
        elif pilihan == "2":
            cari_target_tanpa_setoran(modal, bunga_bulanan)
        elif pilihan == "0":
            break
        else:
            print("  [!] Pilihan tidak valid.")

<<<<<<< 108_Kayla
def cari_target_setoran(setoran, bunga_bulanan):
    from Irham_104 import garis, W
    from Zahra_124 import rp_short
    from Ghevira_103 import tabungan_setoran
    from Abdilla_094 import input_angka
=======
#menu mengecek target setoran
def cari_target_setoran(setoran, bunga_bulanan):
>>>>>>> main
    print()
    garis("-")
    print("  CEK TARGET TABUNGAN".center(W))
    garis("-")
    target = input_angka("  Masukkan target saldo (Rp): ", 1)

    bulan_target = None
    saldo_target = None
    for b in range(1, 12 * 100 + 1):
        saldo = tabungan_setoran(setoran, bunga_bulanan, b)
        if saldo >= target:
            bulan_target = b
            saldo_target = saldo
            break

    print()
    garis("=")
    print("  HASIL CEK TARGET".center(W))
    garis("=")
    print(f"  {'Setoran per bulan':<30}: {rp_short(setoran)}")
    print(f"  {'Target saldo':<30}: {rp_short(target)}")
    garis("-")
    if bulan_target:
        tahun  = bulan_target // 12
        sisa   = bulan_target % 12
        durasi = f"{tahun} tahun {sisa} bulan" if tahun > 0 else f"{sisa} bulan"
        total_setor = setoran * bulan_target
        print(f"  {'Target tercapai pada bulan ke':<30}: {bulan_target}")
        print(f"  {'Setara dengan':<30}: {durasi}")
        print(f"  {'Total uang pada bulan tersebut':<30}: {rp_short(saldo_target)}")
        print(f"  {'Total uang yang disetor':<30}: {rp_short(total_setor)}")
        print(f"  {'Total keuntungan saat itu':<30}: {rp_short(saldo_target - total_setor)}")
    else:
        print("  [!] Target tidak tercapai dalam 100 tahun dengan kondisi ini.")
    garis("=")
<<<<<<< 108_Kayla
    input("\n  Tekan Enter untuk lanjut...")
=======

    input("\n  Tekan Enter untuk lanjut...")

>>>>>>> main
