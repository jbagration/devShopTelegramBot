@echo off

call %~dp0DEV_bot\venv\Scripts\activate # путь

cd %~dp0DEV_bot

set TOKEN= # токен

python startDev.py

pause
