@ECHO OFF
echo Installing Requirements
pip install -r requirements.txt
echo Starting ADB server
adb start-server
@ECHO ON
python main.py
