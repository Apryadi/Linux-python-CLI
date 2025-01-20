import os
import sys
import shutil
import random
import time


def show_ascii_art():
    ascii_art = """
⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠘⠛⠛⠛⠛⠛⠛⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⠛⠛⠛
            ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣤⣤⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤⣤⣤⡄⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⡏⠉⠉⠉⠉⠉⠉⠉⠉⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀ ⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀
    """
    
    title_art = """
     ██████╗██╗     ██╗      ██████╗██████╗  █████╗ ███████╗████████╗
    ██╔════╝██║     ██║     ██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
    ██║     ██║     ██║     ██║     ██████╔╝███████║█████╗     ██║   
    ██║     ██║     ██║     ██║     ██╔══██╗██╔══██║██╔══╝     ██║   
    ╚██████╗███████╗██║     ╚██████╗██║  ██║██║  ██║██║        ██║   
     ╚═════╝╚══════╝╚═╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝   
    """
    print(ascii_art)
    print(title_art)

def show_help():
    print("\n=== CLI-Craft Commands ===")
    print("/dig <block>     - Mine a block (delete file)")
    print("/place <block>   - Place a block (create file)")
    print("/look           - Show blocks in current chunk (list files)")
    print("/tp <location>  - Teleport to location (change directory)")
    print("/coords        - Show current coordinates (show current path)")
    print("/build <struct> - Create a structure (create directory)")
    print("/destroy       - Destroy structure (remove directory)")
    print("/clone         - Clone blocks (copy files)")
    print("/move          - Move blocks (move files)")
    print("/clear         - Clear chat")
    print("/quit          - Leave the game")
    print("/map           - Show chunk structure (tree view)")
    print("/find <item>   - Find items in nearby chunks")
    print("/large <size>  - Find large structures")
    print("/achievement   - Show a random achievement")
    print("/help          - Show this help message")

def achievement():
    achievements = [
        "Achievement Get! /First Command/",
        "Achievement Get! /Master Builder/",
        "Achievement Get! /Explorer/",
        "Achievement Get! /Block Breaker/",
        "Achievement Get! /Organization Expert/"
    ]
    achievement = random.choice(achievements)
    print(f"\n{'='*len(achievement)}")
    print(achievement)
    print(f"{'='*len(achievement)}")

def find_large(size):
    size_bytes = int(size) * 1024 * 1024  # Convert MB to Bytes
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            path = os.path.join(root, file)
            if os.path.getsize(path) > size_bytes:
                print(f"{path} ({os.path.getsize(path)} bytes)")

def search(pattern):
    for root, dirs, files in os.walk(os.getcwd()):
        for name in dirs + files:
            if pattern in name:
                print(os.path.join(root, name))
                
def tree(directory, prefix=""):
    items = os.listdir(directory)
    for i, item in enumerate(items):
        path = os.path.join(directory, item)
        connector = "└──" if i == len(items) - 1 else "├──"
        print(f"{prefix}{connector} {item}")
        if os.path.isdir(path):
            extension = "    " if i == len(items) - 1 else "│   "
            tree(path, prefix + extension)
            
def main():
    while True:
        try:
            command = input(f"World: {os.getcwd()} /> ").strip()
            if not command:
                continue

            args = command.split()
            cmd = args[0]

            if cmd == "/look":
                print("\nBlocks in current chunk:")
                print("\n".join(f"- {item}" for item in os.listdir()))

            elif cmd == "/coords":
                print(f"Current coordinates: {os.getcwd()}")

            elif cmd == "/tp":
                if len(args) < 2:
                    print("Error: Where do you want to teleport?")
                else:
                    try:
                        os.chdir(args[1])
                        print(f"Teleported to {args[1]}")
                    except FileNotFoundError:
                        print(f"Cannot teleport to '{args[1]}': Location not found")

            elif cmd == "/build":
                if len(args) < 2:
                    print("Error: What structure do you want to build?")
                else:
                    try:
                        os.mkdir(args[1])
                        print(f"Built structure: {args[1]}")
                    except FileExistsError:
                        print(f"Structure '{args[1]}' already exists")

            elif cmd == "/destroy":
                if len(args) < 2:
                    print("Error: Which structure to destroy?")
                else:
                    try:
                        os.rmdir(args[1])
                        print(f"Structure destroyed: {args[1]}")
                    except FileNotFoundError:
                        print(f"Structure '{args[1]}' not found")
                    except OSError:
                        print(f"Cannot destroy '{args[1]}': Structure not empty")

            elif cmd == "/place":
                if len(args) < 2:
                    print("Error: Which block to place?")
                else:
                    try:
                        with open(args[1], 'w') as f:
                            pass
                        print(f"Placed block: {args[1]}")
                    except Exception as e:
                        print(f"Cannot place block: {e}")

            elif cmd == "/dig":
                if len(args) < 2:
                    print("Error: Which block to dig?")
                else:
                    try:
                        os.remove(args[1])
                        print(f"Block mined: {args[1]}")
                    except FileNotFoundError:
                        print(f"Block '{args[1]}' not found")

            elif cmd == "/clone":
                if len(args) < 3:
                    print("Error: Specify source and destination")
                else:
                    try:
                        shutil.copy(args[1], args[2])
                        print(f"Cloned {args[1]} to {args[2]}")
                    except FileNotFoundError:
                        print(f"Block '{args[1]}' not found")
                    except Exception as e:
                        print(f"Clone failed: {e}")

            elif cmd == "/move":
                if len(args) < 3:
                    print("Error: Specify source and destination")
                else:
                    try:
                        shutil.move(args[1], args[2])
                        print(f"Moved {args[1]} to {args[2]}")
                    except FileNotFoundError:
                        print(f"'{args[1]}' not found")
                    except Exception as e:
                        print(f"Move failed: {e}")

            elif cmd == "/clear":
                os.system('cls' if os.name == 'nt' else 'clear')
                show_ascii_art()

            elif cmd == "/map":
                print("\nChunk Structure:")
                tree(os.getcwd())

            elif cmd == "/find":
                if len(args) < 2:
                    print("Error: What are you looking for?")
                else:
                    print(f"Searching for {args[1]}...")
                    search(args[1])

            elif cmd == "/large":
                if len(args) < 2:
                    print("Error: Specify size in MB")
                else:
                    print(f"Finding large structures...")
                    find_large(args[1])

            elif cmd == "/achievement":
                achievement()

            elif cmd == "/help":
                show_help()

            elif cmd == "/quit":
                print("\nThanks for playing CLI-Craft! See you soon!")
                time.sleep(1)
                sys.exit()

            else:
                print(f"Unknown command: '{cmd}'. Type /help for help.")

        except KeyboardInterrupt:
            print("\nUse /quit to leave the game")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    show_ascii_art()
    print("Welcome to CLI-Craft! Type /help for available commands.")
    main()