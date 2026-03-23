import os
import time

SIZE = 7

map_grid = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", "P", ".", ".", ".", "I", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", "D", "#"],  # D = Door (keluar)
    ["#", "#", "#", "#", "#", "#", "#"],
]

player_pos = [1, 1]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_map():
    for row in map_grid:
        print(" ".join(row))

def story_intro():
    print("Lampu pecah berkedip...")
    time.sleep(2)
    print("Berusaha menerangi ruangan yang gelap...")
    time.sleep(2)
    print("Seorang anak terbangun di kamar...")
    time.sleep(2)
    print("\nKamar itu berantakan...\n")
    input("Tekan ENTER untuk lanjut...")

def story_encounter():
    clear()
    print("Seorang perempuan terlihat di meja makan...")
    time.sleep(2)
    print("Seperti sedang mabuk...\n")
    time.sleep(2)

    print("WOSHH!!")
    time.sleep(1)
    print("PRANGG!!")
    time.sleep(2)

    print("\nBotol kaca hampir mengenai kamu...\n")
    input("...")

    print('I : "ka..kamu.. sudah bangun ya??"')
    time.sleep(2)

    print("\nDia mulai mendekat...\n")
    time.sleep(2)

    print('I : "JAWAB AKU ANAK SIALAN"')
    time.sleep(1)
    print("PLAK!!")
    time.sleep(2)

    print("\nPipi kamu terasa sakit...\n")
    time.sleep(2)

    print('I : "sekarang.. belikan aku rokok.."')
    time.sleep(2)

    print('I : "CEPAT!!"')
    time.sleep(2)

    input("\nKamu harus keluar rumah...")

def move_player(dx, dy):
    global player_pos

    x, y = player_pos
    new_x = x + dx
    new_y = y + dy

    target = map_grid[new_x][new_y]

    if target != "#":
        map_grid[x][y] = "."
        player_pos = [new_x, new_y]
        map_grid[new_x][new_y] = "P"

        return target
    return None

def game_loop():
    encountered = False

    while True:
        clear()
        print_map()

        move = input("\nGerak (W/A/S/D): ").lower()

        if move == "w":
            tile = move_player(-1, 0)
        elif move == "s":
            tile = move_player(1, 0)
        elif move == "a":
            tile = move_player(0, -1)
        elif move == "d":
            tile = move_player(0, 1)
        else:
            continue

        if tile == "I" and not encountered:
            encountered = True
            story_encounter()

        if tile == "D":
            clear()
            print("Kamu keluar dari rumah...\n")
            print("Malam terasa sunyi...\n")
            print("Tugasmu: membeli rokok...\n")
            print("== TO BE CONTINUED ==")
            break

story_intro()
game_loop()
