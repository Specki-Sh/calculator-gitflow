from calculator import operations
from calculator.cli import CLI

if __name__ == "__main__":
    opt = {
        'add': operations.add,
        'subtract': operations.subtract,
        'multiply': operations.multiply,
    }

    cli = CLI(opt)
    cli.run()
