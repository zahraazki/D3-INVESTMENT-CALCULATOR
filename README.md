# D3 Investment Calculator

Aplikasi kalkulator investasi berbasis CLI (Command Line Interface) yang dibuat menggunakan Python. Program ini membantu menghitung pertumbuhan investasi dengan dua mode: tanpa setoran rutin dan dengan setoran rutin bulanan.

---

## Fitur

- **Investasi Tanpa Setoran Rutin**, Menghitung pertumbuhan modal awal berdasarkan bunga/return per tahun
- **Investasi Dengan Setoran Rutin**, Menghitung akumulasi tabungan dengan setoran bulanan tetap
- **Detail Pertumbuhan Per Bulan**, Mengeluarkan tabel pertumbuhan uang per bulan dalam rentang tertentu
- **Cek Target Tabungan**, Cari tahu berapa bulan yang dibutuhkan untuk mencapai target saldo

---

## Cara Menjalankan

### Prasyarat
- Python 3.x

### Langkah

```bash
# 1. Clone repository
git clone https://github.com/username/D3-INVESTMENT-CALCULATOR.git
cd D3-INVESTMENT-CALCULATOR

# 2. Jalankan program
python main.py
```

Tidak ada dependencies eksternal — hanya menggunakan Python standar.

---

## Struktur File

| File | Kontributor | Isi |
|---|---|---|
| `main.py` | — | Entry point program, menampilkan menu utama |
| `Irham_104.py` | Irham | Konstanta lebar tampilan (`W`), fungsi `garis()`, tabel detail pertumbuhan setoran rutin |
| `Abdilla_094.py` | Abdillah | Fungsi `input_angka()`, cek target tanpa setoran, menu investasi dengan setoran rutin |
| `Ghevira_103.py` | Ghevira | Fungsi `input_bulan()`, rumus tabungan setoran, tabel detail pertumbuhan tanpa setoran |
| `Kayla_108.py` | Kayla | Rumus tabungan tanpa setoran, sub-menu tanpa setoran, cek target setoran rutin |
| `Zahra_124.py` | Zahra | Format rupiah (`rp_short()`), menu tanpa setoran, sub-menu setoran rutin |

---

## Cara Penggunaan

Setelah program dijalankan, pilih menu:

```
[1] Tabungan Investasi Tanpa Setoran Rutin
[2] Tabungan Investasi Dengan Setoran Rutin
[0] Keluar
```

**Menu 1 — Tanpa Setoran Rutin:**
- Masukkan modal awal, bunga per tahun, dan lama investasi (bulan)
- Program akan menampilkan total uang dan keuntungan
- Sub-menu: lihat detail pertumbuhan per bulan atau cek kapan target tercapai

**Menu 2 — Dengan Setoran Rutin:**
- Masukkan setoran per bulan, bunga per tahun, dan lama investasi
- Program akan menampilkan total tabungan dan akumulasi bunga
- Sub-menu: lihat detail pertumbuhan per bulan atau cek kapan target tercapai

---

## Rumus yang Digunakan

**Tanpa setoran rutin (bunga majemuk):**
```
Total = Modal × (1 + bunga_bulanan)^bulan
```

**Dengan setoran rutin:**
```
Total = Setoran × ((1 + bunga_bulanan)^bulan - 1) / bunga_bulanan
```

---

## Anggota Tim

| NIM | Nama |
|---|---|
| 094 | Abdilla |
| 103 | Ghevira |
| 104 | Irham |
| 108 | Kayla |
| 124 | Zahra |
