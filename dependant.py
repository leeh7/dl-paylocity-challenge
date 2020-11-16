class Dependent:
    #   internal attributes prepended with _ not accessed/modified
    #   directly outside class, only through intermediaries or
    #   getters/setters
    def __init__(self):
        self._first_name = ""
        self._last_name = ""
        
    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self._last_name = last_name

    def output_dependent_info(self) -> None:
        print("    Dependent name: {} {} \n".format(self.first_name, self.last_name) )
        print("---------- \n")