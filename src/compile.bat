cd "C:\Users\Ashwin\Desktop\Programming Portfolio\Finished Projects\py-to-exe\src"
python -m pip install --upgrade pip
pip install pyinstaller
pyinstaller --onefile --noconsole --icon="C:\\Users\\Ashwin\\Desktop\\Programming Portfolio\\Finished Projects\\py-to-exe\\icon\\favicon.ico" -w "main.py"