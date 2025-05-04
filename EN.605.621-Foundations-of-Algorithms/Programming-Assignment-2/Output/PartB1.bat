@echo off

:: Activate Virtual Environment
Call .venv\Scripts\activate.bat

:: Run Main.py
Call python Python\Main.py "Part B1" "1011" "1001" "PartB1Output.txt"

:: Deactivate Virtual Environment
Call .venv\Scripts\deactivate.bat
    
pause