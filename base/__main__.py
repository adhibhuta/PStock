#author: lladhibhutall 


import sys
import argparse
import click

from .classmodule import MyClass
from .funcmodule import my_function

@click.command()
@click.argument('symbol')
def main(symbol):
    #parser = argparse.ArgumentParser()
    #parser.add_argument('--symbol', type=str, default='googl',
		        #help='Name of the stock for price') #P change this to something meaningful   
    #args =  parser.parse_args()
    click.echo(my_function(symbol))

    #my_function('hello world')

    #my_object = MyClass('Debjyoti')
    #my_object.say_name()

if __name__ == '__main__':
    main()

