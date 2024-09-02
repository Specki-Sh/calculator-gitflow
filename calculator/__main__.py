from calculator.cli import CLI
from calculator.operations import subtract, multiply

if __name__ == "__main__":
    opt = {
        'subtract': subtract,
        'multiply': multiply
    }

    cli = CLI(opt)
    cli.run()
