import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_scene():
    input("\n(ENTER untuk lanjut ke scene berikutnya...)")

def print_grid(grid):
    for row in grid:
        print(" ".join(row))

def empty_grid():
    return [["." for _ in range(7)] for _ in range(7)]

def auto_text(lines, delay=1.5):
    for line in lines:
        print(line)
        time.sleep(delay)

clear()
grid = empty_grid()
grid[3][3] = "P"

print_grid(grid)

auto_text([
    "Lampu sorot menerangi sebuah kursi...",
    "Seorang anak terduduk diam...",
    "Melihat sekitar dengan bingung...",
    "Mengapa dia disini..."
])

wait_scene()

clear()
print_grid(grid)

auto_text([
    'B1: "Anak seperti mu seharusnya mati saja"',
    'B2: "Tak akan ada yang peduli"',
    'B3: "Lagi pula sampah seperti mu.."'
], 2)

wait_scene()

clear()

auto_text([
    '"Tidak pantas ada disini"'
], 2.5)

wait_scene()

shadow_positions = [
    (2,3),(4,3),(3,2),(3,4),
    (2,2),(2,4),(4,2),(4,4)
]

for i in range(len(shadow_positions)):
    clear()
    grid = empty_grid()
    grid[3][3] = "P"

    for j in range(i+1):
        y,x = shadow_positions[j]
        grid[y][x] = "B"

    print("Bayangan mulai bermunculan...\n")
    print_grid(grid)
    time.sleep(0.6)

auto_text([
    "Bisikan terus menghantui...",
    "Menutup kuping dengan ketakutan...",
    "Berharap semua cepat selesai..."
])

wait_scene()

light_path = [(0,3),(1,3),(2,3),(3,3)]

for pos in light_path:
    clear()
    grid = empty_grid()
    grid[3][3] = "P"

    for y,x in shadow_positions:
        grid[y][x] = "B"

    y,x = pos
    grid[y][x] = "+"

    print("Sedikit cahaya muncul...\n")
    print_grid(grid)
    time.sleep(0.7)

auto_text([
    "Cahaya perlahan mendekat...",
    "Seperti menarik keluar dari kegelapan..."
])

wait_scene()

clear()
grid = empty_grid()
grid[3][3] = "P"

print_grid(grid)

auto_text([
    "Lampu menerangi ruangan...",
    "Dia terbaring disebuah ruangan...",
    "Tampak tidak asing...",
    "Ini masih disekolah..."
])

wait_scene()

npc_path = [(0,3),(1,3),(2,3),(3,3)]

for pos in npc_path:
    clear()
    grid = empty_grid()
    grid[3][3] = "P"

    y,x = pos
    grid[y][x] = "N"

    print_grid(grid)
    time.sleep(0.7)

auto_text([
    'N: "kamu sudah bangun ya.."',
    'N: "..."',
    'N: "jika sudah membaik, boleh ikut ibu?"'
], 2)

wait_scene()

print("\n=== TO BE CONTINUE ===")
