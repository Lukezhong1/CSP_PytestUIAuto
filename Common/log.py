import logging
import time
import os

'''
Log 日志的封装 
日志级别：
'''

class Log():
    def __init__(self, logging_name = '', path: object = '') -> object:
        print(os.path.abspath(__file__))
        if path == '':
            path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        flag = os.path.exists(path)
        # 指定格式
        # 创建api_log+时间命名的文本名称
        now = time.strftime('%Y-%m-%d %H-%M-%S')  # 获取当前时间,精确到秒

        if flag:
            # print("path exist")
            pass
        else:
            # create file path
            os.makedirs(path)
        self.filepath = path + r'\api_log' + now + '.txt'
        self.logging = logging_name  # 日志收集名字，默认为空

    def my_log(self, msg, levl):
        # level：用来选择日志输出格式，默认DEBUG
        # msg：用来编写输入的内容

        # 新建一个日志收集器
        my_logger = logging.getLogger(self.logging)  # 日志收集器名字
        my_logger.setLevel('DEBUG')  # 设定收集的级别

        # 指定格式
        fm = logging.Formatter('%(asctime)s -  %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d ]')

        # 新建一个输出渠道并指定到控制台，输出的级别为DEBUG
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(fm)

        file_handler = logging.FileHandler(self.filepath, encoding='utf-8')
        file_handler.setLevel('DEBUG')  # 指定输出级别
        file_handler.setFormatter(fm)

        # 对接
        my_logger.addHandler(ch)
        my_logger.addHandler(file_handler)

        if levl.upper() == 'DEBUG':
            my_logger.debug(msg)
        elif levl.upper() == 'INFO':
            my_logger.info(msg)
        elif levl.upper() == 'WARNING':
            my_logger.warning(msg)
        elif levl.upper() == 'ERROR':
            my_logger.error(msg)
        elif levl.upper() == 'CRITICAL':
            my_logger.critical(msg)

        # 移除输出格式和存放路径,避免重复输出
        my_logger.removeHandler(ch)
        my_logger.removeHandler(file_handler)

        # 关闭文件
        file_handler.close()

    def __del__(self):
        class_name = self.__class__.__name__
        # print(class_name, '销毁')

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')



if __name__ == '__main__':
    log = Log()
    log.debug("test message")
    log.info("test message")
    log.error("test message")
    log1 = Log()
    log1.debug("test message")
    log1.info("test message")
    log1.error("test message")
