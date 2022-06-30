# !/usr/bin/env python3
# -*- coding:utf-8 -*-
import base64
import pytest
import allure
import time
import os
from py.xml import html
from selenium import webdriver
import Common.define as Define
from util.sendEmail import SendEamils

_driver = None


# 测试失败时添加截图和测试用例描述(用例的注释信息)
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     """
#     当测试失败的时候，自动截图，展示到Allure报告中
#     :param item:
#     :param Call:
#     """
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)
#     if report.when == "call" and report.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             if "tmpir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#                 f.write(report.nodeid + extra + "\n")
#             with allure.step('添加失败截图...'):
#                 allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.clear()  # 清空summary中的内容
    prefix.extend([html.p("所属部门: XX公司测试部")])
    prefix.extend([html.p("测试执行人: 随风挥手")])


@pytest.mark.optionalhook
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """收集测试结果"""
    result = {
        "total": terminalreporter._numcollected,
        'passed': len(terminalreporter.stats.get('passed', [])),
        'failed': len(terminalreporter.stats.get('failed', [])),
        'error': len(terminalreporter.stats.get('error', [])),
        'skipped': len(terminalreporter.stats.get('skipped', [])),
        # terminalreporter._sessionstarttime 会话开始时间
        # 'total times': time.timestamp() - terminalreporter._sessionstarttime
    }
    print(result)
    # if result['failed'] or result['error']:
    #     print("send report at here!")
    # SendEamils.send_allure_report_url()


# scope='Module'模块级别，也就是每个测试文件运行一次
# scope='session'回话级别，也就是整个package运行一次

@pytest.fixture(scope='session', autouse=True)
def driver():
    global _driver

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('disable-infobars')
    chrome_options.add_argument('--disable-gpu')

    # 要使自动化测试脚本在浏览器后台，需要用到headless模式
    # print('----------静默运行中----------')
    # chrome_options.add_argument('headless')
    # driver_path = Define.getDirConfig("PATH", "DRIVER_PATH")
    # _driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

    print('------------open browser------------')
    driver_path = Define.getDirConfig("PATH", "DRIVER_PATH")
    _driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    _driver.maximize_window()
    # _driver.implicitly_wait(5)
    yield _driver
    print('------------close browser------------')
    # _driver.quit()
