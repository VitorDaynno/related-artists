class FileHelper:

    def __init__(self):
        self.__file = None

    def open(self, file, mode):
        self.__file = open(file, mode)

    def write(self, line):
        self.__file.write(line + "\n")

    def close(self):
        self.__file.close()

    def get_lines(self):
        return self.__file.readlines()