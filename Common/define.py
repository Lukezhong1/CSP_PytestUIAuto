from datetime import datetime
import configparser
import os
from Common.log import Log

# 项目根目录,os.path.dirname 获取当前文件的上层路径
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件的路径，要求放在项目所在位置的上层路径
Path_DIR = os.path.join(ROOT_DIR, 'Config')

# ui元素库文件所在目录
UI_CONF = os.path.join(ROOT_DIR, 'PageLocators')

log = Log()


# 从配置文件中读取用户配置信息
def getDirConfig(section, key):
    config = configparser.ConfigParser()
    # 读取配置文件的路径
    path = os.path.join(Path_DIR, "path.conf")
    try:
        config.read(path, encoding='utf-8')
        return config.get(section, key)
    except configparser.NoOptionError as e:
        log.error(e)
        return 'error: No option "{}" in section: "{}"'.format(path, section)


# 从用户配置文件中读取DB配置文件里面的内容
def getDBConfig(section: object, key: object) -> object:
    path = getDirConfig("PATH", "DB_PATH")
    config = configparser.ConfigParser()
    try:
        config.read(path, encoding='utf-8')
        return config.get(section, key)
    except configparser.NoOptionError as e:
        log.error(e)
        return 'error: No option "{}" in section: "{}"'.format(path, section)


# 从用户配置文件中读取email 配置文件里面的内容
def getEmailSetting(section, key):
    path = getDirConfig("PATH", "EMAIL_PATH")
    config = configparser.ConfigParser()
    try:
        config.read(path, encoding='utf-8')
        return config.get(section, key)
    except configparser.NoOptionError as e:
        log.error(e)
        return 'error: No option "{}" in section: "{}"'.format(path, section)


# 读取Path 配置文件里面的内容
def getLocatorDir(section, key):
    path = getDirConfig("path", "locator_path")
    config = configparser.ConfigParser()
    try:
        config.read(path, encoding='utf-8')
        return config.get(section, key)
    except configparser.NoOptionError as e:
        log.error(e)
        return 'error: No option "{}" in section: "{}"'.format(path, section)

# 读取数组元素的例子，这个也可以放在使用的时候再解析
def getArra(section, key):
    path = getDirConfig("PATH", "EMAIL_PATH")
    config = configparser.ConfigParser()
    try:
        config.read(path, encoding='utf-8')
        return tuple(config.get(section, key).split(","))
    except configparser.NoOptionError as e:
        log.error(e)
        return 'error: No option "{}" in section: "{}"'.format(path, section)



if __name__ == '__main__':
    db_dir = getDirConfig("PATH", "DB_PATH")
    db_host = getDBConfig("DATABASE", "DB_HOST")
    email_host = getArra("EMAIL", "TO_USER")
    print(db_dir,db_host,email_host)
