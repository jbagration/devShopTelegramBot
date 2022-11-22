@echo off

call %~dp0DEV_bot\venv\Scripts\activate

cd %~dp0DEV_bot

set TOKEN=5748276803:AAGTmRo2djQmKm_Rt0WB0JFvrZOHNT_eZJk

python startDev.py

pause