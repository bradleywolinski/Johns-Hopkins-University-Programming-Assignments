@echo off

:: Create Virtual Environment
echo "Creating Virtual Environment..."
py -3 -m venv ..\.venv

:: Activate Virtual Environment
echo "Activating Virtual Environment..."
Call ..\.venv\Scripts\activate.bat

:: Install Dependencies
echo "Installing Dependencies..."
python -m pip install -r requirements.txt

:: Deactivate Virtual Environment
echo "Deactivating Virtual Environment..."
Call ..\.venv\Scripts\deactivate.bat

pause