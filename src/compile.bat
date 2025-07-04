cd "C:\Users\ashwi\Desktop\py-to-exe\src"
python -m pip install --upgrade pip
py -m pip install pyinstaller
py -m PyInstaller --onefile --noconsole -w "main.py"