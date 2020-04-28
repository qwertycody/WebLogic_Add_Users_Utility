@echo on

SET "JDEVELOPER_SYSTEM_ENV=C:\Users\Username\AppData\Roaming\JDeveloper\system12.2.1.3.42.170820.0914"

SET "WEBLOGIC_BIN=%JDEVELOPER_SYSTEM_ENV%\DefaultDomain\bin"
SET "WEBLOGIC_SET_DOMAIN_ENV=%WEBLOGIC_BIN%\setDomainEnv.cmd"

SET "SCRIPT_DIRECTORY=%~dp0"
SET "SCRIPT_DIRECTORY=%SCRIPT_DIRECTORY:~0,-1%"

call %WEBLOGIC_SET_DOMAIN_ENV%

cd /D "%SCRIPT_DIRECTORY%"

java weblogic.WLST WLS_UserCreation.py -username weblogic -password password1

pause