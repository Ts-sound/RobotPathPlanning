import logging

class Logger:
    def __init__(self, name, level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        format = '%(asctime)s %(filename)s %(funcName)s %(lineno)d %(levelname)s : %(message)s'
        formatter = logging.Formatter(format)
        
        # 创建一个处理器并设置格式
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        # 将处理器添加到日志记录器
        self.logger.addHandler(handler)

    def get(self):
        return self.logger

global logger
logger = Logger("default",logging.DEBUG).get()


if __name__ == '__main__':

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")

    # logger.warning("test : %d , name : %s",12345,"1-5")
