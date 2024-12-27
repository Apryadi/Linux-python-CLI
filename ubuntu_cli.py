import os
import sys
import shutil
import random

# Fungsi untuk menampilkan bantuan
def show_help():
    print("\nDaftar Perintah CLI Linux yang Didukung:")
    print("ls       - Menampilkan daftar file dan folder di direktori saat ini")
    print("pwd      - Menampilkan direktori kerja saat ini")
    print("cd <dir> - Mengubah direktori kerja")
    print("mkdir <dir> - Membuat direktori baru")
    print("rmdir <dir> - Menghapus direktori (jika kosong)")
    print("touch <file> - Membuat file kosong baru")
    print("rm <file> - Menghapus file")
    print("cp <src> <dest> - Menyalin file dari satu lokasi ke lokasi lain")
    print("mv <src> <dest> - Memindahkan atau mengganti nama file/direktori")
    print("clear    - Membersihkan layar terminal")
    print("exit     - Keluar dari CLI")
    print("search <pattern> - Mencari file atau direktori berdasarkan nama")
    print("tree     - Menampilkan struktur direktori dalam bentuk pohon")
    print("find_large <size> - Menampilkan file yang lebih besar dari ukuran tertentu")
    print("log <command> - Menyimpan riwayat penggunaan command ke file log")
    print("joke     - Menampilkan lelucon acak untuk hiburan")

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk mencari file atau direktori berdasarkan nama
def search(pattern):
    for root, dirs, files in os.walk(os.getcwd()):
        for name in dirs + files:
            if pattern in name:
                print(os.path.join(root, name))

# Fungsi untuk menampilkan struktur direktori dalam bentuk pohon
def tree(directory, prefix=""):
    items = os.listdir(directory)
    for i, item in enumerate(items):
        path = os.path.join(directory, item)
        connector = "└──" if i == len(items) - 1 else "├──"
        print(f"{prefix}{connector} {item}")
        if os.path.isdir(path):
            extension = "    " if i == len(items) - 1 else "│   "
            tree(path, prefix + extension)

# Fungsi untuk menemukan file lebih besar dari ukuran tertentu
def find_large(size):
    size_bytes = int(size) * 1024 * 1024  # Convert MB to Bytes
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            path = os.path.join(root, file)
            if os.path.getsize(path) > size_bytes:
                print(f"{path} ({os.path.getsize(path)} bytes)")

# Fungsi untuk menyimpan command ke file log
def log_command(command):
    with open("command_log.txt", "a") as log_file:
        log_file.write(command + "\n")

# Fungsi untuk menampilkan lelucon acak
def joke():
    jokes = [
        "Kenapa programmer suka kopi? Karena tanpa kopi, mereka akan 'java' tidur.",
        "Apa makanan favorit developer? Spaghetti code!",
        "Kenapa komputer tidak pernah lapar? Karena sudah punya banyak 'byte'."
    ]
    print(random.choice(jokes))

# Fungsi utama CLI
def main():
    while True:
        try:
            command = input(f"{os.getcwd()} $ ").strip()
            if not command:
                continue

            args = command.split()
            cmd = args[0]

            log_command(command)  # Log setiap perintah

            if cmd == "ls":
                print("\n".join(os.listdir()))

            elif cmd == "pwd":
                print(os.getcwd())

            elif cmd == "cd":
                if len(args) < 2:
                    print("Error: Direktori tidak disebutkan")
                else:
                    try:
                        os.chdir(args[1])
                    except FileNotFoundError:
                        print(f"Error: Direktori '{args[1]}' tidak ditemukan")

            elif cmd == "mkdir":
                if len(args) < 2:
                    print("Error: Nama direktori tidak disebutkan")
                else:
                    try:
                        os.mkdir(args[1])
                    except FileExistsError:
                        print(f"Error: Direktori '{args[1]}' sudah ada")

            elif cmd == "rmdir":
                if len(args) < 2:
                    print("Error: Nama direktori tidak disebutkan")
                else:
                    try:
                        os.rmdir(args[1])
                    except FileNotFoundError:
                        print(f"Error: Direktori '{args[1]}' tidak ditemukan")
                    except OSError:
                        print(f"Error: Direktori '{args[1]}' tidak kosong")

            elif cmd == "touch":
                if len(args) < 2:
                    print("Error: Nama file tidak disebutkan")
                else:
                    try:
                        with open(args[1], 'w') as f:
                            pass
                    except Exception as e:
                        print(f"Error: {e}")

            elif cmd == "rm":
                if len(args) < 2:
                    print("Error: Nama file tidak disebutkan")
                else:
                    try:
                        os.remove(args[1])
                    except FileNotFoundError:
                        print(f"Error: File '{args[1]}' tidak ditemukan")

            elif cmd == "cp":
                if len(args) < 3:
                    print("Error: Sumber atau tujuan tidak disebutkan")
                else:
                    try:
                        shutil.copy(args[1], args[2])
                    except FileNotFoundError:
                        print(f"Error: File '{args[1]}' tidak ditemukan")
                    except Exception as e:
                        print(f"Error: {e}")

            elif cmd == "mv":
                if len(args) < 3:
                    print("Error: Sumber atau tujuan tidak disebutkan")
                else:
                    try:
                        shutil.move(args[1], args[2])
                    except FileNotFoundError:
                        print(f"Error: File atau direktori '{args[1]}' tidak ditemukan")
                    except Exception as e:
                        print(f"Error: {e}")

            elif cmd == "clear":
                clear_screen()

            elif cmd == "search":
                if len(args) < 2:
                    print("Error: Pola pencarian tidak disebutkan")
                else:
                    search(args[1])

            elif cmd == "tree":
                tree(os.getcwd())

            elif cmd == "find_large":
                if len(args) < 2:
                    print("Error: Ukuran file tidak disebutkan")
                else:
                    find_large(args[1])

            elif cmd == "log":
                if len(args) < 2:
                    print("Error: Command untuk log tidak disebutkan")
                else:
                    log_command(" ".join(args[1:]))
                    print("Command telah dicatat ke file log.")

            elif cmd == "joke":
                joke()

            elif cmd == "help":
                show_help()

            elif cmd == "exit":
                print("Keluar dari CLI. Sampai jumpa!")
                sys.exit()

            else:
                print(f"Error: Perintah '{cmd}' tidak dikenal")

        except KeyboardInterrupt:
            print("\nGunakan 'exit' untuk keluar dari CLI.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    clear_screen()
    print("Selamat datang di Python CLI. Ketik 'help' untuk melihat daftar perintah.")
    main()
