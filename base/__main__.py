#author: lladhibhutall 


import click

from .classmodule import MyClass
from .funcmodule import my_function

@click.command()
@click.argument('symbol')
def main(symbol):
    ''' Enter the ticker symbol ''' #P look into this and give a meaningful description    
    click.echo(my_function(symbol))
    #_ = my_function(symbol)

if __name__ == '__main__':
    main()

