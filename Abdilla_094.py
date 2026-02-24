def input_angka(prompt, min_val=0):
    while True:
        try:
            val = float(input(prompt))
            if val < min_val:
                print(f"  [!] Nilai harus >= {min_val}")
                continue
            return val
        except ValueError:
            print("  [!] Masukkan angka yang valid!")

def cari_target_tanpa_setoran(modal, bunga_bulanan):
    from Irham_104 import garis, W
    from Zahra_124 import rp_short
    from Kayla_108 import tabungan_tanpa_setoran
    print()
    garis("-")
    print("  CEK TARGET TABUNGAN".center(W))
    garis("-")
    target = input_angka("  Masukkan target saldo (Rp): ", 1)

    bulan_target = None
    saldo_target = None
    for b in range(1, 12 * 100 + 1):
        saldo = tabungan_tanpa_setoran(modal, bunga_bulanan, b)
        if saldo >= target:
            bulan_target = b
            saldo_target = saldo
            break

    print()
    garis("=")
    print("  HASIL CEK TARGET".center(W))
    garis("=")
    print(f"  {'Modal awal':<30}: {rp_short(modal)}")
    print(f"  {'Target saldo':<30}: {rp_short(target)}")
    garis("-")
    if bulan_target:
        tahun  = bulan_target // 12
        sisa   = bulan_target % 12
        durasi = f"{tahun} tahun {sisa} bulan" if tahun > 0 else f"{sisa} bulan"
        print(f"  {'Target tercapai pada bulan ke':<30}: {bulan_target}")
        print(f"  {'Setara dengan':<30}: {durasi}")
        print(f"  {'Total uang pada bulan tersebut':<30}: {rp_short(saldo_target)}")
        print(f"  {'Total keuntungan saat itu':<30}: {rp_short(saldo_target - modal)}")
    else:
        print("  [!] Target tidak tercapai dalam 100 tahun dengan kondisi ini.")
    garis("=")
    input("\n  Tekan Enter untuk lanjut...")

def menu_setoran_rutin():
    from Irham_104 import garis, W
    from Ghevira_103 import input_bulan
    from Zahra_124 import sub_menu_setoran_rutin
    print()
    garis("=")
    print("  TABUNGAN INVESTASI DENGAN SETORAN RUTIN  ".center(W))
    garis("=")
    setoran       = input_angka("  Setoran per bulan (Rp)       : ", 1)
    bunga_tahunan = input_angka("  Bunga/return per tahun (%)   : ", 0)
    total_bulan   = input_bulan("  Lama investasi (bulan)       : ")
    bunga_bulanan = (bunga_tahunan / 100) / 12
    sub_menu_setoran_rutin(setoran, bunga_bulanan, bunga_tahunan, total_bulan)
