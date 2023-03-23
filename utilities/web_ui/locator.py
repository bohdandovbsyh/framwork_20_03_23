class Locator:
    def __init__(self, method: str, locator_string: str):
        self.__method = method
        self.__locator_string = locator_string

    def get_locator(self) -> tuple:
        return self.__method, self.__locator_string
