import time
import os

SIZE = 7

# posisi karakter
hana_pos = [3, 1]
vina_pos = [3, 2]
npc_pos  = [3, 5]
aku_pos  = [5, 5]   # "seseorang" di akhir

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def delay(text, speed=0.045):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(speed)
    print()

def wait():
    input("\n[ENTER untuk lanjut]...")

# ─────────────────────────────────────────────
# GRID HELPERS
# ─────────────────────────────────────────────

def make_grid(markers: dict) -> list:
    """markers = { (row,col): char }"""
    grid = [["." for _ in range(SIZE)] for _ in range(SIZE)]
    for (r, c), ch in markers.items():
        if 0 <= r < SIZE and 0 <= c < SIZE:
            grid[r][c] = ch
    return grid

def print_grid(grid, legend="H=Hana  V=Vina"):
    print("╔" + "═══" * SIZE + "╗")
    for row in grid:
        print("║ " + "  ".join(row) + " ║")
    print("╚" + "═══" * SIZE + "╝")
    print(f"  {legend}\n")

def show_scene(markers, legend="H=Hana  V=Vina", title="MALAM"):
    clear()
    print(f"=== {title} ===\n")
    print_grid(make_grid(markers), legend)

# ─────────────────────────────────────────────
# GERAK KARAKTER
# ─────────────────────────────────────────────

def walk_together(steps=1, direction="right",
                  extra_markers=None, legend="H=Hana  V=Vina", title="BERJALAN"):
    """Animasi dua karakter berjalan bersama."""
    dr = {"right": (0, 1), "left": (0, -1), "up": (-1, 0), "down": (1, 0)}[direction]
    for _ in range(steps):
        hana_pos[0] = max(0, min(SIZE-1, hana_pos[0] + dr[0]))
        hana_pos[1] = max(0, min(SIZE-1, hana_pos[1] + dr[1]))
        vina_pos[0] = max(0, min(SIZE-1, vina_pos[0] + dr[0]))
        vina_pos[1] = max(0, min(SIZE-1, vina_pos[1] + dr[1]))

        m = {tuple(hana_pos): "H", tuple(vina_pos): "V"}
        if extra_markers:
            m.update(extra_markers)
        show_scene(m, legend, title)
        time.sleep(0.7)

# ─────────────────────────────────────────────
# SCENE 1 – PERTEMUAN DI MALAM HARI
# ─────────────────────────────────────────────

def scene_pertemuan():
    hana_pos[:] = [3, 1]
    vina_pos[:] = [3, 2]

    show_scene({tuple(hana_pos): "H", tuple(vina_pos): "V"},
               title="MALAM — JALAN SEPI")

    delay("Keheningan malam membuat suasana menjadi canggung...")
    delay("Cahaya bulan masih menyinari, seperti memperhatikan mereka berdua...")
    delay("Menunggu apa yang akan terjadi...")
    wait()

    show_scene({tuple(hana_pos): "H", tuple(vina_pos): "V"})
    time.sleep(0.5)
    print('V : "Bagaimana?"')
    time.sleep(2)
    print('V : "Jadi.. larut malam begini, kamu mau kemana?"')
    time.sleep(2)
    print('H : *Masih terdiam*')
    time.sleep(2)
    print('V : "Kamu pendiam ya"')
    time.sleep(2)
    print('V : *memperhatikan sekitar*')
    time.sleep(2)
    print('H : *Melihat Vina dengan penasaran*')
    time.sleep(2)
    print('V : *Melihat Hana kembali*')
    time.sleep(2)
    print('V : "Baiklah.."')
    time.sleep(1.5)
    print('V : "Aku akan menemani mu"')
    time.sleep(2)
    print('H : *terdiam sejenak, lalu berjalan pergi — berharap Vina mengikuti*')

    wait()

# ─────────────────────────────────────────────
# SCENE 2 – MINIMARKET
# ─────────────────────────────────────────────

def scene_minimarket():
    hana_pos[:] = [3, 1]
    vina_pos[:] = [3, 2]

    delay("Mereka berjalan bersama tanpa Vina tahu akan dibawa kemana...")
    delay("Perjalanan dipenuhi rasa canggung, tanpa pembicaraan apapun...")
    wait()

    # animasi jalan ke kanan menuju minimarket
    walk_together(3, "right",
                  extra_markers={(npc_pos[0], npc_pos[1]): "N"},
                  legend="H=Hana  V=Vina  N=Kasir",
                  title="MENUJU MINIMARKET")

    show_scene({tuple(hana_pos): "H", tuple(vina_pos): "V",
                tuple(npc_pos):  "N"},
               legend="H=Hana  V=Vina  N=Kasir",
               title="MINIMARKET")

    delay("Hana pergi ke meja kasir...")
    delay("Menunjuk sebungkus rokok di rak...")
    time.sleep(1)
    print('N : *mengambilkan rokok yang diminta*')
    time.sleep(2)
    print('H : *membayar dengan uang koin, lalu keluar*')
    time.sleep(2)
    print('V : "Hana, kenapa kamu membeli rokok? Ini juga sudah malam"')
    time.sleep(2)
    print('H : *hanya terdiam sambil memegang erat sebungkus rokok*')
    time.sleep(2)
    print('V : "Apakah Hana disuruh seseorang?"')
    time.sleep(2)
    print('H : *Mengangguk pelan*')
    time.sleep(2)
    print('V : "Pasti yang menyuruh Hana orang jahat"')
    time.sleep(2)
    print('H : *Menggelengkan kepala*')
    time.sleep(2)
    print('V : *Heran dengan jawaban Hana*')
    time.sleep(2)
    print('V : "Lalu siapa?"')
    time.sleep(2)
    print('H : *Hanya terdiam*')
    time.sleep(2)
    print('V : *Mulai merasa kesal*')
    time.sleep(2)
    print('V : "Kamu itu bisa berbicara ga sih?"')
    time.sleep(2)
    print('H : *Hanya terdiam*')
    time.sleep(2)
    print('V : *Menghela napas menyerah*')
    time.sleep(2)
    print('V : "Baiklah.."')
    time.sleep(1.5)
    print('V : "Ayo kita pulang"')
    time.sleep(2)
    print('V : "Pasti orang tua kita khawatir"')

    wait()

# ─────────────────────────────────────────────
# SCENE 3 – VINA MENYADARI
# ─────────────────────────────────────────────

def scene_sadar():
    hana_pos[:] = [3, 4]
    vina_pos[:] = [3, 2]

    show_scene({tuple(hana_pos): "H", tuple(vina_pos): "V"},
               title="JALAN — MALAM")

    delay("Vina berjalan pergi...")
    delay("Hingga sadar Hana tidak mengikutinya...")

    # Vina berbalik
    time.sleep(1)
    show_scene({tuple(hana_pos): "H", tuple(vina_pos): "V"},
               title="JALAN — MALAM")

    delay("Seperti seorang anak yang tersesat di tengah kegelapan malam...")
    delay("Vina merasakan ada yang salah...")

    time.sleep(1)
    print('\nV : "Ayooo.."')
    time.sleep(2)
    delay("\nTeriakan Vina membuat Hana tersadar...")
    delay("Hana berlari menghampiri Vina...")

    # Hana berlari ke posisi Vina
    for _ in range(2):
        hana_pos[1] -= 1
        show_scene({tuple(hana_pos): "H", tuple(vina_pos): "V"}, title="BERLARI")
        time.sleep(0.5)

    wait()

# ─────────────────────────────────────────────
# SCENE 4 – PERCAKAPAN DI JALAN
# ─────────────────────────────────────────────

def scene_jalan_pulang():
    hana_pos[:] = [3, 2]
    vina_pos[:] = [3, 3]

    show_scene({tuple(hana_pos): "H", tuple(vina_pos): "V"},
               title="JALAN PULANG")

    delay("Jalan itu begitu tenang... atau terlalu tenang.")
    wait()

    walk_together(1, "left", title="JALAN PULANG")

    print('V : "Omong-omong.."')
    time.sleep(2)
    print('V : "Hana tinggal bersama siapa?"')
    time.sleep(2)
    print('H : *Terdiam*')
    time.sleep(2)
    print('V : *Melihatnya, dengan sedikit rasa kesal*')
    time.sleep(2)
    print('V : "Aku lupa kam-"')
    time.sleep(2)
    print('H : "Ibu"')
    time.sleep(2)
    print('V : "-mu.."')
    time.sleep(1.5)
    print('V : *Terdiam mendengar Hana tiba-tiba berbicara*')
    time.sleep(2)
    print('V : *Melihat Hana*')
    time.sleep(2)
    print('V : "Jadi.. kamu tinggal dengan ibu mu ya.."')
    time.sleep(2)
    print('H : *Mengangguk pelan*')
    time.sleep(2)
    print('V : *Kembali melihat ke depan*')

    delay("\nSesuatu perasaan muncul di lubuk hati Vina...")
    delay("Seperti puzzle mulai tersusun di benaknya...")
    wait()

    show_scene({tuple(hana_pos): "H", tuple(vina_pos): "V"}, title="JALAN PULANG")

    print('V : "Ayah Hana?"')
    time.sleep(2)
    print('H : *Hanya diam tak menjawab*')
    time.sleep(2)
    print('V : "Jadi Hana hanya tinggal bersama ibu Hana?"')
    time.sleep(2)
    print('H : *Masih terdiam*')
    time.sleep(2)
    print('V : "Memang nya-"')
    time.sleep(2)
    print('V : *Melihat Hana kembali..*')
    time.sleep(2)
    print('H : *Air mata menetes dari dagu*')
    time.sleep(1)

    delay("\nTanpa suara, tanpa aba-aba...")
    delay("Tiba-tiba Hana menangis dalam diam...")
    delay("Muka Hana yang datar dan tangisan dalam diam itu...")
    delay("Entah mengapa menyakitkan untuk dilihat...")

    wait()

# ─────────────────────────────────────────────
# SCENE 5 – PERPISAHAN
# ─────────────────────────────────────────────

def scene_perpisahan():
    hana_pos[:] = [3, 2]
    vina_pos[:] = [3, 3]

    delay("Mereka masih terus berjalan menelusuri jalan yang gelap...")
    delay("Rasa dingin menusuk kulit mereka...")
    delay("Rasa canggung tak kunjung menghilang...")
    wait()

    # kembali ke posisi awal (tempat pertama bertemu)
    hana_pos[:] = [3, 1]
    vina_pos[:] = [3, 2]

    show_scene({tuple(hana_pos): "H", tuple(vina_pos): "V"},
               title="TEMPAT PERTAMA KALI BERTEMU")

    delay("Mereka kembali di tempat pertama kali bertemu...")
    delay("Menunggu siapapun berbicara untuk perpisahan malam ini...")
    time.sleep(1)

    print('V : *Melihat sekitar dengan tidak nyaman*')
    time.sleep(2)
    delay("\nRasa bersalah Vina menanyakan beberapa pertanyaan pribadi...")
    delay("Ia bingung ingin mengatakan apa...")
    time.sleep(1)

    print('\nH : *Melihat Vina dengan khawatir*')
    time.sleep(2)
    print('V : *Melihat Hana*')
    time.sleep(2)
    print('V : *Memperhatikan raut kekhawatiran Hana*')
    time.sleep(1)

    delay("\nMomen itu membuat dunia terasa berhenti di pandangan Vina...")
    delay("Campuran rasa yang belum pernah ia rasakan muncul...")
    wait()

    show_scene({tuple(hana_pos): "H", tuple(vina_pos): "V"},
               title="PERPISAHAN")

    print('V : "Jika Hana butuh aku.."')
    time.sleep(2)
    print('V : "Rumah ku ga jauh dari sini"')
    time.sleep(2)
    print('V : *Menunjuk jalan ke arah rumahnya*')
    time.sleep(2)
    print('V : "Di situ rumah ku"')
    time.sleep(2)
    print('H : *Hanya terdiam ketika menjelaskan*')
    time.sleep(2)
    print('V : "Jika butuh aku, datang saja ya.."')
    time.sleep(1)

    delay("\nVina berlari pergi dengan tergesa-gesa...")
    delay("Hana hanya bisa terdiam bingung...")
    delay("Vina menghilang tanpa sempat bereaksi...")
    time.sleep(1)

    # Vina pergi (bergerak menjauh)
    for _ in range(3):
        vina_pos[1] += 1
        vina_pos[1] = min(SIZE-1, vina_pos[1])
        show_scene({tuple(hana_pos): "H", tuple(vina_pos): "V"}, title="VINA PERGI")
        time.sleep(0.6)

    print('\nH : *Terdiam melihat jalan yang dilalui Vina*')
    time.sleep(2)
    print('H : *Berjalan pergi menuju rumahnya*')

    wait()

# ─────────────────────────────────────────────
# SCENE 6 – DEPAN PINTU RUMAH
# ─────────────────────────────────────────────

def scene_rumah():
    hana_pos[:] = [3, 2]
    aku_pos_local = [3, 4]

    show_scene({tuple(hana_pos): "H"},
               legend="H=Hana",
               title="DEPAN RUMAH HANA")

    delay("Malam itu terasa aneh bagi Hana...")
    delay("Momen pertama kali di hidupnya...")
    delay("Dan pertama kalinya bertemu Vina...")
    delay("Sedikit rasa nyaman muncul di hati kecil Hana...")
    wait()

    show_scene({tuple(hana_pos): "H"},
               legend="H=Hana",
               title="DEPAN PINTU RUMAH")

    delay("Sebelum perasaan itu kembali...")
    delay("Ketika ia sudah sampai di depan pintu rumah...")
    delay("Sebelum sempat membuka pintu...")
    delay("Sudah terdengar suara ricuh dari dalam...")
    time.sleep(1)

    # pintu dibuka — I muncul
    show_scene({tuple(hana_pos): "H",
                tuple(aku_pos_local): "I"},
               legend="H=Hana  I=Seseorang",
               title="PINTU TERBUKA")

    delay("Hana membuka pintu...")
    delay("Ia melihat seseorang yang sedang menghancurkan semua yang ada di depannya...")
    time.sleep(1)

    print('\nI : *memandang Hana*')
    time.sleep(2)

    delay("\n...")
    time.sleep(0.8)
    delay("...")
    time.sleep(0.8)

    wait()

# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    clear()
    print("=" * 40)
    delay("  ✦  MALAM YANG TERLALU TENANG  ✦")
    print("=" * 40)
    delay("\n  Sebuah cerita tentang dua orang asing")
    delay("  yang bertemu di keheningan malam...\n")
    wait()

    scene_pertemuan()
    scene_minimarket()
    scene_sadar()
    scene_jalan_pulang()
    scene_perpisahan()
    scene_rumah()

    clear()
    print("=" * 40)
    delay("       — to be continued —")
    print("=" * 40)
    print()

if __name__ == "__main__":
    main()
