import logging

class Logger:
    def __init__(self, name, level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        format = '%(asctime)s\t%(filename)s\t%(lineno)d : %(message)s'
        formatter = logging.Formatter(format)
        
        # 创建一个处理器并设置格式
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        # 将处理器添加到日志记录器
        self.logger.addHandler(handler)

    def debug(self, message):
        level=   'DEBUG  '  
        self.logger.debug(level+message)

    def info(self, message):
        level=   'INFO  '  
        self.logger.info(level+message)

    def warning(self, message):
        level= '\033[33m' + 'WARNING  ' 
        self.logger.warning(level+message+'\033[0m')

    def error(self, message):
        level= '\033[31m' + 'ERROR  '
        self.logger.error(level+message+'\033[0m')

    def critical(self, message):
        level= '\033[31m' + 'CRITICAL  '
        self.logger.critical(level+message+'\033[0m')




if __name__ == '__main__':

    # 使用自定义的日志管理器
    logger = Logger("my_logger")

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
