@echo off
setlocal

rem Set the paths for reports
set ALLURE_RESULTS=D:\PyProjects\shopvi\reports\allurereports
set HTML_REPORTS=D:\PyProjects\shopvi\reports\htmlreports
set ALLURE_HTML_REPORT=D:\PyProjects\shopvi\reports\allure_report
set ZIP_FILE=D:\PyProjects\shopvi\reports\allure_report.zip

rem Clean up old report directories
if exist %ALLURE_RESULTS% (
    rmdir /s /q %ALLURE_RESULTS%
)
if exist %HTML_REPORTS% (
    rmdir /s /q %HTML_REPORTS%
)
if exist %ALLURE_HTML_REPORT% (
    rmdir /s /q %ALLURE_HTML_REPORT%
)

rem Create new report directories
mkdir %ALLURE_RESULTS%
mkdir %HTML_REPORTS%

rem Run pytest with verbosity and generate Allure results
pytest -v --alluredir=%ALLURE_RESULTS%

rem Generate Allure HTML report
allure generate --clean -o %ALLURE_HTML_REPORT% %ALLURE_RESULTS%

rem Zip the Allure HTML report for sharing
powershell -command "Compress-Archive -Path '%ALLURE_HTML_REPORT%\*' -DestinationPath '%ZIP_FILE%'"

rem Run pytest-html with verbosity
pytest -v --html=%HTML_REPORTS%\report.html

endlocal
pause
