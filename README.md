# OPTAGEN Fish Project

Desktop application for managing fish cultivation tanks. It is a PyQt5-based
GUI (with a Bengali interface) backed by SQLite, with optional hardware/serial
modules for automated water preparation and culture monitoring.

## Features

- Register and unregister cultivation tanks (tank number + volume).
- Track tank availability, pre-culture and active cultivation stages.
- Water preparation reports (pH, TDS) per tank.
- Active culture monitoring with culture duration and water quality reports.
- Fish collection / culture termination workflow.
- Persistent storage in SQLite databases under `operational data/`.
- Optional background executables for pre-culture and culture automation
  (`backend/pre_culture_executive.py`, `backend/culture_monitoring_executive.py`)
  that talk to tank/lab modules over serial.

## Project layout

```
.
├── main.py                          # Application entry point
├── sample.py                        # Main window UI (generated from Qt Designer)
├── ui_reg.py                        # Tank registration dialog UI
├── ui_delregwidget.py               # Tank unregistration dialog UI
├── basic_functions.py               # Small DB helper utilities
├── Controller.py                    # Controller helpers
├── backend/
│   ├── database_module.py           # SQLite data manager (database_manager)
│   ├── sercom_module.py             # Serial communication with tank/lab modules
│   ├── gui_bakground.py             # GUI background helpers
│   ├── pre_culture_executive.py     # Background pre-culture automation
│   ├── culture_monitoring_executive.py
│   ├── database_tester.py
│   ├── test.py
│   ├── lab_code.ino                 # Arduino firmware for lab module
│   └── tank_code.ino                # Arduino firmware for tank module
├── operational data/                # SQLite DBs (tank.db, reports.db)
├── main_sample.ui                   # Qt Designer source for the main window
└── Changes/CodeChanges.txt
```

## Requirements

- Python **3.10** (the project targets PyQt5; Python 3.10 is the version
  that ships PyQt5 on this system).
- PyQt5
- pyserial (only needed for the hardware/serial backend modules)
- SQLite (bundled with Python via `sqlite3`)

Install the Python dependencies:

```bash
# PyQt5 (system package on Debian/Ubuntu)
sudo apt install python3-pyqt5

# Serial support for the hardware modules (optional)
pip install pyserial
```

> Note: the GUI itself only needs PyQt5. The serial modules are only required
> when running the background automation executables against real hardware.

## How to run

Always run from the project root, because database paths are relative to it.

```bash
cd /home/fahad/Documents/PROJECTS/SmartGeoRef/OPTAGEN_Fish_Project
python3.10 main.py
```

The entry point is also executable:

```bash
./main.py
```

On startup the app creates/opens `operational data/tank.db` and
`operational data/reports.db` (created automatically by `database_manager`).

### Running the background automation (optional, hardware required)

```bash
cd backend
python3.10 pre_culture_executive.py
python3.10 culture_monitoring_executive.py
```

These scripts expect the serial devices `/dev/ttyS0` and `/dev/ttyUSB0` to be
available and the Arduino firmware in `backend/*_code.ino` to be flashed.

## Confirming it is executable

`main.py` has a shebang (`#!/usr/bin/python3.10`) and the executable bit set.

```bash
ls -l main.py        # should show -rwxr-xr-x
file main.py         # should report a Python script
./main.py            # launches the GUI (exit code 124 on timeout is expected)
```

A quick smoke test that only imports the UI modules without opening a window:

```bash
cd /home/fahad/Documents/PROJECTS/SmartGeoRef/OPTAGEN_Fish_Project
python3.10 -c "import sample, ui_reg, ui_delregwidget, basic_functions; print('imports OK')"
```

## Notes

- The UI text is in Bengali; the `Baloo Da 2` font is recommended for correct
  rendering but the application runs without it.
- Default password used in the dialogs is `1234`.
- Working directory matters: run commands from the project root.