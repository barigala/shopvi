@echo off
setlocal

rem Start Appium server (optional if you want to start Appium before running tests)
rem start /B appium
rem timeout /T 10

rem Activate virtual environment
call D:\PyProjects\shopvipytest\myenv\Scripts\activate

rem Paths setup
set WORKSPACE_DIR=D:\PyProjects\shopvipytest
set ALLURE_RESULTS=%WORKSPACE_DIR%\tests\reports\allure-results
set HTML_REPORT=%WORKSPACE_DIR%\tests\reports\pytest_report.html
set ALLURE_REPORT=%WORKSPACE_DIR%\tests\reports\allure-report
set ALLURE_SINGLE_FILE_REPORT=%WORKSPACE_DIR%\allure-report\allure-single-file-report.html

echo Workspace Directory: %WORKSPACE_DIR%
echo Allure Results Directory: %ALLURE_RESULTS%
echo HTML Report: %HTML_REPORT%
echo Allure Report Directory: %ALLURE_REPORT%
echo Allure Single File Report: %ALLURE_SINGLE_FILE_REPORT%

rem Clean up old results and reports
if exist %ALLURE_RESULTS% ( rmdir /s /q %ALLURE_RESULTS% )
if exist %ALLURE_REPORT% ( rmdir /s /q %ALLURE_REPORT% )

rem Create allure-results directory if it doesn't exist
if not exist %ALLURE_RESULTS% ( mkdir %ALLURE_RESULTS% )

rem Run pytest with Allure and HTML reports
pytest -v --alluredir=%ALLURE_RESULTS% --html=%HTML_REPORT% --self-contained-html

rem Generate Allure report with clean option
allure generate --clean %ALLURE_RESULTS% -o %ALLURE_REPORT%

rem Generate single-file Allure report
allure generate --single-file %ALLURE_RESULTS% --clean -o %ALLURE_SINGLE_FILE_REPORT%

rem Serve Allure report (open the report in a browser)
allure serve %ALLURE_RESULTS%

rem Stop Appium server (optional if you want to stop Appium after running tests)
rem taskkill /F /IM node.exe

endlocal
