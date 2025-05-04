@echo off

:: Activate Virtual Environment
Call .venv\Scripts\activate.bat

:: Run Main.py
Call python Python\Main.py "Part B3" "1011" "10" "PartB3Output.txt"

:: Deactivate Virtual Environment
Call .venv\Scripts\deactivate.bat
    
pause