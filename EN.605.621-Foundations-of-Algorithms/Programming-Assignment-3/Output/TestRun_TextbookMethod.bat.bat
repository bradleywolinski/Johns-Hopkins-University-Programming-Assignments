@echo off

:: Activate Virtual Environment
Call .venv\Scripts\activate.bat

:: Run Main.py
Call python Python\Main.py "Test Runs" "Textbook Method"

:: Deactivate Virtual Environment
Call .venv\Scripts\deactivate.bat
    
pause