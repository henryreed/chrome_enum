# Chrome Enum
"Anyone who stores a password in their browser deserves what they get." --A dear friend of mine.

Decrypts and dumps Google Chrome cookies and passwords in Microsoft Windows.
## Features
* Does not require administrator privileges
* Does not require Windows password
* Supports both crypto methods used before and after Chrome V80
* Program will not fail as a result of a database lock by Chrome; i.e., you may launch this program while Chrome is running
* Data is in a list of lists, allowing for easy integration with other software as a library
## Installation
You may use the chrome_enum.exe file in the dist directory, no installation required. The software was tested in Python 3.9.0, but compiled into the .exe with Python 3.7.9 to comply with Pyinstaller's version requirement. 
```
.\dist\chrome_enum.exe
```
If you wish, you may run the script directly. It is recommended to use a virtual environment:
```
python -m venv venv
.\venv\Scripts\pip.exe install -r requirements.txt
.\venv\Scripts\python.exe chrome_enum.py
```
Installation without a virtual environment:
```
pip install -r requirements.txt
python chrome_enum.py
```
### Planned features
* Support for Mac OS
* Support for Linux