#author: lladhibhutall 


import click

from .classmodule import MyClass
from .funcmodule import my_function

@click.command()
@click.argument('symbol')
def main(symbol):
    
    click.echo(my_function(symbol))


if __name__ == '__main__':
    main()

