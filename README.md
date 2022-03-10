# Chrome Enum
"Anyone who stores a password in their browser deserves what they get." --A dear friend of mine.

Decrypts and dumps Chrome-based browser cookies and passwords in Microsoft Windows.

## Features
* Does not require administrator privileges
* Does not require Windows password
* Supports both crypto methods used before and after Chrome V80
* Program will not fail as a result of a database lock by Chrome; i.e., you may launch this program while Chrome is running
* Data is in a list of lists, allowing for easy integration with other software as a library

## Supported Browsers
* Opera
* Brave Browser
* Chrome-based version of Microsoft Edge
* Google Chrome

## Installation
You may use the chrome_enum.exe file in the dist directory, no installation required. The software was tested and bundled in Python 3.10.2. PyInstaller version 4.10 was used to bundle the script into an executable binary.
```
.\dist\chrome_enum.exe
```
If you wish, you may run the script directly. It is recommended to use a virtual environment:
```
PS > python -m venv venv
PS > .\venv\Scripts\Activate.ps1
(venv) PS > pip install -r requirements.txt
(venv) PS > python chrome_enum.py
```
Installation without a virtual environment (NOT recommended):
```
PS > pip install -r requirements.txt
PS > python chrome_enum.py
```
### Planned features
* Windows support for other Chrome-based browsers
* Support for Linux
* Support for macOS