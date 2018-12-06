#author: lladhibhutall 


import sys
import argparse
import click

from .classmodule import MyClass
from .funcmodule import my_function

@click.command()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--symbol', type=str, default='googl',
		        help='Name of the stock for price') #P change this to something meaningful   
    args =  parser.parse_args()
    sys.stdout.write(my_function(args))

    #my_function('hello world')

    #my_object = MyClass('Debjyoti')
    #my_object.say_name()

if __name__ == '__main__':
    main()

