from calculator import operations
from calculator.cli import CLI
from calculator.operations import subtract, multiply

if __name__ == "__main__":
    opt = {
        'add': operations.add,
        'subtract': subtract,
        'multiply': multiply,
    }

    cli = CLI(opt)
    cli.run()
