#author: lladhibhutall 
import pprint
import click

from .classmodule import MyClass
from .funcmodule import my_function, sort_by_time
from .drawmodule import draw_plot
@click.command()
@click.argument('symbol')
def main(symbol):
    ''' Enter the Symbol'''  
    pp = pprint.PrettyPrinter(indent=4)
    #click.echo(my_function(symbol))
    unsorted_list = my_function(symbol)
    sorted_list = sort_by_time(unsorted_list)
    #pp.pprint(sorted_list)
    draw_plot(sorted_list)

if __name__ == '__main__':
    main()

