@ECHO OFF
echo Installing Requirements
pip install -r requirements.txt
echo Starting ADB server
echo Make sure you headset is plugged in
pause
adb start-server
@ECHO ON
python main.py
