def garis(char="="):
    print(char * W)

def detail_pertumbuhan_tanpa_setoran(modal, bunga_bulanan, total_bulan):
    print()
    garis("-")
    print("  DETAIL PERTUMBUHAN (RANGE BULAN)".center(W))
    garis("-")
    print(f"  Total bulan investasi: {total_bulan} bulan")
    bulan_awal = input_bulan("  Tampilkan dari bulan ke  : ")
    bulan_akhir = input_bulan("  Tampilkan sampai bulan ke: ")

    if bulan_awal > bulan_akhir:
        print("  [!] Bulan awal tidak boleh lebih besar dari bulan akhir.")
        return
    if bulan_akhir > total_bulan:
        print(f"  [!] Melebihi batas investasi ({total_bulan} bulan), disesuaikan otomatis.")
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

# MAIN

def main():
    while True:
        print()
        garis("=")
        print("  KALKULATOR INVESTASI CERDAS".center(W))
        garis("=")
        print()
        print("  [1] Tabungan Investasi Tanpa Setoran Rutin")
        print("  [2] Tabungan Investasi Dengan Setoran Rutin")
        print("  [0] Keluar")
        print()
        pilihan = input("  Pilih menu: ").strip()

        if pilihan == "1":
            menu_tanpa_setoran()
        elif pilihan == "2":
            menu_setoran_rutin()
        elif pilihan == "0":
            print()
            garis()
            print("  Terima kasih. Semoga investasimu sukses!".center(W))
            garis()
            print()
            break
        else:
            print("  [!] Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
