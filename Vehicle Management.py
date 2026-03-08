import os
import time
import json
from datetime import datetime

# --------- Soft Pastel Eye-Friendly Colors ---------
RESET = "\033[0m"
SOFT_BLUE = "\033[38;5;110m"
SOFT_GREEN = "\033[38;5;114m"
SOFT_CYAN = "\033[38;5;117m"
SOFT_PINK = "\033[38;5;175m"
SOFT_YELLOW = "\033[38;5;180m"
SOFT_RED = "\033[38;5;203m"

HOURLY_RATE = 5
MAX_DAILY = 50
DATA_FILE = "parking_data.json"
LOG_FILE = "parking_log.txt"

# --------- Safe File Creation ---------
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("Cozy Parking Pro Log\n")
        f.write("=====================\n")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input(SOFT_CYAN + "\nPress Enter to continue..." + RESET)

def header():
    print(SOFT_PINK + "═" * 80)
    print("               🌿 COZY PARKING PRO 🌿")
    print("═" * 80 + RESET)

def save_log(text):
    with open(LOG_FILE, "a") as f:
        f.write(text + "\n")

# --------- Load & Save Data ---------
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

data_store = load_data()

if "spots" not in data_store:
    while True:
        try:
            TOTAL_SPOTS = int(input("Enter number of parking spots ➜ "))
            if TOTAL_SPOTS <= 0:
                raise ValueError
            break
        except:
            print("Enter valid number.")

    data_store = {
        "total_spots": TOTAL_SPOTS,
        "spots": [None] * TOTAL_SPOTS,
        "earnings": 0,
        "total_cars": 0
    }
    save_data(data_store)

TOTAL_SPOTS = data_store["total_spots"]

# --------- Realistic Parking Diagram ---------
def show_parking():
    spots = data_store["spots"]
    half = TOTAL_SPOTS // 2

    print(SOFT_BLUE + "\n           ENTRY")
    print("            ↓")
    print("╔════════════════════════════════════════════════╗")

    # Top Row
    print("║ ", end="")
    for i in range(half):
        s = spots[i]
        if s:
            print(f"[{s['emoji']}]", end=" ")
        else:
            print("[   ]", end=" ")
    print("║")

    # Road Divider
    print("║────────────────────────────────────────────────║")

    # Bottom Row
    print("║ ", end="")
    for i in range(half, TOTAL_SPOTS):
        s = spots[i]
        if s:
            print(f"[{s['emoji']}]", end=" ")
        else:
            print("[   ]", end=" ")
    print("║")

    print("╚════════════════════════════════════════════════╝")
    print("            ↑")
    print("           EXIT\n" + RESET)

# --------- Car Menu ---------
def choose_car():
    cars = {
        "1": ("Sedan", "🚗"),
        "2": ("SUV", "🚙"),
        "3": ("Truck", "🚚"),
        "4": ("Sports", "🏎"),
        "5": ("Motorcycle", "🏍"),
        "6": ("Electric", "🔋"),
        "7": ("Van", "🚐"),
        "8": ("Taxi", "🚕"),
        "9": ("Police", "🚓"),
    }

    print(SOFT_CYAN + "\nChoose Vehicle Type\n" + RESET)
    for k, v in cars.items():
        print(f"{k}. {v[0]} {v[1]}")

    return cars.get(input("Select ➜ "))

# --------- Park Vehicle ---------
def park():
    name = input("Vehicle name ➜ ").strip()
    if not name:
        print("Invalid name."); time.sleep(1); return

    car = choose_car()
    if not car:
        print("Invalid type."); time.sleep(1); return

    try:
        spot = int(input(f"Choose spot (1-{TOTAL_SPOTS}) ➜ "))
        if not 1 <= spot <= TOTAL_SPOTS:
            raise ValueError
    except:
        print("Invalid spot."); time.sleep(1); return

    if data_store["spots"][spot-1]:
        print("Spot occupied."); time.sleep(1); return

    try:
        hours = int(input("Hours ➜ "))
        if hours <= 0:
            raise ValueError
    except:
        print("Invalid hours."); time.sleep(1); return

    cost = min(hours * HOURLY_RATE, MAX_DAILY)

    vehicle = {
        "name": name,
        "type": car[0],
        "emoji": car[1],
        "hours": hours,
        "cost": cost
    }

    data_store["spots"][spot-1] = vehicle
    data_store["earnings"] += cost
    data_store["total_cars"] += 1

    save_data(data_store)

    save_log(f"{datetime.now()} | PARKED | {name} | Spot {spot} | ${cost}")

    print(SOFT_GREEN + f"\nParked successfully! Charged ${cost}" + RESET)
    pause()

# --------- Remove Vehicle ---------
def remove():
    try:
        spot = int(input("Enter spot to remove ➜ "))
        if not 1 <= spot <= TOTAL_SPOTS:
            raise ValueError
    except:
        print("Invalid spot."); time.sleep(1); return

    vehicle = data_store["spots"][spot-1]
    if not vehicle:
        print("Spot empty."); time.sleep(1); return

    data_store["spots"][spot-1] = None
    save_data(data_store)

    save_log(f"{datetime.now()} | REMOVED | {vehicle['name']} | Spot {spot}")

    print(SOFT_YELLOW + "\nVehicle removed successfully." + RESET)
    pause()

# --------- Clear All (New Option 1) ---------
def clear_all():
    confirm = input("Are you sure? (yes/no) ➜ ").lower()
    if confirm == "yes":
        data_store["spots"] = [None] * TOTAL_SPOTS
        save_data(data_store)
        print("All spots cleared.")
    pause()

# --------- View Log (New Option 2) ---------
def view_log():
    clear()
    header()
    print(SOFT_CYAN + "\nParking Activity Log\n" + RESET)
    with open(LOG_FILE, "r") as f:
        print(f.read())
    pause()

# --------- Stats ---------
def stats():
    print(SOFT_CYAN + "\nStatistics\n" + RESET)
    print(f"Total Cars Ever Parked ➜ {data_store['total_cars']}")
    print(f"Total Earnings ➜ ${data_store['earnings']}")
    print(f"Available Spots ➜ {data_store['spots'].count(None)}")
    pause()

# --------- Main Loop ---------
while True:
    clear()
    header()
    show_parking()

    print("1. Park Vehicle 🚗")
    print("2. Remove Vehicle 🚘")
    print("3. View Statistics 📊")
    print("4. Clear All Parking 🧹")
    print("5. View Log 📝")
    print("6. Exit ❌\n")

    choice = input("Select ➜ ")

    if choice == "1": park()
    elif choice == "2": remove()
    elif choice == "3": stats()
    elif choice == "4": clear_all()
    elif choice == "5": view_log()
    elif choice == "6":
        print(SOFT_GREEN + "\nSystem safely closed. Drive carefully 🌿🚗\n" + RESET)
        break
    else:
        print("Invalid choice."); time.sleep(1)