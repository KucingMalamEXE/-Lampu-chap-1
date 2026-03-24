Vinos
import time

SIZE = 7

player_pos = [6, 3]
npc_pos = [2, 3]
step_count = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=2):
    print(text)
    time.sleep(delay)

def next_scene():
    input("\n(Enter untuk lanjut ke scene berikutnya...)")

def draw_map(show_npc=False):
    for i in range(SIZE):
        for j in range(SIZE):
            if [i, j] == player_pos and [i, j] == npc_pos:
                print("X", end=" ")
            elif [i, j] == player_pos:
                print("P", end=" ")
            elif show_npc and [i, j] == npc_pos:
                print("N", end=" ")
            else:
                print(".", end=" ")
        print()
    print("\nGunakan 'W' untuk maju")

def intro_story():
    clear()
    slow_print("Dingin malam menusuk kulit")
    slow_print("Seorang anak yang malang")
    slow_print("Berjalan menembus gelap malam")
    slow_print("Terang bulan menerangi jalan")
    slow_print("Dengan lampu redup")
    slow_print("Berusaha menerangi")

    slow_print("\n...")
    slow_print("Disebuah pertigaan")
    slow_print("Tanpa melihat jalan")

    next_scene()

def movement():
    global step_count

    while True:
        clear()
        draw_map()

        move = input("Input: ").strip().lower()

        if move == "w":
            if step_count == 3:
                player_pos[0] = npc_pos[0]
                break

            if player_pos[0] > 0:
                player_pos[0] -= 1
                step_count += 1
        else:
            print("Gunakan 'W' untuk maju!")
            time.sleep(1)

def collision_scene():
    clear()
    draw_map(show_npc=True)
    time.sleep(1.5)

    slow_print("\nBUGHH!!", 1.5)
    slow_print("P menabrak seseorang", 2)

    next_scene()

def after_collision():
    clear()
    slow_print("...")
    slow_print("Melihat orang tersebut")
    slow_print("Dengan perasaan malu")
    slow_print("Dan rasa bersalah")
    slow_print("Itu adalah anak seusianya")

    next_scene()

def dialog_scene():
    clear()

    slow_print('N : "kamu gapapa?"')
    slow_print('P : "..."')
    slow_print('N : *bingung*')
    slow_print('P : *bingung*')
    slow_print('N : "kamu baik-baik saja?"')
    slow_print('P : "..."')
    slow_print('N : "kamu bisa berbicara?"')
    slow_print('P : *terdiam.. sebelum mengangguk*')
    slow_print('N : "ohh.. begitu ya.."')

    slow_print("\nRasa canggung diantara mereka")

    slow_print('N : "omong-omong.."')
    slow_print('N : "kenalin aku Vina" ')
    slow_print('V : "kamu bisa panggil aku vin"')
    slow_print('P : "..."')
    slow_print('V : *merasa canggung*')
    slow_print('V : "Nama mu?"')
    slow_print('P : *tak menjawab*')
    slow_print('V : "baiklah akan ku panggil kamu.."')
    slow_print('V : *berfikir dengan keras*')
    slow_print('V : "akan ku panggil.. Fai"')
    slow_print('F : *melihat Vin penuh penasaran*')
    slow_print('V : "bagaimana?"')

    next_scene()

    print("\n=== TO BE CONTINUE ===")

def main():
    intro_story()
    movement()
    collision_scene()
    after_collision()
    dialog_scene()

if __name__ == "__main__":
    main()
