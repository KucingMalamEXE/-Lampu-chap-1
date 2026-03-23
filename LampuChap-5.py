import time
import os

SIZE = 7

# posisi awal (lebih tengah)
player_pos = [3, 2]
npc_pos = [3, 3]

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def delay(text, speed=0.04):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(speed)
    print()

def wait():
    input("\n[ENTER]...")

def draw_grid():
    grid = [["." for _ in range(SIZE)] for _ in range(SIZE)]

    grid[player_pos[0]][player_pos[1]] = "P"
    grid[npc_pos[0]][npc_pos[1]] = "N"

    print("=== SCENE ===\n")
    for row in grid:
        print(" ".join(row))
    print("\nP = Kamu | N = Guru\n")

def scene_awal():
    clear()

    delay("Guru itu melihatnya...")
    delay("Dengan perasaan kasihan...")
    delay("Mengetahui hal apa..")
    delay("Yang dialaminya...")
    delay("Sebelum...")
    wait()

    clear()
    draw_grid()

    time.sleep(1)
    print('\nN : "kamu butuh sesuatu nak?"')
    time.sleep(2)
    print('P : *hanya terdiam*')
    time.sleep(2)
    print('N : "hm.. ikut ibu ya"')
    time.sleep(2)
    print('P : *masih terdiam*')
    time.sleep(2)
    print('N : "ayok"')

    wait()

def scene_ranjang():
    clear()

    delay("Membantu anak itu...")
    delay("Untuk turun dari ranjang...")
    delay("Bekas dia tertidur...")
    delay("Tidak sadarkan diri...")

    wait()

def move_right(steps=1):
    for _ in range(steps):
        if player_pos[1] < SIZE - 2:
            player_pos[1] += 1
            npc_pos[1] += 1

        clear()
        draw_grid()
        time.sleep(0.8)

def scene_lorong():
    clear()

    delay("Berjalan bersama...")
    delay("Menyusuri lorong...")
    delay("Yang disinari cahaya...")
    delay("Sinar sore hari...")
    wait()

    move_right(3)

    print()
    time.sleep(1)

    print('N : "omong-omong"')
    time.sleep(2)
    print('N : "apakah ibu mu sudah membaik?"')
    time.sleep(2)
    print('P : *hanya merenung*')
    time.sleep(2)
    print('N : "jika tidak salah.."')
    time.sleep(2)
    print('N : "bulan lalu, ibu mu sudah pulang ya?"')

    delay("\nP hanya bisa terdiam...")
    delay("Meremas ujung rok nya...")
    delay("Dengan menahan emosi...")

    wait()

def scene_bicara():
    clear()

    delay("Guru itu menyadari...")
    delay("Kegelisahan muridnya...")
    delay("Dengan cepat...")
    delay("Merubah pembicaraan...")
    wait()

    print('N : "nilai mu dalam sosial.."')
    time.sleep(2)
    print('N : "tinggi sekali"')
    time.sleep(2)
    print('P : *hanya terdiam*')
    time.sleep(2)
    print('N : "seperti nya kamu anak.."')
    time.sleep(2)
    print('N : "yang suka mengamati"')
    time.sleep(2)
    print('N : "ibu rasa.. kamu pendengar yang baik"')
    time.sleep(2)
    print('N : "mungkin akan menjadi psikiater"')

    delay("\nP terpaku diam...")
    delay("Di tengah langkahnya...")
    delay("Diam-diam tertarik...")

    wait()

def scene_pintu():
    move_right(2)

    clear()

    delay("Mereka berhenti...")
    delay("Di depan pintu kepala sekolah...")
    wait()

    delay("Pintu dibuka...")
    delay("Terlihat kepala sekolah...")
    delay("Dan seorang anak...")
    delay("Dengan orang tua...")
    delay("Orang tua P juga ada disana...")

    wait()

def scene_akhir():
    clear()

    grid = [["." for _ in range(SIZE)] for _ in range(SIZE)]

    grid[3][2] = "P"
    grid[3][4] = "N"
    grid[3][5] = "A"  # anak lain

    print("=== RUANGAN ===\n")
    for row in grid:
        print(" ".join(row))

    print("\nP = Kamu | N = Guru | A = Anak lain\n")

    delay("Terlihat anak tersebut...")
    delay("Menatap P...")
    delay("Dengan tersenyum...")

    time.sleep(2)
    delay("\n...")
    time.sleep(1)
    delay("To be continued.")

def main():
    scene_awal()
    scene_ranjang()
    scene_lorong()
    scene_bicara()
    scene_pintu()
    scene_akhir()

if __name__ == "__main__":
    main()
