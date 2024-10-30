@echo off
setlocal

rem Start Appium server
start /B appium
timeout /T 10

rem Activate virtual environment
call D:\PyProjects\shopvipytest\myenv\Scripts\activate

rem Set the paths for reports
set ALLURE_RESULTS=D:\PyProjects\shopvipytest\reports\allurereports
set HTML_REPORT=D:\PyProjects\shopvipytest\reports\pytest_report.html
set ALLURE_HTML_REPORT=D:\PyProjects\shopvipytest\reports\allure_report

rem Clean up old report directories
if exist %ALLURE_RESULTS% ( rmdir /s /q %ALLURE_RESULTS% )
if exist %ALLURE_HTML_REPORT% ( rmdir /s /q %ALLURE_HTML_REPORT% )

rem Create new report directories
mkdir %ALLURE_RESULTS%

rem Run pytest with Allure and HTML reports
pytest -v --alluredir=%ALLURE_RESULTS% --html=%HTML_REPORT% --self-contained-html

rem Generate Allure HTML report
allure generate --clean -o %ALLURE_HTML_REPORT% %ALLURE_RESULTS%

rem Open Allure report in the default web browser
start %ALLURE_HTML_REPORT%

rem Stop Appium server
taskkill /F /IM node.exe

endlocal
