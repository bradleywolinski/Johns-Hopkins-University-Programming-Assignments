@echo off

:: Activate Virtual Environment
Call .venv\Scripts\activate.bat

:: Run Main.py
Call python Python\Main.py "Part A" "1001" "" "PartAOutput.txt"

:: Deactivate Virtual Environment
Call .venv\Scripts\deactivate.bat
    
pause