import logging

class Logger:
    def __init__(self, name, level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        format = '%(asctime)s %(filename)s %(lineno)d : %(message)s'
        formatter = logging.Formatter(format)
        
        # 创建一个处理器并设置格式
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        # 将处理器添加到日志记录器
        self.logger.addHandler(handler)

    def debug(self, message,*args):
        level=   'DEBUG  '  
        self.logger.debug(level+message,*args)

    def info(self, message,*args):
        level=   'INFO  '  
        self.logger.info(level+message,*args)

    def warning(self, message,*args):
        level= '\033[33m' + 'WARNING  ' 
        self.logger.warning(level+message+'\033[0m',*args)

    def error(self, message,*args):
        level= '\033[31m' + 'ERROR  '
        self.logger.error(level+message+'\033[0m',*args)

    def critical(self, message,*args):
        level= '\033[31m' + 'CRITICAL  '
        self.logger.critical(level+message+'\033[0m',*args)


global logger
logger = Logger("default",logging.INFO)


if __name__ == '__main__':

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")

    logger.warning("test : %d , name : %s",12345,"1-5")
