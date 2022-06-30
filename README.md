Pytest框架实战项目实例
帮助：
    通过此项目可以学到以下内容
    1.命令行如何运行测试用例
    2.pytest如何收集测试用例
    3.如何使用fixture
    4.如何使用conftest.py文件
    5.如何使用pytest-html插件生成测试报告
    6.PO设计模式思想是什么样的
    7.selenium 部分API的使用和如何进行简单的二次封装
    8.pytest框架如何参数化测试用例
    9.如何发送测试报告邮件
    10.如何使用代码的方式执行测试用例或整个项目
    11.测试用例编写逻辑
说明：
    1.本项目测试地址为
    http://172.18.188.103:8080/csp/app/login?lang=en_US
    2.请先简单了解项目的各个功能
环境要求：
    1.windows 7 以上版本
    2.需安装python 3以上版本
    3.selenium 2 以上版本
    4.需安装pytest框架
    5.需安装pytest -html插件
    6.需安装谷歌浏览器及对应驱动
    7.需要安装yagmail库发送测试报告
    8.需安装pymysql对数据库连接及操作
运行项目：
    为本项目建立的空白的虚拟环境
    在虚拟环境中使用： pip install -r requirements.txt   自动安装依赖
    1.下载项目到本地
    2.打开cmd切换到项目根目录
    3.输入python RunTestCase.py运行项目生成报告
    4.或者直接通过pytest --html=report/report.html 运行
    5.或者在pycharm中打开项目，直接运行RunTestCase.py文件（新建一个python工程后，工程PYthon interpreter为虚拟环境，左上角file->Setting->Tools->Python Integrated Tools->项目名称->Default test runner->选择py.test）
    6.pytest --alluredir report
    查看报告 allure serve report

