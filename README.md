📌 Description
Cozy Parking Pro is a Python console application that simulates a parking lot system. It allows users to park vehicles, remove them, track earnings, and view parking activity. The program stores data using JSON and maintains a log for all parking actions.

✨ Features

🚗 Park vehicles with different vehicle types
📊 View parking statistics and earnings
🅿️ Visual parking lot diagram in the terminal
💰 Automatic hourly parking fee calculation
📅 Daily parking charge limit
📝 Activity logging system
💾 Persistent data storage using JSON
🧹 Clear all parking spots when needed

🖥️ Preview

Example parking layout:

           ENTRY
            ↓
╔════════════════════════════════════════════════╗
║ [🚗] [🚙] [   ] [🚚] [   ] ║
║────────────────────────────────────────────────║
║ [   ] [🏎] [   ] [🚐] [   ] ║
╚════════════════════════════════════════════════╝
            ↑
           EXIT
📂 Project Structure
Cozy-Parking-Pro/
│
├── cozy_parking_pro.py
├── parking_data.json
├── parking_log.txt
└── README.md
⚙️ Requirements

Python 3.x

Works in any terminal (Windows / macOS / Linux)

No external libraries are required.

▶️ How to Run

Clone or download the repository

git clone https://github.com/yourusername/cozy-parking-pro.git

Open the project folder

cd cozy-parking-pro

Run the program

python cozy_parking_pro.py
📊 Program Options
1. Park Vehicle
2. Remove Vehicle
3. View Statistics
4. Clear All Parking
5. View Log
6. Exit
🧠 How It Works

On the first run, the program asks for the total number of parking spots.

Vehicles are stored in a JSON file so the parking lot persists between runs.

Every parking or removal action is recorded in a log file with timestamps.

📁 Files Generated
File	Purpose
parking_data.json	Stores parking spots, earnings, and car data
parking_log.txt	Records parking and removal history
