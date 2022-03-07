class Logger:

    def __init__(self) -> None:
        self.log_file = open('gameplay.log', 'a+')

    def write_log(self, data) -> None:
        self.log_file.write(data)

    def close_log(self) -> None:
        self.log_file.close()
