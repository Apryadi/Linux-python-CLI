# CLI-Craft

## Ini adalah versi bahasa Inggris dari readme Untuk versi bahasa Indonesia, Anda dapat memeriksa [Readme_EN](README.en.md).

Antarmuka Baris Perintah bertema Minecraft yang dibuat dengan Python yang memungkinkan Anda menavigasi dan memanipulasi sistem file menggunakan perintah gaya Minecraft.
```
 ██████╗██╗     ██╗      ██████╗██████╗  █████╗ ███████╗████████╗
██╔════╝██║     ██║     ██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
██║     ██║     ██║     ██║     ██████╔╝███████║█████╗     ██║   
██║     ██║     ██║     ██║     ██╔══██╗██╔══██║██╔══╝     ██║   
╚██████╗███████╗██║     ╚██████╗██║  ██║██║  ██║██║        ██║   
 ╚═════╝╚══════╝╚═╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝   
```

## Deskripsi

CLI-Craft mengubah antarmuka baris perintah biasa menjadi pengalaman bertema Minecraft. Menavigasi melalui direktori seolah-olah Anda sedang menjelajahi dunia Minecraft, membuat dan menghapus file seolah-olah Anda menempatkan dan menambang blok, dan mengelola sistem file Anda dengan perintah-perintah Minecraft yang sudah dikenal.
## Fitur

- Sistem perintah gaya Minecraft menggunakan awalan `/`
- Antarmuka seni ASCII
- Sistem pencapaian
- Manipulasi file dan direktori menggunakan terminologi Minecraft
- Tampilan pohon dari struktur direktori
- Fungsionalitas pencarian file
- Pencari berkas berdasarkan ukuran

## Persyaratan

- Python 3.6 atau lebih tinggi
- Sistem Operasi: Windows, Linux, atau MacOS

## Instalasi

1. Kloning repositori:
```bash
git clone https://github.com/yourusername/cli-craft.git
```

2. Arahkan ke direktori proyek:
```bash
cd cli-craft
```

3. Jalankan skrip:
```bash
python cli_craft.py
```

## Perintah

| Perintah | Deskripsi | Ekuivalen CLI Asli |
|---------|-------------|------------------------|
| `/look` | Menampilkan berkas di direktori saat ini | `ls` |
| `/tp <lokasi>` | Mengubah direktori | `cd` |
| `/coords` | Tampilkan jalur saat ini | `pwd` | | |/build

| `/destroy` | Menghapus direktori | `rmdir` | | | Menghapus direktori
| `/place <block>` | Membuat berkas | `touch` |
| `/dig <block>` | Menghapus berkas | `rm` | | | `/dig
| `/clone` | Menyalin berkas | `cp` |

| `/clear` | Menghapus layar | `clear` |
| `/map` | Menampilkan pohon direktori | `tree` | | | `/map` | | | `/map` | | Menampilkan pohon direktori
| `/temukan <item>` | Mencari file | `temukan` |
| `/besar <size>` | Menemukan file besar | - |
| `/prestasi` | Menampilkan prestasi secara acak | - |
| `/bantuan` | Menampilkan pesan bantuan | `bantuan` |
| `/quit` | Keluar dari CLI-Craft | `exit` |

Contoh Penggunaan ## Contoh Penggunaan

1. Menavigasi ke sebuah direktori:
```bash
World''. 2. Menuju ke direktori /home/user /> /tp Documents
```

2. Membuat daftar berkas di direktori saat ini:
```bash
World /home/user/Documents /> /look
```

3. Membuat direktori baru:
```bash
World: /home/user/Documents /> /build NewWorld
```

4. Membuat berkas baru:
```bash
World'': /home/user/Documents /> /place my_block.txt
```

5. Menyalin sebuah berkas:
```bash
World: /home/user/Documents /> /copy source.txt backup/source.txt
```

## Penanganan Kesalahan

CLI-Craft menyediakan pesan kesalahan yang jelas untuk masalah-masalah umum:
- File/direktori tidak ditemukan
- Izin ditolak
- Perintah tidak valid
- Argumen yang hilang

## Berkontribusi

1. Memotong (fork) repositori
2. Buat cabang fitur (`git checkout -b fitur/AmazingFeature`)
3. Komit perubahan Anda (`git commit -m 'Add some AmazingFeature'`)
4. Dorong ke cabang (`git push asal fitur/AmazingFeature`)
5. Buka Permintaan Tarik (Pull Request)

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat berkas [LICENSE](LICENSE) untuk detailnya.

## Ucapan Terima Kasih

- Terinspirasi oleh sistem perintah Minecraft
- Dibangun menggunakan pustaka standar Python
- Seni ASCII yang dibuat untuk antarmuka CLI-Craft

## Perbaikan di Masa Depan

- [ ] Menambahkan dukungan file konfigurasi
- [ ] Menerapkan pengeditan konten file
- [ ] Tambahkan lebih banyak fitur bertema Minecraft
- [ ] Membuat tema khusus
- [ ] Tambahkan dukungan multipemain
- [ ] Menerapkan manajemen izin file
- [ ] Tambahkan riwayat perintah

## Dukungan
Untuk dukungan, silakan buka masalah di repositori GitHub atau hubungi pengelola.
