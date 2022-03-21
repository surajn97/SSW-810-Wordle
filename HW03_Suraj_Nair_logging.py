import os


class Logger:

    def __init__(self) -> None:
        self.log_file = open('gameplay.log', 'a+')

    def write_log(self, data) -> None:
        self.log_file.write(data)

    def close_log(self) -> None:
        self.log_file.close()

    def __str__(self) -> str:
        if self.log_file and os.stat('gameplay.log').st_size != 0:
            temp_file = open('gameplay.log', 'r')
            x = temp_file.read()
            temp_file.close()
            return 'All Logs:\n' + x
        else:
            return 'No Logs created yet.'
