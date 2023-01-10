import time

import pytest
from selenium import webdriver

from com_CE_Pages.EducationHomePage import HomePage
from com_CE_Testdata.HomePageData import HomePageData
from com_CE_Utilities.UtilClass import BaseClass

class TestEducation(BaseClass):
    @pytest.fixture(params=HomePageData.getTestData("testcase2"))
    def getData(self, request):
        return request.param

    def test_Education(self, getData):

        log = self.getLogger()
        log.info("print 1st two course")

        self.driver.implicitly_wait(20)
        Home = HomePage(self.driver)

        Home.sendname().send_keys(getData["searchdata"])
        #log.info("search" + getData[0])

        #enter on search bar
        #driver.find_element(By.XPATH, "//input[@placeholder='What do you want to learn?']").send_keys("web development")
        #Home.sendname().send_keys("web development")
        #time.sleep(15)

        # Headless mode execution=
        #chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("headless")
        #chrome_options.add_argument("--ignore-certificate-errors")

        Home.pressEnter().click()

        #Title = Home.pageTitle().text
        #assert "Learn without limits" in Title

        #select web development option
        #driver.find_element(By.XPATH, "//span[normalize-space()='web development']").click()
        #Home.clickWD().click()
        #time.sleep(20)

        #click on Begginer
        #driver.find_element(By.XPATH, "//span[contains(text(),'Beginner')]").click()
        Home.clickBginer().click()
        #time.sleep(40)


        #click on "show more " language
        #driver.find_element(By.XPATH, "(//span[@class='cds-2 cds-button-label'])[11]").click()
        Home.clickshowm().click()
        #time.sleep(30)

        #click on english language
        #driver.find_element(By.XPATH, "//span[contains(text(),'English')]").click()
        #time.sleep(30)
        Home.clickeng().click()

        #driver.find_element(By.XPATH, "//input[@aria-labelledby='cds-react-aria-660-label-text']").click()
        #time.sleep(30)
        #sc = Select(driver.find_element(By.XPATH, "//input[@aria-labelledby='cds-react-aria-660-label-text']"))
        #sc.select_by_visible_text("English")
        #time.sleep(30)

        #click on apply
        #driver.find_element(By.XPATH, "//span[normalize-space()='Apply']").click()
        Home.clickApply().click()
        time.sleep(5)

        firstcoursetitle = Home.firstcoursename().text
        print("1st course name :- " +firstcoursetitle)

        firstratting = Home.firstcourseRating().text
        print("1st course rating :-" +firstratting)

        fristCtime = Home.firstcoursetime().text
        print("Time duration :- " +fristCtime)


        #show 1st course info
        #firstcourse = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Meta Front-End Developer professional certificate by [object Object]'] div[class='css-ilhc4l']").text
        #print(firstcourse)
        fs = Home.clickfirst().text
        print(fs)

        #show 2nd course info
        #secondcourse = driver.find_element(By.CSS_SELECTOR, "a[aria-label='IBM Full Stack Software Developer professional certificate by [object Object]'] div[class='css-ilhc4l']").text
        #print(secondcourse)
        sc = Home.clicksecond().text
        print(sc)

        #assertion done for first 2 course name
        ff = Home.clickfirstast().text
        assert "Meta Front-End Developer" in ff

        ss = Home.clicknd().text
        assert "IBM Full Stack Software Developer" in ss

        #assertion to check display courses for begginer only
        beginer = Home.begineeronly().text
        assert "Beginner" in beginer

        star = Home.rattingplus()
        assert star.text >= '4.0'

        #ss = Home.clicknd().text
        #assert "IBM Full Stack Software Developer" in ss
        #ss = Home.clicknd().text
        #if ss == "IBM Full Stack Software Developer":
            #assert True
        #else:
            #self.driver.get_screenshot_as_file("C:/Users/niran/PycharmProjects/python_Coursera/com_CE_Utilities/screenshot.png")
            #assert False

        #star = Home.rattingplus()
        #for i in star:
            #if star.text >= '4.0':
                #assert True
            #else:
                #print(star.text)

        #star = Home.rattingplus()
        #if star == 4.0:
            #assert True
        #else:
            #print(star)

