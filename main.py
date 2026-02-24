# MAIN
def main():
  import Abdilla_094.py
  import Ghevira_103.py
  import Irham_104.py
  import Kayla_108.py
  import Zahra_124.py
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
