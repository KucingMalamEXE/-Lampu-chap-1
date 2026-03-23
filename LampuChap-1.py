import time
import os

def clear():
    os.system("clear")

def delay(text, speed=0.04):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(speed)
    print()

def wait():
    input("\n[ENTER]...")

def draw_corridor(step):
    clear()

    width = 21
    middle = [" "] * width
    middle[step] = "P"

    top = ["N"," ","N"," ","B"," ","N"," ","N"," ","N"," ","B"," ","N"," ","N"," ","N"," ","N"]
    bottom = ["N"," ","N"," ","N"," ","N"," ","B"," ","N"," ","N"," ","N"," ","B"," ","N"," ","N"]

    print("=== LORONG SEKOLAH ===\n")

    print("".join(top))
    print("".join(middle))
    print("".join(bottom))

    print("\nP = Kamu")

def corridor_scene():
    delay("Lampu sorot menyinari satu anak...", 0.05)
    delay("Dia berjalan menyusuri lorong sekolah...", 0.05)
    wait()

    for i in range(3):
        draw_corridor(i + 2)
        delay("Langkah terasa berat...", 0.05)
        time.sleep(1)

    clear()
    delay("Riuh bisik mulai terdengar...", 0.05)
    print()

    time.sleep(1)
    print('N : "kemarin seru ya"')
    time.sleep(2)
    print('N : "iya, sepulang sekolah mau main lagi?"')
    time.sleep(2)
    print('B : "lihat anak itu, kotor sekali, pasti orang tua nya tidak peduli"')
    time.sleep(2)
    print('N : "Boleh"')
    time.sleep(2)
    print('B : "orang tua dia itu pecandu dulu nya loh.."')

    wait()

def classroom_scene():
    clear()

    delay("Anak itu terus berjalan...", 0.05)
    delay("Dan memasuki kelas.", 0.05)
    wait()

    clear()

    print("=== KELAS ===\n")

    print("N   N   N   N   N")
    print("N   N   N   N   N")
    print("N   N   P   N   N")
    print("N   N   N   N   N")
    print("N   N   N   N   N")

    print()

    delay("Dia duduk di bangkunya...", 0.05)
    delay("Suasana terasa berbeda...", 0.05)
    delay("Sunyi...", 0.08)
    delay("Terlalu sunyi...", 0.08)

    time.sleep(2)

    delay("\nWush....", 0.1)
    time.sleep(1)
    delay("BUKK!!", 0.2)

    delay("\nSebuah buku mengenai kepalanya.", 0.05)

    wait()

def main():
    corridor_scene()
    classroom_scene()

    clear()
    delay("...", 0.2)
    time.sleep(1)
    delay("To be continued.", 0.1)

if __name__ == "__main__":
    main()
