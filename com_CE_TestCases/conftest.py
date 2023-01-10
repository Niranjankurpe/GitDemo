import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browserName = request.config.getoption("browser_name")
    if browserName == "chrome":
        service_obj = Service(r'E:\selenium\chrome driver\chromedriver.exe')
        driver = webdriver.Chrome(service=service_obj)
    elif browserName == "edge":
        Service_obj = Service("E:\selenium\msedgedriver.exe")
        driver = webdriver.Edge(service=Service_obj)
    elif browserName == "firefox":
        print("Running")

    driver.get("https://www.coursera.org/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.rcvacadmy.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory=os.path.dirname(item.config.option.htmlpath)
            file_name=report.nodeid.replace("::","_")+".png"
            destinetionFile=os.path.join(report_directory,file_name)
            driver.save_screenshot(destinetionFile)
            if file_name:
                html='<div><img src="%s" alt="screenshot" style="width=300px;height=200px"' \
                     'onclick="windo.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_report_title(report):
    report.title = "Coursera HTML report!"






















