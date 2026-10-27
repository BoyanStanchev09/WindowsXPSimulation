@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Could not find the project's .venv virtual environment.
    echo Create it and install requirements.txt before running this launcher.
    pause
    exit /b 1
)

start "Windows XP Simulation Server" cmd /k ".venv\Scripts\python.exe manage.py runserver"
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:8000/"
endlocal
