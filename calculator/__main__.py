from calculator.cli import CLI
from calculator.operations import subtract

if __name__ == "__main__":
    opt = {'subtract': subtract}

    cli = CLI(opt)
    cli.run()
