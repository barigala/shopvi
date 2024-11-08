import os
import shutil
import sys
import pytest
import time

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the Driver class after modifying sys.path
from base.DriverClass import Driver

ALLURE_RESULTS_PATH = 'D:\\PyProjects\\shopvipytest\\tests\\reports\\allurereports'

@pytest.fixture(scope="session")
def session_driver():
    """This fixture initializes the Appium driver once for the entire session."""
    print("Initializing Appium driver for the session...")
    driver = Driver().getDriverMethod()  # Initializes the driver
    yield driver
    print("Quitting Appium driver for the session...")
    driver.quit()  # Quits driver after all tests are done

@pytest.fixture(scope="class")
def class_setup(request, session_driver):
    """This fixture provides the session-level driver to all test classes."""
    request.cls.driver = session_driver  # Set session driver for test class

@pytest.fixture(scope='class')
def beforeClass(request):
    # Clean up Allure logs before the test run
    print('Cleaning Allure logs...')
    if os.path.exists(ALLURE_RESULTS_PATH):
        # Delete all files in the directory without removing the folder itself
        for filename in os.listdir(ALLURE_RESULTS_PATH):
            file_path = os.path.join(ALLURE_RESULTS_PATH, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Remove the file
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove subdirectories, if any
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

    print('Before Class')
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print('After Class')

@pytest.fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')
