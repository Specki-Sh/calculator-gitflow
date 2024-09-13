import sys
from typing import Callable, Dict


class CLI:
    operations: Dict[str, Callable]

    def __init__(self, operations: Dict[str, Callable]) -> None:
        self.operations = operations

    def run(self):
        if len(sys.argv) < 2:
            print("Usage: python calculator <operation> [args...]")
            return

        operation_name = sys.argv[1]
        args = sys.argv[2:]

        if operation_name not in self.operations:
            print(f"Operation '{operation_name}' not found.")
            return

        try:
            result = self.operations[operation_name](*args)
            if result is not None:
                print(result)
        except TypeError as e:
            print(f"Argument error during operation '{operation_name}': {e}")
        except Exception as e:
            print(f"Error during operation '{operation_name}': {e}")
