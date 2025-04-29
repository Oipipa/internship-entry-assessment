from abc import ABC, abstractmethod

class A(ABC):
    def __init__(self, name: str):
        self._name = name  

    @abstractmethod
    def print_name(self) -> None:
        ...

class B(A):
    def __init__(self, name: str):
        super().__init__(name)

    def __print_name(self, message: str) -> None:  
        print(f"{message}: {self._name}")

class C(B):
    def print_name(self, message: str = "C says") -> None:
        print(f"{message}: {self._name}")

class D(A):
    def print_name(self) -> None:
        print(f"D here – my name is {self._name}")

# Smoke test
if __name__ == "__main__":
    d = D("Delta")
    d.print_name()

    c = C("Charlie")
    c.print_name() 
    c.print_name("Custom message") 