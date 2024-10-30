@echo off
setlocal

rem Start Appium server
rem start /B appium
rem timeout /T 10

rem Activate virtual environment
call D:\PyProjects\shopvipytest\myenv\Scripts\activate

rem Set the paths for reports
set ALLURE_RESULTS=D:\PyProjects\shopvipytest\reports\allure-results
set HTML_REPORT=D:\PyProjects\shopvipytest\reports\pytest_report.html

rem Clean up old report directories
if exist %ALLURE_RESULTS% ( rmdir /s /q %ALLURE_RESULTS% )

rem Create new allure-results directory if it doesn't exist
if not exist %ALLURE_RESULTS% ( mkdir %ALLURE_RESULTS% )

rem Run pytest with Allure and HTML reports
pytest -v --alluredir=%ALLURE_RESULTS% --html=%HTML_REPORT% --self-contained-html

rem Generate Allure HTML report
allure generate --clean -o D:\PyProjects\shopvipytest\reports\allure-report %ALLURE_RESULTS%

rem Open Allure report in the default web browser
start D:\PyProjects\shopvipytest\reports\allure-report

rem Stop Appium server
rem taskkill /F /IM node.exe

endlocal
