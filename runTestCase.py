import pytest
import os
import Common.define as Define
from util.sendEmail import SendEamils

if __name__ == '__main__':
    # 使用配置路径生成report
    path = Define.getDirConfig("DIR", "REPORT_DIR")
    HOST = Define.getDirConfig("REPORT", "ALLURE_HOST")
    PORT = Define.getDirConfig("REPORT", "ALLURE_PORT")
    # pytest.main(['TestCase', '--alluredir', path])

    pytest.main(['TestCase/reportFuncSetupCase', '--alluredir', path])

    # 在对应的配置路径下启动allure server.注意启动的服务器上需要安装allure server,allure allure-commandline
    os.system('allure serve -h '+HOST+' -p '+PORT+' ' + path)

