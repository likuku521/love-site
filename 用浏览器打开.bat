@echo off
rem Open confession site in Chrome/Edge (bypass WPS html hijack)
set "FILE=%~dp0index.html"
for %%B in (
  "C:\Program Files\Google\Chrome\Application\chrome.exe"
  "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
  "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
  "C:\Program Files\Microsoft\Edge\Application\msedge.exe"
) do (
  if exist %%B (
    start "" "%%~B" "%FILE%"
    exit /b
  )
)
start "" "%FILE%"
