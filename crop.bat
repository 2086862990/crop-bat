@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
set /p folder_path=Path:

for /r %folder_path% %%i in (*.png) do (
	set file_name=%%~ni
	if "!file_name:~0,1!" == "C" (
		start python crop.py %folder_path% %%i !file_name!
	)
)
pause