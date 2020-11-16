from dependant import Dependent
from typing import List

class Employee:
    #   internal attributes prepended with _ not accessed/modified
    #   directly outside class, only through intermediaries or
    #   getters/setters
    def __init__(self):
        self._first_name = ""
        self._last_name = ""
        self._num_of_dependents = 0
        self._dependents = []
        
    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def num_of_dependents(self) -> int:
        return len(self._dependents)

    @property
    def dependents(self):
        return self._dependents

    @dependents.setter
    def dependents(self, dependents: List[Dependent]) -> None:
        self._dependents = dependents

    def add_dependant(self, dependant: Dependent) -> None:
        self._dependents.append(dependant)

    def output_employee_info(self) -> None:
        print("Employee name: {} {} \n".format(self.first_name, self.last_name) )
        print("Number of dependents: {} \n".format(self.num_of_dependents))
        print("Dependents: \n")
        for dependent in self.dependents:
            dependent.output_dependent_info()

