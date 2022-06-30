import pytest
import time
import os
from selenium.webdriver.support.wait import WebDriverWait as WD
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    TimeoutException,
    NoAlertPresentException,
)

# 从selenium里面导入webdriver
from selenium import webdriver
import Common.define as Define


class BasePage(object):
    """结合显示等待封装一些selenium内置方法"""

    def __init__(self, driver, base_url='', timeout=10):

        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link text': By.LINK_TEXT,
            'css selector': By.CSS_SELECTOR,
            'partial link text': By.PARTIAL_LINK_TEXT
        }
        self.driver = driver
        if base_url=='':
            self.base_url = Define.getDirConfig("URL", "base_url")
        else:
            self.base_url = base_url
        self.outTime = timeout

    def find_element(self, by, locator):
        """
        find alone element
        :param by: eg: id, name, xpath, css.....
        :param locator: id, name, xpath for str
        :return: element object
        """
        try:
            print('[Info:Starting find the element "{}" by "{}"!]'.format(locator, by))
            element = WD(self.driver, self.outTime).until(lambda x: x.find_element(by, locator))
        except TimeoutException as t:
            print('error: found "{}" timeout!'.format(locator), t)
        else:
            return element

    def find_elements(self, by, locator):
        """
        find group elements
        :param by: eg: id, name, xpath, css.....
        :param locator: eg: id, name, xpath for str
        :return: elements object
        """
        try:
            print('[Info:start find the elements "{}" by "{}"!]'.format(locator, by))
            elements = WD(self.driver, self.outTime).until(lambda x: x.find_elements(by, locator))
        except TimeoutException as t:
            print('error: found "{}" timeout!'.format(locator), t)
        else:
            return elements

    def is_element_exist(self, by, locator):
        """
        assert element if exist
        :param by: eg: id, name, xpath, css.....
        :param locator: eg: id, name, xpath for str
        :return: if element return True else return false
        """
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime). \
                    until(ec.visibility_of_element_located((self.byDic[by], locator)))
            except TimeoutException:
                print('Error: element "{}" not exist'.format(locator))
                return False
            return True
        else:
            print('the by:"{}" not exist!'.format(by))

    def is_click(self, by, locator):
        if by.lower() in self.byDic:
            try:
                element = WD(self.driver, self.outTime). \
                    until(ec.element_to_be_clickable((self.byDic[by], locator)))
            except TimeoutException:
                print("元素不可以点击")
            else:
                return element
        else:
            print('the "{}" error!'.format(by))

    def is_alert(self):
        """
        assert alert if exsit
        :return: alert obj
        """
        try:
            re = WD(self.driver, self.outTime).until(ec.alert_is_present())
        except (TimeoutException, NoAlertPresentException):
            print("error:no found alert")
        else:
            return re

    def switch_to_frame(self, by, locator):
        """判断frame是否存在，存在就跳到frame"""
        print('info:switching to iframe "{}"'.format(locator))
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime). \
                    until(ec.frame_to_be_available_and_switch_to_it((self.byDic[by], locator)))
            except TimeoutException as t:
                print('error: found "{}" timeout！切换frame失败'.format(locator), t)
        else:
            print('the "{}" error!'.format(by))

    def switch_to_default_frame(self):
        """返回默认的frame"""
        print('info:switch back to default iframe')
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(e)

    def get_alert_text(self):
        """获取alert的提示信息"""
        alert = self.is_alert()
        if alert:
            return alert.text
        else:
            return None

    def get_element_text(self, by, locator, name=None):
        """获取某一个元素的text信息或属性值"""
        try:
            element = self.find_element(by, locator)
            if name:
                print('get_attribute successed:"{}"'.format(element.get_attribute(name)))
                return element.get_attribute(name)
            else:
                print('get text successed:"{}"'.format(element.text))
                return element.text
        except AttributeError:
            print('get "{}" text failed return None'.format(locator))

    def load_url(self, url):
        full_url = self.base_url + url
        print('info: string upload url "{}"'.format(full_url))
        self.driver.get(full_url)

    def get_source(self):
        """获取页面源码"""
        return self.driver.page_source

    def send_keys(self, by, locator, value=''):
        """写数据"""
        try:
            element = self.find_element(by, locator)
            element.send_keys(value)
            print('info:input "{}"'.format(value))
        except AttributeError as e:
            print(e)

    def clear(self, by, locator):
        """清理数据"""
        try:
            element = self.find_element(by, locator)
            element.clear()
            print('info:clearing value')
        except AttributeError as e:
            print(e)

    def click(self, by, locator):
        """点击某个元素"""
        print('info:click "{}"'.format(locator))
        element = self.is_click(by, locator)
        if element:
            element.click()
        else:
            print('the "{}" unclickable!'.format(locator))

    @staticmethod
    def sleep(num=0):
        """强制等待"""
        print('info:sleep "{}" second'.format(num))
        time.sleep(num)

    def wait_element_to_be_located(self, by, locator):
        """显示等待某个元素出现，且可见"""
        print('info:waiting "{}" to be located'.format(locator))
        try:
            return WD(self.driver, self.outTime).until(ec.presence_of_element_located((self.byDic[by], locator)))
        except TimeoutException as t:
            print('error: found "{}" timeout！'.format(locator), t)

    def get_page_source(self):
        return self.get_source()

    # 截图并保存在图片文件夹下
    def save_web_screenshot(self):
        path = Define.getDirConfig("DIR", "IMG_PATH")
        if path is None:
            path = Define.IMG_DIR
        flag = os.path.exists(path)
        now = time.strftime('%Y-%m-%d %H-%M-%S')  # 获取当前时间,精确到秒

        if flag:
            print("文件夹：{}不存在".format(path), "DEBUG")
        else:
            print("文件夹：保存在：".format(path), "DEBUG")
            os.makedirs(path)
        filename = path + r'\img_' + now + '.png'
        try:
            self.driver.get_screenshot_as_base64()
            print("网页截图成功，保存在：{}".format(filename), "debug")
        except:
            print("请检查你定位是否正确".format(filename), "debug")
            raise

        """关闭浏览器"""

    def quit(self):
        self.driver.quit()
        print('quit the browser')

def test_main():
    # 执行到这里的时候Selenium会到指定的路径将chrome driver程序运行起来
    driver_path = Define.getDirConfig("PATH", "DRIVER_PATH")
    driver = webdriver.Chrome(driver_path)
    page = BasePage(driver, "http://172.18.188.103:8080")
    page.load_url("/csp/app/login?lang=en_US")
    driver.maximize_window()
    page.save_web_screenshot()
    BasePage.sleep(2)
    page.quit()


if __name__ == '__main__':
    pytest.main(['-v', 'basePage.py'])
