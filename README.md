# Auto-Stop-Windows
TL;DR : Shutdown Scheduler for Windows

This project is a simple desktop application for scheduling the automatic shutdown of your computer. The user interface allows the user to set a specific time in hours and minutes after which the computer will shut down.

## Features

- Schedule the time for your computer to shut down automatically.
- Cancel the scheduled shutdown at any time.
- Simple and easy-to-use user interface.

## Installation

To use this application, first clone the repository and install the necessary dependencies.

```bash
git clone https://github.com/Yamatotori/Auto-Stop-Windows.git
cd Auto-Stop-Windows
```

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

## Execution

To run the application, launch the main script:

```bash
python main.py
```

## Creating an Executable

To create an executable file for this application, use PyInstaller:

```bash
pyinstaller --onefile --windowed --icon=logo.png --name="Auto Stop Windows" --clean main.py
```

### Note on Antivirus

When creating the executable file with PyInstaller, some antivirus software may falsely detect the .exe file as malicious. If this happens, you may temporarily disable your antivirus or add an exception for this file. Ensure to perform this action only if you are confident in the legitimacy and safety of your script.

## License
Include information about the license under which your project is distributed.