@echo off

:: Activate Virtual Environment
Call .venv\Scripts\activate.bat

:: Run Main.py
Call python Python\Main.py "S1" "100010101" "101" "0"

:: Run Main.py
Call python Python\Main.py "S2" "101010101010101" "101" "010"

:: Run Main.py
Call python Python\Main.py "S3" "001100110101011001100110010101111" "101" "010"

:: Run Main.py
Call python Python\Main.py "S4" "100110011001" "101" "010"

:: Deactivate Virtual Environment
Call .venv\Scripts\deactivate.bat
    
pause