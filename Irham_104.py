def garis(char="="):
    print(char * W)
    
#ditampilkan setelah memilih menu invest dengan setoran rutin -> submenu detail pertumbuhan dengan setoran
def detail_pertumbuhan_setoran(setoran, bunga_bulanan, bunga_tahunan, total_bulan):
    print()
    garis("=")
    print("  TABEL DETAIL PERTUMBUHAN SETORAN RUTIN".center(W))
    print(f"  Setoran: {rp_short(setoran)}/bln   |   Bunga: {bunga_tahunan}%/tahun   |   Durasi: {total_bulan} bulan".center(W))
    garis("=")
    header = f"  {'Bln':^4} | {'Setoran Bln':^18} | {'Total Disetor':^18} | {'Total Tabungan':^18} | {'Akum. Bunga':^16}"
    print(header)
    garis("-")

    for b in range(1, total_bulan + 1):
        saldo_b       = tabungan_setoran(setoran, bunga_bulanan, b)
        total_setor_b = setoran * b
        akum_bunga    = tabungan_setoran(setoran, bunga_bulanan, b) - setoran * b
        print(f"  {b:^4} | {rp_short(setoran):^18} | {rp_short(total_setor_b):^18} | {rp_short(saldo_b):^18} | {rp_short(akum_bunga):^16}")

    garis("-")
    saldo_akhir  = tabungan_setoran(setoran, bunga_bulanan, total_bulan)
    untung_akhir = tabungan_setoran(setoran, bunga_bulanan, total_bulan) - setoran * total_bulan
    total_setor  = setoran * total_bulan
    print(f"  {'TOTAL AKHIR':<8}   {rp_short(setoran):^18}   {rp_short(total_setor):^18}   {rp_short(saldo_akhir):^18}   {rp_short(untung_akhir):^16}")
    garis("=")
    input("\n  Tekan Enter untuk lanjut...")


