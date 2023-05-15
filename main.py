import requests
from ppadb.client import Client as AdbClient
import os
import json
import urllib.request
import zipfile
from colorama import Fore, Style

package = "com.TrassGames.GodsOfGravity"
version = "1.0.0"
# just makes my life easier

os.system("cls")

headers = {
  'Accept': 'application/json',
  'X-Modio-Platform': 'Oculus'
}

print("Hello! Thanks for using Gods of Modding. To get started, you'll need to put your API key in. We'll only use this to download the needed files from mod.io. Don't trust us? Look at the code for yourself.\n\nDon't have one?\nTo make one, follow these steps.\n1. Navigate to https://mod.io/me/access in a web browser\n2. Make sure you're logged in to mod.io.\n3. Make an API key, and paste it in here.\n4. DO NOT SHARE THIS API KEY!")
apikey = input("API Key: ")

os.system("cls")
print(f"{Style.BRIGHT}Gods of Modding {Style.RESET_ALL}| {version}\n\nLoading... (connecting to adb)")

try:
  client = AdbClient(host="127.0.0.1", port=5037)
except:
  print(f"\n{Style.BRIGHT}{Fore.RED}Couldn't connect to adb. Make sure to start the adb server.")
  exit()
devices = client.devices()
print("Loading... (checking devices)")
counter = 0

for device in devices:
  counter += 1
  installed = device.is_installed(package)

if(counter==0):
  print(f"\n{Style.BRIGHT}{Fore.RED}Couldn't find any connected devices. Make sure your headset is plugged in.{Style.RESET_ALL}")
  exit()
elif(counter>=2):
  print(f"\n{Style.BRIGHT}{Fore.RED}Multiple devices appear to be connected. Please only connect your headset.{Style.RESET_ALL}")
  exit()
elif(counter==1):
  os.system("cls")
  print(f"{Style.BRIGHT}Gods of Modding {Style.RESET_ALL}| {version}\n\nGoG installed? {Fore.CYAN}{installed}{Style.RESET_ALL}\n\nTip: Always make sure you're using the latest version of Gods of Modding!")
  if(installed==True):
    print(f"{Style.BRIGHT}\nSelect an option:\n{Style.RESET_ALL}[1] Install modded Gods of Gravity\n[2] Uninstall Gods of Gravity\n[0] Exit")
  elif(installed==False):
    print(f"{Style.BRIGHT}\nSelect an option:\n{Style.RESET_ALL}[1] Install modded Gods of Gravity\n[0] Exit")
  else:
    print(f"\n{Style.BRIGHT}{Fore.RED}ERROR! Please make an issue on the GitHub.\nError details: The game is not installed but not uninstalled.\nError code: Blobfish")
    exit()
  try:
    v = input("> ")
  except:
    print(f"\n{Style.BRIGHT}{Fore.RED}ERROR! Bad input.")
    exit()
  if(v=="0"):
    exit()
  elif(v=="1"):
    if(installed==True):
      print("Uninstalling Gods of Gravity...")
      for device in devices:
        try:
          device.uninstall(package)
        except:
          print(f"{Style.BRIGHT}{Fore.RED}ERROR! Uninstall failed.")
          exit()
      for device in devices:
        insta2 = device.is_installed(package)
      if(insta2==True):
        print(f"{Style.BRIGHT}{Fore.RED}ERROR! Uninstall failed.")
        exit()
      elif(insta2==False):
        print("Uninstalled Gods of Gravity!")
    r = requests.get('https://api.mod.io/v1/games/5003/mods/2989636/files/3798676', params={'api_key': apikey}, headers = headers)
    ri = r.json()
    try:
      rib = ri["download"]
    except:
      print(f"{Style.BRIGHT}{Fore.RED}ERROR! The needed file could not be installed. You probably put in an invalid API key.")
      exit()
    ribs = rib["binary_url"]
    print("Downloading file...")
    try:
      urllib.request.urlretrieve(ribs, "build.zip")
    except:
      print(f"{Style.BRIGHT}{Fore.RED}Failed to download file.")
      exit()
    with zipfile.ZipFile("build.zip", 'r') as zip_ref:
      zip_ref.extractall("moddedapk")
    for device in devices:
      try:
        os.chdir("moddedapk")
        device.install("build.apk")
      except:
        print(f"\n{Style.BRIGHT}{Fore.RED}An error occured during install. Try:\n- Making sure your headset is in developer mode (enabled in mobile app)\n- Making sure your headset is properly connected\n- Rerunning this script")
        exit()
      print(f"{Style.BRIGHT}{Fore.GREEN}Modded Gods of Gravity installed!{Style.RESET_ALL} Now:\n- Open the game on your headset\n- You will see the Trass Games logo then nothing\n- DO NOT TURN OFF YOUR HEADSET OR EXIT THE APP! Wait for the game to load\n- This will take a few minutes\n- Once you load in, your game should be modded!")
      exit()
    else:
      print(f"\n{Style.BRIGHT}{Fore.RED}ERROR! Please make an issue on the GitHub.\nError details: The game is not installed but not uninstalled.\nError code: Second Blobfish")
      exit()
  elif(v=="2"):
    if(installed==True):
      print("Uninstalling Gods of Gravity...")
      for device in devices:
        try:
          device.uninstall(package)
        except:
          print(f"{Style.BRIGHT}{Fore.RED}ERROR! Uninstall failed.")
          exit()
      for device in devices:
        insta2 = device.is_installed(package)
      if(insta2==True):
        print(f"{Style.BRIGHT}{Fore.RED}ERROR! Uninstall failed.")
        exit()
      elif(insta2==False):
        print("Uninstalled Gods of Gravity!")
        exit()
      else:
        print(f"{Style.BRIGHT}{Fore.RED}\nERROR! Please make an issue on the GitHub.\nError details: The game is not installed but not uninstalled.\nError code: Third Blobfish")
        exit()
  else:
    print(f"\n{Style.BRIGHT}{Fore.RED}ERROR! Bad input.")
else:
  print(f"{Style.BRIGHT}{Fore.RED}\nERROR! Please make an issue on the GitHub.\nError details: The counter is not zero, is not one, and is not equal to or above two.\nError code: Jellyfish")
  exit()
