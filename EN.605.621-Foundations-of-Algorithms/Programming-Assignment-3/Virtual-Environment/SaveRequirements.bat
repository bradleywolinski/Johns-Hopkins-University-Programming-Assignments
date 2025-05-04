@echo off

:: Activate Virtual Environment
echo "Activating Virtual Environment..."
Call ..\.venv\Scripts\activate.bat

:: Create Requirements
echo "Creating Requirements Text File..."
python -m pip freeze > requirements.txt

:: Deactivate Virtual Environment
echo "Deactivating Virtual Environment..."
Call ..\.venv\Scripts\deactivate.bat

pause